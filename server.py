from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
CORS(app)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "neuro.symbolic.validator.service@gmail.com"

SENDER_PASSWORD = "latf npxp fvge nsjk"  # Replace with your 16-character Google App Password

@app.route('/submit', methods=['POST'])
def handle_submission():
    data = request.get_json() or request.form
    user_email = data.get('email')
    
    if not user_email:
        return jsonify({"status": "error", "message": "Email is required"}), 400

    print(f"[+] New waitlist signup received: {user_email}")

    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = user_email
        msg['Subject'] = "Welcome to Neuro-Symbolic Validator Beta"
        
        body = (
            "Hello user,\n\n"
            "Thank you for joining the Neuro-Symbolic Validator beta. "
            "To get your code verified by our Z3 constraint solver engine, please reply directly to this email with a link to your C/C++ code on Pastebin.\n\n"
            "Once received, our engine will analyze your code for memory corruption and integer overflows, and we will send back your formal proof or counterexample.\n\n"
            "Best regards,\n"
            "Neuro-Symbolic Validator Team"
        )
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, user_email, msg.as_string())
        server.quit()
        
        print(f"[+] Autoresponder sent successfully to {user_email}")
        return jsonify({"status": "success", "message": "Email sent!"})
    
    except Exception as e:
        print(f"[-] Error sending email: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)