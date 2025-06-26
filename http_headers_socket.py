# This Python program establishes a raw socket connection to http://data.pr4e.org/intro-short.txt,
# sends an HTTP GET request, and retrieves the HTTP response—including headers and body—
# using low-level socket programming.

import socket  # Import the socket module to enable low-level network communication

# Create a new socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the web server at data.pr4e.org on port 80 (HTTP)
mysock.connect(('data.pr4e.org', 80))

# Prepare the HTTP GET request.
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

# Send the encoded HTTP request to the server
mysock.send(cmd)

# Loop to receive data from the server in chunks of 512 bytes
while True:
    data = mysock.recv(512)  # Read up to 512 bytes from the socket
    if (len(data) < 1):      # If no more data is received, break out of the loop
        break
    print(data.decode())     # Decode the bytes into a string and print it to the console

# Close the socket connection after all data has been received
mysock.close()
