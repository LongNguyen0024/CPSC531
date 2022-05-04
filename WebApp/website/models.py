from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(db.Model, UserMixin):
    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    usernname = db.Column(db.String(100))

class ArtworkOrder(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100))
    customer_phone = db.Column(db.Integer)
    order_date = db.Column(db.DateTime(timezone=True), default=func.now())
    order_price = db.Column(db.Integer)
    apparel = db.Column(db.String(100))
    base_color = db.Column(db.String(100))
    max_color = db.Column(db.String(100))
    art_location = db.Column(db.String(100))
    description = db.Column(db.String(100))
    cost = db.Column(db.Integer)
    employee = db.Column(db.String(100))
    date_complete = db.Column(db.DateTime(timezone=True), default=func.now())


# class PrintOrder(db.Model):
#     customer_id
#     customer_name
#     customer_phone

#     order_date
#     due_date
#     print_date
#     date_delivered

#     setup_charge
#     deposit 
#     discount
#     total_cost

#     s_number
#     s_charge
#     l_number
#     l_charge

   


class CostAnalysis(db.Model):
    Project_id = db.Column(db.Integer, primary_key=True)


class EmployeeManagement(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.Integer)
    employee_phone = db.Column(db.Integer)
    employee_jobtype = db.Column(db.Integer)
    project = db.Column(db.String(100))
    task = db.Column(db.String(100))
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)



