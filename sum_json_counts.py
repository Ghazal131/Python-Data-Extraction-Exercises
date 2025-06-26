# This Python program prompts the user for a URL pointing to JSON data,
# retrieves the JSON, parses it to extract all 'count' values from the comments list,
# then calculates and displays the total number of comment entries and the sum of all counts.

import urllib.request
import json

# URL for reference:
# http://py4e-data.dr-chuck.net/comments_2231609.json

# Prompt for the URL
url = input("Enter location: ")
print("Retrieving", url)


# Open the URL and read the data
response = urllib.request.urlopen(url)
data = response.read().decode()
print("Retrieved", len(data), "characters")


# Parse the JSON data
info = json.loads(data)


# Extract the list of comments
comments = info['comments']


# Count the number of items and calculate the total
count = len(comments)
total = sum(item['count'] for item in comments)


# Print the results
print("Count:", count)
print("Sum:", total)


# Output of code:-
# Retrieving http://py4e-data.dr-chuck.net/comments_2231609.json
# Retrieved 2720 characters
# Count: 50
# Sum: 2381