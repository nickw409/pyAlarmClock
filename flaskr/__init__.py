import os, threading
from flask import Flask
from . import alarm, server


def create_app(test_config=None):
    #creating instance of application in function so global
    #variable isnt used
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        #when not testing load config if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        #when testing load test config if passed in
        app.config.from_mapping(test_config)
    
    #ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(alarm.bp)
    app.add_url_rule("/", endpoint="get_input")

    with open("alarm_time.txt", 'w') as f:
        f.write("Starting up")
    
    t = threading.Thread(target=server.run, daemon=True)
    t.start()
    
    return app