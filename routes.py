from flask import *
import logging
# from classes import *
from utilities.test_content import *

DEBUG = True #FIXME Please remove

# Assigning app to the Flask namespace and redefining template folder
app = Flask(__name__, template_folder='static/pages')

#Passing test data as arguments to Home
@app.route('/')
def home(company = test_company, user = test_user_logged_out, buttonlabel = "Login"):
    """Routing for site homepage"""
    return render_template('index.html', company = test_company, user = test_user_logged_out, buttonlabel = "Login")


#Passing test data as arguments to dashboard
@app.route('/dashboard')
def dashboard(company = test_company, user = test_user_logged_in, ticket = test_ticket, buttonlabel = "Login"):
    """Routing for site homepage"""
    return render_template('dashboard.html', company = test_company, user = test_user_logged_in, ticket = test_ticket, buttonlabel = "Login")

#Passing test data as arguments to companies_search
@app.route('/companies')
def companies_search(company = test_company, user = test_user_logged_in, buttonlabel = "Login"):
    """Routing for site homepage"""
    return render_template('companies-search.html', company = test_company, user = test_user_logged_in, buttonlabel = "Login")

#Passing test data as arguments to customers_search
@app.route('/customers')
def customer_search(company = test_company, user = test_user_logged_in):
    """Routing for site homepage"""
    return render_template('customers-search.html', company = test_company, user = test_user_logged_in, buttonlabel = "{} {}".format(test_user_logged_in.first_name, test_user_logged_in.last_name))


#Passing test data as arguments to settings
@app.route('/settings')
def settings(company = test_company, user = test_user_logged_in):
    """Routing for site homepage"""
    return render_template('settings.html', company = test_company, user = test_user_logged_in, buttonlabel = "{} {}".format(test_user_logged_in.first_name, test_user_logged_in.last_name))


#Passing test data as arguments to ticket_search
@app.route('/tickets')
def tickets_search(company = test_company, user = test_user_logged_in, buttonlabel = "Login"):
    """Routing for site homepage"""
    return render_template('tickets-search.html', company = test_company, user = test_user_logged_in, buttonlabel = "Login")

#Passing test data as arguments to companies_search
@app.route('/search')
def search(company = test_company, user = test_user_logged_in, buttonlabel = "Login"):
    """Routing for site homepage"""
    return render_template('search.html', company = test_company, user = test_user_logged_in, buttonlabel = "Login")


@app.route('/robots.txt')
def robots_txt():
    return app.send_static_file('robots.txt')

#Removing SW pages for now
# @app.route('/offline.html')
# def offline():
#     return app.send_static_file('offline.html')


# @app.route('/service-worker.js')
# def sw():
#     return app.send_static_file('service-worker.js')

if __name__ == '__main__':
    app.static_folder = 'static'
    app.debug = DEBUG
    app.run(host='0.0.0.0')