"""
================================================================================
File: database.py
Responsibility: MongoDB Database Connection & Collection Exports
Team Member Assigned: abdul (Backend Lead)
--------------------------------------------------------------------------------
Description:
    Connects to the local MongoDB instance using PyMongo and exports
    handles for the 'users' and 'properties' collections to be used across
    the application routes.
================================================================================
"""


from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['relocease_db']

landlord_collection = db['landlords']

properties_collection = db['properties']