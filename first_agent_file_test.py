# -*- coding: utf-8 -*-
# एआई एजेंट टेस्ट फाइल / AI Agent Test File
# यह प्रोग्राम उपयोगकर्ता से जानकारी लेता है / This program takes user information
# और एक स्वागत संदेश भेजता है / and sends a welcome message

import re
import logging
import sys
import io
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from getpass import getpass

# Windows पर UTF-8 सपोर्ट के लिए / UTF-8 support for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# लॉगिंग सेटअप / Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AIAgent:
    """एआई एजेंट क्लास / AI Agent Class"""

    def __init__(self):
        # उपयोगकर्ता की जानकारी स्टोर करने के लिए / Store user information
        self.user_data = {}

        # ईमेल कॉन्फ़िगरेशन / Email configuration
        self.smtp_server = None
        self.smtp_port = None
        self.sender_email = None
        self.sender_password = None

        logger.info("AI Agent initialized")

    def validate_email(self, email: str) -> bool:
        """ईमेल को वैलिडेट करो / Validate email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def validate_mobile(self, mobile: str) -> bool:
        """मोबाइल नंबर को वैलिडेट करो / Validate mobile number"""
        # 10 से 13 अंक के बीच / Between 10 to 13 digits
        return re.match(r'^\d{10,13}$', mobile.replace(' ', '').replace('-', '')) is not None

    def setup_email_config(self):
        """ईमेल कॉन्फ़िगरेशन सेटअप करो / Setup email configuration"""
        try:
            print("\n" + "="*60)
            print("*** ईमेल कॉन्फ़िगरेशन / Email Configuration ***")
            print("="*60)
            print("\n[i] Gmail के लिए: smtp.gmail.com (पोर्ट: 587)")
            print("[i] For Gmail: smtp.gmail.com (Port: 587)")
            print("[i] https://support.google.com/accounts/answer/185833 (App Password)")

            self.smtp_server = input("\nSMTP सर्वर / SMTP Server (डिफ़ॉल्ट: smtp.gmail.com): ").strip() or "smtp.gmail.com"
            self.smtp_port = int(input("SMTP पोर्ट / SMTP Port (डिफ़ॉल्ट: 587): ").strip() or "587")
            self.sender_email = input("भेजने वाली ईमेल / Sender Email: ").strip()
            self.sender_password = getpass("ईमेल पासवर्ड / Email Password (App Password for Gmail): ")

            logger.info(f"Email configuration setup with server: {self.smtp_server}")
            print("[OK] ईमेल कॉन्फ़िगरेशन तैयार / Email configuration ready!\n")

        except Exception as e:
            logger.error(f"Error setting up email configuration: {e}")
            print(f"[X] ईमेल कॉन्फ़िगरेशन में त्रुटि / Error in email setup: {e}")
            raise

    def send_email(self, receiver_email: str, subject: str, body: str) -> bool:
        """ईमेल भेजो / Send email"""
        try:
            if not self.smtp_server or not self.sender_email:
                logger.warning("Email configuration not setup, skipping email send")
                return False

            # ईमेल संदेश बनाओ / Create email message
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = receiver_email

            # HTML भाग / HTML part
            html_body = f"""
            <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <div style="background-color: #f0f0f0; padding: 20px; border-radius: 5px;">
                        <h2 style="color: #2c3e50;">स्वागत संदेश / Welcome Message</h2>
                        <hr style="border: none; border-top: 2px solid #3498db;">
                        {body.replace(chr(10), '<br>')}
                        <hr style="border: none; border-top: 2px solid #3498db;">
                        <p style="color: #7f8c8d; font-size: 12px;">
                            यह एक स्वचालित संदेश है। / This is an automated message.
                        </p>
                    </div>
                </body>
            </html>
            """

            part = MIMEText(html_body, "html")
            message.attach(part)

            # SMTP सर्वर से कनेक्ट करो / Connect to SMTP server
            print(f"[*] ईमेल भेज रहे हैं {receiver_email} को... / Sending email to {receiver_email}...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(message)
            server.quit()

            logger.info(f"Email sent successfully to {receiver_email}")
            print(f"[OK] ईमेल सफलतापूर्वक भेजा गया / Email sent successfully!")
            return True

        except smtplib.SMTPAuthenticationError:
            logger.error(f"SMTP Authentication failed for {self.sender_email}")
            print("[X] [ERROR] ईमेल प्रमाणीकरण विफल / Email authentication failed. Check credentials.")
            return False

        except smtplib.SMTPException as se:
            logger.error(f"SMTP error while sending email: {se}")
            print(f"[X] [ERROR] SMTP त्रुटि / SMTP Error: {se}")
            return False

        except Exception as e:
            logger.error(f"Error sending email: {e}")
            print(f"[X] [ERROR] ईमेल भेजने में त्रुटि / Error sending email: {e}")
            return False

    def get_user_name(self) -> str:
        """उपयोगकर्ता का नाम लो / Get user name"""
        while True:
            try:
                name = input("कृपया अपना नाम दर्ज करें / Please enter your name: ").strip()

                if not name:
                    print("[X] नाम खाली नहीं हो सकता / Name cannot be empty")
                    logger.warning("Empty name entered")
                    continue

                if len(name) < 2:
                    print("[X] नाम कम से कम 2 वर्ण का होना चाहिए / Name must be at least 2 characters")
                    logger.warning(f"Name too short: {name}")
                    continue

                logger.info(f"Valid name entered: {name}")
                return name

            except Exception as e:
                print(f"[X] त्रुटि: {e} / Error: {e}")
                logger.error(f"Error getting name: {e}")

    def get_user_address(self) -> str:
        """उपयोगकर्ता का पता लो / Get user address"""
        while True:
            try:
                address = input("कृपया अपना पता दर्ज करें / Please enter your address: ").strip()

                if not address:
                    print("[X] पता खाली नहीं हो सकता / Address cannot be empty")
                    logger.warning("Empty address entered")
                    continue

                if len(address) < 5:
                    print("[X] पता अधिक विस्तृत होना चाहिए / Address should be more detailed")
                    logger.warning(f"Address too short: {address}")
                    continue

                logger.info(f"Valid address entered: {address}")
                return address

            except Exception as e:
                print(f"[X] त्रुटि: {e} / Error: {e}")
                logger.error(f"Error getting address: {e}")

    def get_user_mobile(self) -> str:
        """उपयोगकर्ता का मोबाइल नंबर लो / Get user mobile number"""
        while True:
            try:
                mobile = input("कृपया अपना मोबाइल नंबर दर्ज करें / Please enter your mobile number: ").strip()

                if not mobile:
                    print("[X] मोबाइल नंबर खाली नहीं हो सकता / Mobile number cannot be empty")
                    logger.warning("Empty mobile entered")
                    continue

                if not self.validate_mobile(mobile):
                    print("[X] कृपया एक वैध मोबाइल नंबर दर्ज करें (10-13 अंक) / Please enter a valid mobile number (10-13 digits)")
                    logger.warning(f"Invalid mobile format: {mobile}")
                    continue

                logger.info(f"Valid mobile entered: {mobile}")
                return mobile

            except Exception as e:
                print(f"[X] त्रुटि: {e} / Error: {e}")
                logger.error(f"Error getting mobile: {e}")

    def get_user_email(self) -> str:
        """उपयोगकर्ता का ईमेल लो / Get user email"""
        while True:
            try:
                email = input("कृपया अपना ईमेल दर्ज करें / Please enter your email: ").strip()

                if not email:
                    print("[X] ईमेल खाली नहीं हो सकता / Email cannot be empty")
                    logger.warning("Empty email entered")
                    continue

                if not self.validate_email(email):
                    print("[X] कृपया एक वैध ईमेल दर्ज करें / Please enter a valid email")
                    logger.warning(f"Invalid email format: {email}")
                    continue

                logger.info(f"Valid email entered: {email}")
                return email

            except Exception as e:
                print(f"[X] त्रुटि: {e} / Error: {e}")
                logger.error(f"Error getting email: {e}")

    def collect_user_info(self):
        """सभी उपयोगकर्ता जानकारी एकत्र करो / Collect all user information"""
        try:
            print("\n" + "="*60)
            print("** AI AGENT में आपका स्वागत है / Welcome to AI Agent **")
            print("="*60 + "\n")

            self.user_data['name'] = self.get_user_name()
            self.user_data['address'] = self.get_user_address()
            self.user_data['mobile'] = self.get_user_mobile()
            self.user_data['email'] = self.get_user_email()

            logger.info(f"All user data collected successfully")

        except Exception as e:
            print(f"[ERROR] उपयोगकर्ता जानकारी एकत्र करने में त्रुटि / Error collecting user info: {e}")
            logger.error(f"Error collecting user info: {e}")
            raise

    def send_welcome_message(self):
        """स्वागत संदेश भेजो / Send welcome message"""
        try:
            if not self.user_data:
                print("[X] पहले उपयोगकर्ता जानकारी एकत्र करो / Please collect user information first")
                logger.warning("No user data available for welcome message")
                return

            name = self.user_data.get('name', 'User')

            # स्वागत संदेश / Welcome message
            welcome_msg = f"""
