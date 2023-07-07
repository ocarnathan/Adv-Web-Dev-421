import requests
import json
import re

url ="http://michaelgathara.com/api/python-challenge"

# Send a GET request to retrieve the challenge
response = requests.get(url)

#Extract the challenges from the response
challenges = response.json()

print("Name: Obie Carnathan\nBlazer ID: aikia16")
for equation in challenges:
    print("\nProblem " + str(equation['id'])+ ": " + equation['problem'][:-1] + " = " + str(eval(equation['problem'][:-1])))