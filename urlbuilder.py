from pendulum import Pendulum
from urllib.parse import urlencode


def date_range(date_from, date_to):
    date_from = Pendulum.create_from_format(date_from, "%Y-%m-%d")
    date_to = Pendulum.create_from_format(date_to, "%Y-%m-%d")
    period = date_to - date_from

    for date in period:
        yield date, date.add(days=1).to_date_string()


def make_url(location, date_from, date_to, stars, reviews, distance):
    urls = []
    base_url = 'https://www.trivago.pl/?'
    for today, tomorrow in date_range(date_from, date_to):
        params = {
            'iPathId': location,
            'aDateRange[arr]': today,
            'aDateRange[dep]': tomorrow,
            'aCategoryRange': stars,
            'aOverallLiking': reviews,
            'iGeoDistanceLimit': distance,
            'sOrderBy': 'price asc',
        }
        urls.append(base_url + urlencode(params))
    return urls
