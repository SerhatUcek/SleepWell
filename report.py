from jinja2 import Environment, FileSystemLoader


def save(name, hotels):
    env = Environment(loader=FileSystemLoader('templates'))
    report = env.get_template('report.html')
    report.stream(hotels=hotels).dump(name + '.html')