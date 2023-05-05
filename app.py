import requests

# Set up the payload with the new password
payload = {
    'passwordOld': 'CURRENT_PASSWORD',
    'passwordNew': '2694adk63AjD',
    'passwordNewConfirm': '2694adk63AjD'
}

# Send the POST request to the password reset endpoint
response = requests.post('https://www.roblox.com/account/settings/security/password', data=payload)

# Check the response status code to see if the password was successfully changed
if response.status_code == 200:
    print("Password successfully changed to 2694adk63AjD!")
else:
    print("Error: Password not changed. Response code:", response.status_code)
