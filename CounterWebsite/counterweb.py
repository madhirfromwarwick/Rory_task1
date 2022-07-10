# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 13:54:37 2022

@author: coolm
"""

from flask import Flask
from flask_restful import Api, Resource

#create Flask app and api
app = Flask(__name__)
api = Api(app)

#create database of count
global rick_counts 
rick_counts = {"rory": {"num_rr": 1000},
               "mahir": {"num_rr": 0}}

#make a resource for count
class Counter(Resource):
    def get(self,name):
        if name == "rory":
            # global rick_counts
            rick_counts["rory"]["num_rr"] = rick_counts["rory"]["num_rr"] + 1
        elif name == "mahir":
            # global rick_counts
            rick_counts["mahir"]["num_rr"] = rick_counts["mahir"]["num_rr"] - 1
        return rick_counts[name]

#add resource to api
api.add_resource(Counter, "/rickrollcounter/<string:name>")

#run app
if __name__ == "__main__":
    app.run()