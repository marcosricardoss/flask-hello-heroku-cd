from flask import Flask

def create_app(test_config: dict = {}):
    app = Flask(__name__)
    app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return 'Hello, Heroku'

    return app