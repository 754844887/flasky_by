from flask import Flask, render_template, session
from flask_session import Session
from exts import db
import config
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    db.init_app(app)
    sess = Session()
    sess.init_app(app)
    return app


app = create_app()

# @app.route('/')
# def index():
#     session['key'] = 'abc'
#     session.permanent = True
#     # app.permanent_session_lifetime = timedelta(minutes=10)
#     return render_template('index.html')



