# -*- coding: utf-8 -*-
# AI Agent Test File
# This program takes user information and sends a welcome message

import re
import logging
import sys
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from getpass import getpass

# UTF-8 support for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AIAgent:
    """AI Agent Class"""

    def __init__(self):
        # Store user information
        self.user_data = {}

        # Email configuration
        self.smtp_server = None
        self.smtp_port = None
        self.sender_email = None
        self.sender_password = None

        logger.info("AI Agent initialized")

    def validate_email(self, email: str) -> bool:
        """Validate email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_mobile(self, mobile: str) -> bool:
        """Validate mobile number"""
        # Between 10 to 13 digits
        return re.match(r'^\d{10,13}$', mobile.replace(' ', '').replace('-', '')) is not None

    def setup_email_config(self):
        """Setup email configuration"""
        try:
            print("\n" + "="*60)
            print("*** Email Configuration ***")
            print("="*60)
            print("\n[i] For Gmail: smtp.gmail.com (Port: 587)")
            print("[i] https://support.google.com/accounts/answer/185833 (App Password)")

            self.smtp_server = input("\nSMTP Server (default: smtp.gmail.com): ").strip() or "smtp.gmail.com"
            self.smtp_port = int(input("SMTP Port (default: 587): ").strip() or "587")
            self.sender_email = input("Sender Email: ").strip()
            self.sender_password = getpass("Email Password (App Password for Gmail): ")

            logger.info(f"Email configuration setup with server: {self.smtp_server}")
            print("[OK] Email configuration ready!\n")

        except Exception as e:
            logger.error(f"Error setting up email configuration: {e}")
            print(f"[X] Error in email setup: {e}")
            raise

    def send_email(self, receiver_email: str, subject: str, body: str) -> bool:
        """Send email"""
        try:
            if not self.smtp_server or not self.sender_email:
                logger.warning("Email configuration not setup, skipping email send")
                return False

            # Create email message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = receiver_email

            # HTML part
            html_body = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="background-color: #f0f0f0; padding: 20px; border-radius: 5px;">
                        <h2 style="color: #2c3e50;">Welcome Message</h2>
                        <hr style="border: none; border-top: 2px solid #3498db;">
                        {body.replace(chr(10), '<br>')}
                        <hr style="border: none; border-top: 2px solid #3498db;">
                        <p style="color: #7f8c8d; font-size: 12px;">
                            This is an automated message.
                        </p>
                    </div>
                </body>
            </html>
            """

            part = MIMEText(html_body, "html")
            message.attach(part)

            # Connect to SMTP server
            print(f"[*] Sending email to {receiver_email}...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(message)
            server.quit()

            logger.info(f"Email sent successfully to {receiver_email}")
            print(f"[OK] Email sent successfully!")
            return True

        except smtplib.SMTPAuthenticationError:
            logger.error(f"SMTP Authentication failed for {self.sender_email}")
            print("[X] [ERROR] Email authentication failed. Check credentials.")
            return False

        except smtplib.SMTPException as se:
            logger.error(f"SMTP error while sending email: {se}")
            print(f"[X] [ERROR] SMTP Error: {se}")
            return False

        except Exception as e:
            logger.error(f"Error sending email: {e}")
            print(f"[X] [ERROR] Error sending email: {e}")
            return False

    def get_user_name(self) -> str:
        """Get user name"""
        while True:
            try:
                name = input("Please enter your name: ").strip()

                if not name:
                    print("[X] Name cannot be empty")
                    logger.warning("Empty name entered")
                    continue

                if len(name) < 2:
                    print("[X] Name must be at least 2 characters")
                    logger.warning(f"Name too short: {name}")
                    continue

                logger.info(f"Valid name entered: {name}")
                return name

            except Exception as e:
                print(f"[X] Error: {e}")
                logger.error(f"Error getting name: {e}")

    def get_user_address(self) -> str:
        """Get user address"""
        while True:
            try:
                address = input("Please enter your address: ").strip()

                if not address:
                    print("[X] Address cannot be empty")
                    logger.warning("Empty address entered")
                    continue

                if len(address) < 5:
                    print("[X] Address should be more detailed")
                    logger.warning(f"Address too short: {address}")
                    continue

                logger.info(f"Valid address entered: {address}")
                return address

            except Exception as e:
                print(f"[X] Error: {e}")
                logger.error(f"Error getting address: {e}")

    def get_user_mobile(self) -> str:
        """Get user mobile number"""
        while True:
            try:
                mobile = input("Please enter your mobile number: ").strip()

                if not mobile:
                    print("[X] Mobile number cannot be empty")
                    logger.warning("Empty mobile entered")
                    continue

                if not self.validate_mobile(mobile):
                    print("[X] Please enter a valid mobile number (10-13 digits)")
                    logger.warning(f"Invalid mobile format: {mobile}")
                    continue

                logger.info(f"Valid mobile entered: {mobile}")
                return mobile

            except Exception as e:
                print(f"[X] Error: {e}")
                logger.error(f"Error getting mobile: {e}")

    def get_user_email(self) -> str:
        """Get user email"""
        while True:
            try:
                email = input("Please enter your email: ").strip()

                if not email:
                    print("[X] Email cannot be empty")
                    logger.warning("Empty email entered")
                    continue

                if not self.validate_email(email):
                    print("[X] Please enter a valid email")
                    logger.warning(f"Invalid email format: {email}")
                    continue

                logger.info(f"Valid email entered: {email}")
                return email

            except Exception as e:
                print(f"[X] Error: {e}")
                logger.error(f"Error getting email: {e}")

    def collect_user_info(self):
        """Collect all user information"""
        try:
            print("\n" + "="*60)
            print("** Welcome to AI Agent **")
            print("="*60 + "\n")

            self.user_data['name'] = self.get_user_name()
            self.user_data['address'] = self.get_user_address()
            self.user_data['mobile'] = self.get_user_mobile()
            self.user_data['email'] = self.get_user_email()

            logger.info(f"All user data collected successfully")

        except Exception as e:
            print(f"[ERROR] Error collecting user info: {e}")
            logger.error(f"Error collecting user info: {e}")
            raise

    def send_welcome_message(self):
        """Send welcome message"""
        try:
            if not self.user_data:
                print("[X] Please collect user information first")
                logger.warning("No user data available for welcome message")
                return

            name = self.user_data.get('name', 'User')

            # Welcome message
            welcome_msg = f"""
========================================================
           ** WELCOME MESSAGE **
========================================================

Hello!

I am an AI Agent.

Welcome, {name}!

Your Information:
   * Name: {self.user_data['name']}
   * Address: {self.user_data['address']}
   * Mobile: {self.user_data['mobile']}
   * Email: {self.user_data['email']}

*** Welcome to the AI Era! ***

I am here to help you.

Let's move towards the future!

========================================================
"""

            print(welcome_msg)
            logger.info(f"Welcome message displayed for {name}")

            # Send email
            if self.sender_email:
                receiver_email = self.user_data.get('email')
                email_subject = f"Welcome from AI Agent - {name}"
                self.send_email(receiver_email, email_subject, welcome_msg)
            else:
                logger.warning("Email not configured, skipping email send")

            logger.info(f"Welcome message completed for {name}")

        except Exception as e:
            print(f"[X] Error sending welcome message: {e}")
            logger.error(f"Error sending welcome message: {e}")


def main():
    """Main program"""
    try:
        # एआई एजेंट को इनिशियलाइज करो / Initialize AI Agent
        agent = AIAgent()

        # ईमेल कॉन्फ़िगरेशन सेटअप करो / Setup email configuration
        setup_email = input("\nक्या आप ईमेल कॉन्फ़िगरेशन करना चाहते हैं? (y/n, डिफ़ॉल्ट: y) / Do you want to setup email configuration? (y/n, default: y): ").strip().lower()

        if setup_email != 'n':
            try:
                agent.setup_email_config()
            except Exception as email_setup_error:
                logger.warning(f"Email setup skipped: {email_setup_error}")
                print("[!] Skipping email configuration...")

        # उपयोगकर्ता जानकारी एकत्र करो / Collect user information
        agent.collect_user_info()

        # स्वागत संदेश भेजो / Send welcome message
        agent.send_welcome_message()

        logger.info("Program completed successfully")

    except KeyboardInterrupt:
        print("\n\n[X] प्रोग्राम उपयोगकर्ता द्वारा बंद किया गया / Program interrupted by user")
        logger.info("Program interrupted by user")

    except Exception as e:
        print(f"[X] Fatal error in program: {e}")
        logger.error(f"Fatal error: {e}")


if __name__ == '__main__':
    main()
