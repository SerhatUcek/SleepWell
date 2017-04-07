""" 
    The script is designed for scraping hotel prices from Trivago website.
    It saves scraping result in easy to read HTML file.
"""
import argparse
import time
from selenium.common.exceptions import NoSuchElementException, \
    StaleElementReferenceException
from tqdm import tqdm
from browser import Browser
from report import save
from urlbuilder import make_url


class SleepWell:
    def __init__(self, location, date_from, date_to, stars, reviews, distance, max_price):
        self.location = self.get_location_id(location)
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.reviews = reviews
        self.distance = distance
        self.max_price = max_price
        self.report = '{} - {}'.format(location, time.strftime("%Y-%m-%d %H%M"))

    @staticmethod
    def get_location_id(location):
        with Browser() as browser:
            browser.get("http://trivago.pl")
            browser.find_element_by_css_selector("input.input.horus__querytext.js-query"
                                                 "-input").send_keys(location)
            browser.find_element_by_css_selector("div.horus__col.horus__col--search >"
                                                 " button > span").click()
            time.sleep(3)
            location_id = [x.replace("iPathId=", "") for x in browser.current_url.split(
                "&") if "iPathId" in x][0]
            return location_id

    @staticmethod
    def get_data(browser):
        while True:
            date = browser.find_element_by_class_name("btn-horus__value")
            hotels = browser.find_elements_by_class_name("hotel")
            for hotel in hotels:
                try:
                    name = hotel.find_element_by_class_name("name__copytext")
                    price = hotel.find_element_by_class_name("item__best-price")
                    website = hotel.find_element_by_class_name("item__deal-best-ota")
                    data = {
                        'Name': name.text,
                        'Price': int(price.text.translate(str.maketrans('', '', 'zł '))),
                        'Website': website.text,
                        'Date': date.text.split(",")[1]
                    }
                    yield data
                except StaleElementReferenceException:
                    pass
            try:
                next_page = browser.find_element_by_class_name("btn--next")
                next_page.click()
                time.sleep(5)
            except NoSuchElementException:
                break

    def run(self):
        urls = make_url(self.location, self.date_from, self.date_to, self.stars,
                        self.reviews, self.distance)
        hotels = []
        with tqdm(total=len(urls)) as pbar:
            for url in urls:
                with Browser() as browser:
                    browser.get(url)
                    for hotel in self.get_data(browser):
                        if hotel['Price'] < self.max_price:
                            hotels.append(hotel)
                        else:
                            break
                pbar.update(1)
        hotels = sorted(hotels, key=lambda k: k['Price'])
        save(self.report, hotels, self.location, self.date_from, self.date_to, self.stars,
             self.reviews, self.distance, self.max_price)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--location")
    parser.add_argument("-df", "--date_from")
    parser.add_argument("-dt", "--date_to")
    parser.add_argument("-s", "--stars", default="1,2,3,4,5")
    parser.add_argument("-r", "--reviews", default="1,2,3,4,5")
    parser.add_argument("-d", "--distance", nargs="?", default=None)
    parser.add_argument("-mp", "--max_price", nargs="?", default=100000, type=int)
    args = parser.parse_args()
    SleepWell(args.location, args.date_from, args.date_to, args.stars, args.reviews,
              args.distance, args.max_price).run()
