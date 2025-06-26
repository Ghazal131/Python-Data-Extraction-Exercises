# Python Data Extraction Exercises

This repository contains seven Python scripts written to practice working with:
- Text parsing
- Regular expressions
- HTTP requests
- HTML and XML/JSON parsing
- API usage with BeautifulSoup and urllib

These exercises are based on assignments from the **Python for Everybody** course by Dr. Charles Severance (Dr. Chuck).



## 🔍 Overview of Each Script

### 1. `regex_number_sum.py`
Reads a local `.txt` file and uses regular expressions to extract all numbers, then computes their sum.

- ✅ Requires file: `regex_sum_2231604.txt` (place in the same folder as the script)



### 2. `http_headers_socket.py`
Uses raw sockets to send an HTTP GET request and prints the full HTTP response (headers + body) from the specified URL.



### 3. `sum_span_numbers.py`
Fetches HTML from a URL using BeautifulSoup, finds all numbers inside `<span>` tags, then calculates and prints their total and count.



### 4. `follow_link_position.py`
Starts from a specified URL and follows the link at a specified position for a number of times. After the final retrieval, it prints the last name in the sequence (from the URL).



### 5. `sum_xml_counts.py`
Downloads XML data from a given URL, extracts all `<count>` values inside `<comment>` tags, then prints how many were found and their total sum.



### 6. `sum_json_counts.py`
Fetches JSON data from a URL, extracts all `count` values inside the `comments` list, and prints the count and the sum.



### 7. `opengeo_plus_code.py`
Prompts the user for a location, encodes the query, sends it to the OpenGeo API, and extracts the first `plus_code` from the JSON response.



## 🚀 How to Run

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run any script using:
python script_name.py




## 📦 Dependencies

These scripts use standard Python libraries:

* `urllib`
* `re`
* `json`
* `xml.etree.ElementTree`
* `socket`
* `ssl`
* `bs4` *(BeautifulSoup)*

If you don’t have BeautifulSoup installed, install it with:
pip install beautifulsoup4




## 📚 Credits

These exercises are based on assignments from the [Python for Everybody](https://www.py4e.com/) course by Dr. Chuck Severance.
