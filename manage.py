from flask import url_for
from flask_script import Manager
import urllib.parse

from app import app, initialize_app

initialize_app(app)

manager = Manager(app)


@manager.command
def hello():
    print("Hello")


@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


@manager.command
def scaffold():
    from app import db
    db.create_all()


if __name__ == "__main__":
    manager.run()
