from flask import Flask, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource


from data import db_session, news_api, jobs_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/blogs.sqlite")
    app.register_blueprint(news_api.blueprint)
    app.register_blueprint(jobs_api.blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)
    app.run()


if __name__ == '__main__':
    main()
