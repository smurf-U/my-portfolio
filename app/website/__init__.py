# from import app
from flask_assets import Environment

from app import app
from .assets import *

assets = Environment(app)

# css = Bundle('css/bootstrap.min.css')
assets.register('assets_frontend_css', assets_bundles)
