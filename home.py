from flask import Flask,render_template,request,session,redirect,url_for
from database import properties_collection

def init_home_route(app):
    @app.route('/add_home',methods=['POST','GET'])
    def home():
        if 'user_id' not in session:
            return redirect(url_for('login'))

        if request.method == 'POST':
            district = request.form.get('district')
            state = request.form.get('state')
            address = request.form.get('address')
            rent = request.form.get("rent")
            house_type = request.form.get('house_type')
            phone = request.form.get('phone')
            contact_email = request.form.get('email')

            if district and state and address and rent and house_type and phone and contact_email:
                query = {
                    "owner_id":session['user_id'],
                    "district":district,
                    "state":state,
                    "address":address,
                    "rent":rent,
                    "house_type":house_type,
                    "phone":phone,
                    "contact_email":contact_email
                }
        

                properties_collection.insert_one(query)
                return f"""
                    <script>
                        alert("Home added successfully!");
                        window.location.href = "{url_for('dashboard')}";
                    </script>
                """
                
        
            return 'Please fill all the fields.'

        return render_template('home.html')