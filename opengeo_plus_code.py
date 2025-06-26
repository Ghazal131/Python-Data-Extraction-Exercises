# This Python program prompts the user for a location name,
# sends a GET request to the OpenGeo API with the encoded location,
# retrieves JSON data, and extracts the first plus_code from the response.

import urllib.request
import urllib.parse
import json


# API endpoint
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"


# Sample and Graded Input Addresses:
# Sample Input: South Federal University (Expected Plus Code: 6FV8QPRJ+VQ)
# Graded Input: Moscow State University (Expected Plus Code: 9G7VPG2J+WP)

# Prompt user
address = input("Enter location: ")


# Encode query string
params = {'q': address}
url = serviceurl + urllib.parse.urlencode(params)

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")


# Parse the JSON
js = json.loads(data)


# Extract and print plus_code
try:
    plus_code = js["features"][0]["properties"]["plus_code"]
    print("Plus code", plus_code)
except (KeyError, IndexError):
    print("Plus code not found.")