========================================================
           ** स्वागत संदेश / WELCOME MESSAGE **
========================================================

नमस्ते! / Hello!

मैं एआई एजेंट हूँ। / I am an AI Agent.

आपका स्वागत है, {name}!
Welcome, {name}!

आपकी जानकारी / Your Information:
   * नाम / Name: {self.user_data['name']}
   * पता / Address: {self.user_data['address']}
   * मोबाइल / Mobile: {self.user_data['mobile']}
   * ईमेल / Email: {self.user_data['email']}

*** आप एआई युग में आपका स्वागत है! ***
*** Welcome to the AI Era! ***

मैं आपकी सहायता के लिए यहाँ हूँ।
I am here to help you.

आइए भविष्य की ओर चलें! / Let's move towards the future!

========================================================
"""

            print(welcome_msg)
            logger.info(f"Welcome message displayed for {name}")

            # ईमेल भेजो / Send email
            if self.sender_email:
                receiver_email = self.user_data.get('email')
                email_subject = f"एआई एजेंट से स्वागत / Welcome from AI Agent - {name}"
                self.send_email(receiver_email, email_subject, welcome_msg)
            else:
                logger.warning("Email not configured, skipping email send")

            logger.info(f"Welcome message completed for {name}")

        except Exception as e:
            print(f"[X] स्वागत संदेश भेजने में त्रुटि / Error sending welcome message: {e}")
            logger.error(f"Error sending welcome message: {e}")


def main():
    """मुख्य प्रोग्राम / Main program"""
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
                print("[!] ईमेल कॉन्फ़िगरेशन छोड़ा जा रहा है / Skipping email configuration...")

        # उपयोगकर्ता जानकारी एकत्र करो / Collect user information
        agent.collect_user_info()

        # स्वागत संदेश भेजो / Send welcome message
        agent.send_welcome_message()

        logger.info("Program completed successfully")

    except KeyboardInterrupt:
        print("\n\n[X] प्रोग्राम उपयोगकर्ता द्वारा बंद किया गया / Program interrupted by user")
        logger.info("Program interrupted by user")

    except Exception as e:
        print(f"[X] प्रोग्राम में त्रुटि / Fatal error in program: {e}")
        logger.error(f"Fatal error: {e}")


if __name__ == '__main__':
    main()
