import pandas as pd

from bs4 import BeautifulSoup

from datetime import datetime
from dateutil.relativedelta import relativedelta


def parse_station(station, begin_date, end_date):
    """
    This function parses the web pages downloaded from wunderground.com
    into a flat CSV file for the station you provide it.

    Make sure to run the wunderground_scraper() first so you have the web
    pages downloaded.

    :param station: The name of station. Example -> KSFO
    :param begin_date: Example -> '2014-1'
    :param end_date: Example -> '2014-12'
    """

    # Parse the HTML files between January 1, 2014 and December 31, 2014.
    # You can change the dates here if you prefer to parse a different range.
    current_date = datetime.strptime(begin_date, "%Y-%m")
    end_date = datetime.strptime(end_date, "%Y-%m") + relativedelta(months=+1)

    while current_date != end_date:
        # Here you can choose the path you want, this folder is hidden
        # as it is only HTML for the parser.
        with open('wund_html/{}/{}-{}.html'.format(station,
                                                   current_date.year,
                                                   current_date.month)) as in_file:

            soup = BeautifulSoup(in_file.read(), 'html.parser')
            weather_data = soup.tbody.find_all('tbody')

            # Get all tables columns from HTML.
            dates = []
            temperatures = []
            dew_points = []
            humidities = []
            wind_speeds = []
            pressures = []
            precipitations = []

            for tbody, html in enumerate(weather_data):
                for td in html.stripped_strings:
                    if td.replace('.', '').isnumeric():
                        if tbody == 0:
                            day = f'{current_date.year}-{current_date.month}-{td}'
                            dates.append(day)
                        elif tbody == 1:
                            temperatures.append(td)
                        elif tbody == 2:
                            dew_points.append(td)
                        elif tbody == 3:
                            humidities.append(td)
                        elif tbody == 4:
                            wind_speeds.append(td)
                        elif tbody == 5:
                            pressures.append(td)
                        else:
                            precipitations.append(td)

            # Separates the columns into maximum, mean and minimum
            # like the table on the web page of WunderGround.
            max_temps_f = list(temperatures[::3])
            mean_temps_f = list(temperatures[1::3])
            min_temps_f = list(temperatures[2::3])
            max_dewpoints_f = list(dew_points[::3])
            mean_dewpoints_f = list(dew_points[1::3])
            min_dewpoints_f = list(dew_points[2::3])
            max_humidities = list(humidities[::3])
            mean_humidities = list(humidities[1::3])
            min_humidities = list(humidities[2::3])
            max_wind_speeds = list(wind_speeds[::3])
            mean_wind_speeds = list(wind_speeds[1::3])
            min_wind_speeds = list(wind_speeds[2::3])
            max_pressures = list(pressures[::3])
            mean_pressures = list(pressures[1::3])
            min_pressures = list(pressures[2::3])

            # Best way to save a table.
            data_frame = pd.DataFrame({
                'DATE': dates,
                'Max TemperatureF': max_temps_f,
                'Mean TemperatureF': mean_temps_f,
                'Min TemperatureF': min_temps_f,
                'Max Dew PointF': max_dewpoints_f,
                'Mean Dew PointF': mean_dewpoints_f,
                'Min Dew PointF': min_dewpoints_f,
                'Max Humidity': max_humidities,
                'Mean Humidity': mean_humidities,
                'Min Humidity': min_humidities,
                'Max Wind SpeedMPH': max_wind_speeds,
                'Mean Wind SpeedMPH': mean_wind_speeds,
                'Min Wind SpeedMPH': min_wind_speeds,
                'Max PressureHG': max_pressures,
                'Mean PressureHG': mean_pressures,
                'Min PressureHG': min_pressures,
                'PrecipitationIn': precipitations,
            })

            # Pass data frame of the month to a CSV file.
            data_frame.to_csv('wund_weather_data/{}-{}.csv'.format(
                current_date.year, current_date.month), index=False)
            print(f'{current_date.year}-{current_date.month}.csv done.')

        current_date += relativedelta(months=+1)


# Example program.
parse_station('SBFZ', '2018-1', '2018-12')
