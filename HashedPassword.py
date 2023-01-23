import bcrypt
from twilio.rest import Client
import random

# Twilio account SID and Auth token
account_sid = '<your_twilio_account_sid>'
auth_token = '<your_twilio_auth_token>'

# Twilio phone number to send the SMS from
from_phone_number = '<your_twilio_phone_number>'

def send_otp(phone_number: str, otp: str):
    """
    Send an OTP via SMS to the given phone number
    """
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=from_phone_number,
        to=phone_number
    )
    print(f'OTP sent to {phone_number}')

def verify_otp(otp_input: str, otp: str) -> bool:
    """
    Verify the OTP entered by the user
    """
    return otp_input == otp

def hash_password(password: str):
    """
    Hashes a plaintext password using the bcrypt algorithm
    """
    # generate a random salt with a cost factor of 12
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str, phone_number:str) -> bool:
    """
    Verifies a plaintext password against a hashed password, and sends an OTP via SMS
    """
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        otp = str(random.randint(100000, 999999))
        send_otp(phone_number, otp)
        otp_input = input("Enter the OTP: ")
        if verify_otp(otp_input, otp):
            return True
    return False

def validate_password(password: str):
    """
    Validate a plaintext password by applying some rules
    """
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one digit")

