# This Python program downloads an XML file from a user-provided URL,
# parses it to extract all <count> elements inside <comment> tags,
# sums their integer values, and prints the count of those elements and their total sum.

import urllib.request
import xml.etree.ElementTree as ET


# URL for reference:
# http://py4e-data.dr-chuck.net/comments_2231608.xml

# Ask the user to enter the URL
url = input('Enter location: ')
print('Retrieving', url)


# Open the URL and read the XML data
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')


# Parse the XML string into a tree structure
tree = ET.fromstring(data)


# Find all <count> elements anywhere in the XML tree using XPath
counts = tree.findall('.//count')


# Sum all the numbers inside <count> tags
total = 0 
for count in counts:
     total += int(count.text)       # Can also do:  total = sum(int(count.text) for count in counts)


# Output results
print('Count:', len(counts))      # How many <count> tags
print('Sum:', total)       # Total sum of their values


# Output of code:-
# Retrieving http://py4e-data.dr-chuck.net/comments_2231608.xml
# Retrieved 4220 characters
# Count: 50
# Sum: 2311