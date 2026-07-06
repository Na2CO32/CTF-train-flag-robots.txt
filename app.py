from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# 首頁
@app.route('/')
def index():
    return render_template('index.html')

# 讓 robots.txt 可以被存取
@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')

# 參賽者解碼後訪問的隱藏頁面
@app.route('/secret_path_by_A359')
def hidden_flag():
    return render_template('APFSDS.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)