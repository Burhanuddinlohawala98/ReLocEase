"""

File: main.py
Responsibility: Central Application Entry Point
Team Member Assigned: Member 2 (Backend) / Member 3 (Integration)

Description:
    This file initializes the Flask framework application, loads the standard
    configurations (such as session secret keys), registers all functional
    route modules, and runs the application server.

"""

from flask import Flask,render_template,url_for
from search import init_search_route
from home import init_home_route
from owners import init_login_route,init_signup_route

app = Flask(__name__)
app.secret_key = 'team_relocease'

@app.route("/")
def index():
    return render_template("index.html")

init_search_route(app)
init_home_route(app)
init_signup_route(app)
init_login_route(app)

if __name__ == "__main__":
    print("Starting the app")
    app.run(debug=True)