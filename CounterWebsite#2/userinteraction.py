# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:26:34 2022

@author: coolm
"""

import requests

BASE = "http://localhost:5000/"

# response = requests.get(BASE + "Counter/rory")
response = requests.post(BASE + "Increment/rory")

print(response.json())