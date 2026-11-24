"""

File: search.py
Responsibility: Relocator District Search Functionality
Team Member Assigned: abdul (Backend) & Member 1 (Frontend UI)

Description:
    Handles district-based search requests submitted by relocating users.
    Queries MongoDB using case-insensitive regular expressions and passes 
    results back to search.html without JavaScript.

"""


from flask import Flask,render_template,request
from database import properties_collection

def init_search_route(app):
    @app.route('/search',methods=['GET'])
    def search():
        district = request.args.get('district','')
        state = request.args.get('state','')

        results = []

        if district and state:
            query = {
                "district":district,
                "state":state
            }

            results = list(properties_collection.find(query))

        return render_template('search.html',properties=results ,district = district, state=state)