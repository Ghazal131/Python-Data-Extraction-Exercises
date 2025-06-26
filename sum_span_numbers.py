# This Python program retrieves an HTML page from a given URL,
# parses the page using BeautifulSoup to extract all numbers inside <span> tags,
# then sums those numbers and counts how many numbers were found.

import urllib.request, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


# The URL to process
url = 'https://py4e-data.dr-chuck.net/comments_2231606.html'


# Open and parse the HTML
html = urllib.request.urlopen(url, context=ssl_context).read()
soup = BeautifulSoup(html, 'html.parser')


# Find all <span> tags
span_tags = soup('span')


# Initialize counters
total_sum = 0
number_count = 0


# Loop through each <span> tag and sum the numbers
for tag in span_tags:
    number = int(tag.text)
    total_sum += number
    number_count += 1


# Print results
print('Count:', number_count)    # Count: 50
print('Sum:', total_sum)    # Sum: 2260
