from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for, make_response, send_from_directory, \
    safe_join, send_file
from passlib.handlers.sha2_crypt import sha256_crypt
# from app.auth.forms import LoginForm
# from app.auth.models import User

from app import app

website = Blueprint('website', __name__,
                    template_folder='templates',
                    static_folder='static',
                    # static_url_path='/website/static')
                    static_url_path='%s/website' % app.static_url_path)


# Set the route and accepted methods
@website.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@website.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@website.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")


# @website.route('/blog', methods=['GET', 'POST'])
# def blog():
#     return render_template("about.html")


@website.route('/works', methods=['GET', 'POST'])
def works():
    return render_template("works.html")


@website.route('/resume', methods=['GET', 'POST'])
def resume():
    # filename = url_for('static', filename='resume.pdf')
    # fp = open(filename, 'rb')
    #
    # response = make_response(fp.read())
    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = \
    #     'inline; filename=%s.pdf' % 'cv_kaushal_prajapati'
    # return response
    return render_template("about.html")
