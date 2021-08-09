import pandas as pd

from datetime import datetime
from dateutil.relativedelta import relativedelta


def combine_wunderground_csv_files(begin_date, end_date):
    """
    This function combines the csv files generated after
    using the wunderground_parser () function.

    :param begin_date: Example -> '2014-01'
    :param end_date: Example -> '2014-01'
    """

    # Combines the files between January 1, 2014 and December 31, 2014.
    # You can change the dates here if you prefer to parse a different range.
    current_date = datetime.strptime(begin_date, "%Y-%m")
    end_date = datetime.strptime(end_date, "%Y-%m") + relativedelta(months=+1)

    # List with the files name.
    all_filenames = []
    while current_date != end_date:
        # Save the filename in the list 'all_filenames'.
        all_filenames.append('wund_weather_data/{}-{}.csv'.format(
            current_date.year, current_date.month
        ))
        current_date += relativedelta(months=+1)

    # Combine all files in the list and export as CSV.
    combined_csv = pd.concat([pd.read_csv(file) for file in all_filenames])
    combined_csv.to_csv('../csv_matplotlib/fortaleza_rainfall_{}.csv'.format(
        current_date.year - 1), index=False, encoding='utf-8-sig'
    )


# Example program.
combine_wunderground_csv_files('2018-1', '2018-12')
