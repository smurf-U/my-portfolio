from os import path

from flask import Flask, render_template, send_from_directory
from flask_assets import Environment
from flask_sqlalchemy import SQLAlchemy
from .assets import assets_bundles


class MyPortfolioApp(Flask):

    def send_static_file(self, filename):
        for blueprint_name, blueprint in self.blueprints.items():
            filepath = path.join(blueprint.static_folder, filename)
            if path.exists(filepath):
                return send_from_directory(blueprint.static_folder, filename)
        return super(MyPortfolioApp, self).send_static_file(filename)


app = MyPortfolioApp(__name__, static_folder="static", template_folder="templates")

# Configurations
app.config.from_object('config')
# app.config.from_pyfile('config.py')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# from app.auth.controllers import auth
from app.website.controllers import website
#
# # Register blueprint(s)
# app.register_blueprint(auth)
app.register_blueprint(website)

# Build the database:
# This will create the database file using SQLAlchemy
# db.create_all()

# Assets Registration
# from app.website import assets

assets = Environment(app)
assets.register(assets_bundles)
