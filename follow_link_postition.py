# This Python program starts from a given URL and repeatedly follows the link found at a specified position
# on each page for a set number of times. After following the links, it reports the final URL retrieved,
# which contains a name embedded in it (Stewart).

import urllib.request, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE


# User inputs
# Start URL: http://py4e-data.dr-chuck.net/known_by_Amber.html
# Repeat count: 7
# Position to find link: 18

start_url = input('Enter URL: ')
repeat_count = int(input('Enter count: '))
link_postition = int(input('Enter position: '))

print('Retrieving:', start_url)


# Follow links repeatedly
for step in range(repeat_count):
    html = urllib.request.urlopen(start_url, context=ssl_context).read()
    soup = BeautifulSoup(html, 'html.parser')

    
    # Find all <a> tags
    anchor_tags = soup('a')
    current_position = 0

    
    # Loop to reach the desired link
    for anchor in anchor_tags:
        current_position += 1
        if current_position == link_postition:
            next_url = anchor.get('href', None)
            print('Retrieving:', next_url)
            start_url = next_url
            break
