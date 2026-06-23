from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    print(f"문의 접수 - 이름: {data.get('name')}, 연락처: {data.get('phone')}, 내용: {data.get('message')}")
    return jsonify({'message': '문의가 접수되었습니다. 빠른 시일 내에 연락드리겠습니다.'})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
