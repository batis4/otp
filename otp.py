import random
import smtplib

# Generate a 6-digit OTP as it's required from the task synsintership
otp = random.randint(100000, 999999)

# Store the OTP in a variable as a instruction
otp_message = f"Your OTP is {otp} please do not share it with anyone else"

    # Write a function to send emails ( by Ba Tis )
def send_email(to_email, message):
    # Replace the placeholders with your email credentials
    from_email = "otpvertificationassignment1@gmail.com"
    app_email_password = "abot hxhx cwft kdni"

    # Create the email message
    email_message = f"Subject: OTP Verification\n\n{message}"

    # Connect to the email server and send the message
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(from_email, app_email_password)
        smtp.sendmail(from_email, to_email, email_message)

# Send the OTP to the user's email
user_email = input("Enter your email address: ")
send_email(user_email, otp_message)

# Request the OTP from the user and verify it
user_otp = input("Enter the OTP you received by your email: ")
if user_otp == str(otp):
    print("OTP verification successful, Congratulations !! ")
else:
    print("Invalid OTP. Please enter a correct one! ")