import os

from datetime import datetime
from dateutil.relativedelta import relativedelta

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def scrape_station(station, begin_date, end_date):
    """
    This function scrapes the weather data web pages from wunderground.com
    for the station you provide it.
    You can look up your city's weather station by performing a search for
    it on wunderground.com then clicking on the "History" section.
    The 4-letter name of the station will appear on that page.

    Update: This works fine now with the new web pages with JS from WunderGroud.
    However, it is extremely slow because it uses Selenium with ChromeDriver, so
    I made sure that it only looks for the wunderground.com pages of the months,
    as it is much better to do this with only 12 pages than 365. I advise testing
    with every page of each day of the year, try to make sure that it works with
    the date you prefer to use.

    :param station: The name of station. Example -> KSFO
    :param begin_date: Example -> '2014-01'
    :param end_date: Example -> '2014-01'
    """

    # Scrape between January 1, 2014 and December 31, 2014.
    # You can change the dates here if you prefer to parse a different range.
    current_date = datetime.strptime(begin_date, '%Y-%m')
    end_date = datetime.strptime(end_date, '%Y-%m') + relativedelta(months=+1)

    try:
        # Create a directory for each station web pages
        os.mkdir(f'wund_html/{station}')
    except FileExistsError:
        os.replace(f'wund_html/{station}', f'wund_html/{station}')

    # Use .format(station, YYYY, M).
    lookup_url = 'https://www.wunderground.com/history/monthly/{}/date/{}-{}'

    while current_date != end_date:

        if current_date.day == 1:
            print(f'{current_date} {station}')

        formatted_lookup_url = lookup_url.format(station,
                                                 current_date.year,
                                                 current_date.month)

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')

        driver = webdriver.Chrome(options=options)
        driver.get(formatted_lookup_url)
        wait = WebDriverWait(driver, 30)
        table = wait.until(lambda d: d.find_element_by_class_name('days'))

        # Here you can choose the path you want, this folder is hidden
        # as it is only HTML for the parser.
        out_file_name = 'wund_html/{}/{}-{}.html'.format(station,
                                                         current_date.year,
                                                         current_date.month)

        with open(out_file_name, 'w', encoding='utf-8') as out_file:
            out_file.write(table.get_attribute('innerHTML'))

        current_date += relativedelta(months=+1)


# Example program.
scrape_station('SBFZ', begin_date='2018-2', end_date='2018-12')
