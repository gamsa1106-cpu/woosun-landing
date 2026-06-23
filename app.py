import os
import smtplib
from email.mime.text import MIMEText
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

GMAIL_USER = os.environ.get('GMAIL_USER')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD')

def send_email(name, phone, message):
    body = f"""
우선컴퍼니 홈페이지 문의가 접수되었습니다.

이름: {name}
연락처: {phone}
문의 내용:
{message}
"""
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = f'[우선컴퍼니] 새 문의 - {name}'
    msg['From'] = GMAIL_USER
    msg['To'] = GMAIL_USER

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.send_message(msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name', '')
    phone = data.get('phone', '')
    message = data.get('message', '')

    try:
        send_email(name, phone, message)
        return jsonify({'message': '문의가 접수되었습니다. 빠른 시일 내에 연락드리겠습니다.'})
    except Exception as e:
        print(f"이메일 전송 실패: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
