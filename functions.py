#function  to generate random numbers
# 6 random numbers 124978

# def number_generate():
#     import random
#     #import string 
   
#     print(random.randint(100000,999999))






#lowercase letters
# import random
# import string
# def lowercase():
#     print("".join(random.choice(string.ascii_lowercase for x in range(6)))  )

# lowercase()
    
# funtion to check password validity
#lower case
#uppercase
# a digit
#special character

import re

def checkpassword(password):
    # Check for lowercase letters
    haslowercase = re.search(r'[a-z]', password)
    # Check for uppercase letters
    hasuppercase = re.search(r'[A-Z]', password)
    # Check for digits
    hasdigit = re.search(r'\d', password)
    # Check for special characters
    hasspecial = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)  # Added more special characters

    if len(password) < 8:
        return "Your password is too short"
    elif not haslowercase:
        return "Password must contain at least one lowercase letter"
    elif not hasuppercase:
        return "Password must contain at least one uppercase letter"
    elif not hasdigit:
        return "Password must contain at least one digit"
    elif not hasspecial:
        return "Password must contain at least one special character"
    else:
        return True

# Test the function
checkpassword("123abc@eeA")       # Test with a password that fails multiple criteria
# checkpassword("Password1!")       # Test with a strong password
# checkpassword("short")            # Test with a too short password
# checkpassword("NOdigits!")        # Test with missing digits
# checkpassword("nodigits")         # Test with missing digits and special characters


#check phone validity format
#0712345678
#+25412345678
    
import re

def checkphone(phone):
    # Corrected regular expression pattern
    pattern = r"^(07\d{8}|\+254\d{9})$"
    if re.match(pattern, phone):
        print("Valid phone")
        return True
    else:
        print("Not valid")
        return False

# Test the function
# checkphone("712345678")
checkphone("+254712345678")
# checkphone("1234567890")  # Example of an invalid number
#how to hash passwords 
import bcrypt
def hash_password(password):
    # password = b"my secret password"
    # hash_password = bcrypt.hashpw(password,bcrypt.gensalt())
    # print(f("hashed password:{hashed password}"))
    bytes = password.encode("utf-8")
    # print(bytes)
    salt = bcrypt.gensalt()
    # print(salt)
    hash = bcrypt.hashpw(bytes, salt)
    # print(hash)
    return hash.decode()

# hash_password("Olioks@2003")

# hash verify
def hash_verify(originalpassword, hashedpassword):
    bytes = originalpassword.encode("utf-8")
    result = bcrypt.checkpw(bytes, hashedpassword.encode())
    # print(result)
    return result

# hash_verify
# ("Olioks@2003","$2b$12$Fjn7wMOXqY1Ph3suGD5nhOLBqmZjE8Q.NpObKCipMoZkEusExKgnu")
  
#sending sms




import africastalking

africastalking.initialize(

 username="joe2022",

 api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"

 # justpaste.it/1nua8 

)

sms = africastalking.SMS

def send_sms(phone, message):
    recipients = [phone]
    sender = "ARICASTALKING"
    response = sms.send(message,recipients )
    print (response)
# send_sms("+254769191897","Thank you for regestration")
# Encryption 
from cryptography.fernet import Fernet
def gen_key():
    key = Fernet.generate_key()
    # print(key)
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# gen_key()
        
# load key
def load_key():
    return open("key.key","rb").read()

# Encription 
def encrypt(data):
    key = load_key()
    # print(key)
    f = Fernet(key)
    # print(f)
    encrypted_data = f.encrypt(data.encode())
    print (encrypted_data.decode)
    return encrypted_data.decode()

# encrypt("this is my data")

# decrypt data
def decrypt (encrypted_data):
    key = load_key()
    f =Fernet(key)

    decrypt_data = f.decrypt(encrypted_data.encode())
    print(decrypt_data)
    return decrypt_data.decode()

# decrypt ("gAAAAABm4tKphlKMDbISH57rGSt3ZylfIaWx7HkAq1_vGOlvbvnbRosCD4jltTcDzhNH4LArAizsmzyRpuv3JYQ9-_UO61XL5w==")



import requests
import base64
import datetime
from requests.auth import HTTPBasicAuth

def mpesa_payment(amount, phone, invoice_no):
    # GENERATING THE ACCESS TOKEN
    consumer_key = "oAN7tFvWXa4qJ6XWAqcjG3RZoMGsSOXA"
    consumer_secret = "J2TFUVbsnM5CEvvr"

    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    if r.status_code != 200:
        print(f"Failed to get access token: {r.status_code} - {r.text}")
        return
    
    data = r.json()
    access_token = "Bearer " + data['access_token']
    print("Access Token:", access_token)

    # GETTING THE PASSWORD
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    business_short_code = "174379"
    data = business_short_code + passkey + timestamp
    encoded = base64.b64encode(data.encode())
    password = encoded.decode('utf-8')
    print("Password:", password)

    # BODY OR PAYLOAD
    payload = {
        "BusinessShortCode": business_short_code,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone,
        "PartyB": business_short_code,
        "PhoneNumber": phone,
        "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
        "AccountReference": "Lab Account",
        "TransactionDesc": "account"
    }

    # POPULATING THE HTTP HEADER
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

    response = requests.post(url, json=payload, headers=headers)

    # Debugging the response
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code != 200:
        print(f"Error during M-Pesa payment: {response.status_code} - {response.text}")
        return

    # Try to parse the JSON response
    try:
        json_response = response.json()
        print("JSON Response:", json_response)
        return json_response
    except ValueError as e:
        print("JSON Decode Error:", str(e))
        print("Raw Response:", response.text)

# Example usage:
# mpesa_payment(1, "254700000000", "invo