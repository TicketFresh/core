from flask import *
from functools import wraps
import logging
# from classes import *
from test_content import *

DEBUG = True #FIXME Please remove

# Assigning app to the Flask namespace and redefining template folder
app = Flask(__name__, template_folder='static/pages')

app.secret_key = '>wwx7M_9!>IU6z!ME[D"HxcLN#<)v('

def login_required(test):
    """Used to force users to login on specific pages"""
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You must login first to access this page')
            return redirect(url_for('login'))
    return wrap

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


@app.route('/logout')
def logout():
    """Function to reset user session 'logs user out'"""
    """
    session.pop('logged_in', None)
    session['username'] = ""
    flash("You've been logged out")
    return redirect(url_for('login'))
    """
    #This is here for reference to a previous implementation
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Defines how users login; uses HTTP get and post requests"""

    """
    error = None
    if request.method == 'POST':
        # TODO: Tie this to an admin database so that users and passwords can be managed properly

        # NOTE: Change the 'admin' credentials here; this is user login validation
        if request.form['username'].lower().rstrip().lstrip() == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            session['username'] = "admin"
            flash("Success! Logged In")
            return redirect(url_for('userediting'))
        if request.form['username'].lower().rstrip().lstrip() == 'employee' and request.form['password'] == 'employee':
            session['logged_in'] = True
            session['username'] = "employee"
            flash("Success! Logged In")
            return redirect(url_for('userediting'))
        #if login succeeds
        else:
            error = 'Invalid credentials. Please try again'

    #first time viewing or refresh on failed login
    return render_template('login.html', error = error)
    """
    #This is here for reference to a previous implementation
    pass

@app.route('/offline.html')
def offline():
    return app.send_static_file('offline.html')


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

if __name__ == '__main__':
    app.static_folder = 'static'
    app.debug = DEBUG
    app.run(host='0.0.0.0')