from jinja2 import Environment, FileSystemLoader


def save(name, hotels, location, date_from, date_to, stars, reviews, distance, max_price):
    env = Environment(loader=FileSystemLoader('templates'))
    report = env.get_template('report.html')
    report.stream(hotels=hotels, location=location, date_from=date_from, date_to=date_to,
                  stars=stars, reviews=reviews, distance=distance,
                  max_price=max_price).dump(name + '.html')