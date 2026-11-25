from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hasil', methods=['POST'])
def hasil():
    nama = request.form['nama']
    return render_template('index.html', hasil=nama)

if __name__ == '__main__':
    app.run(debug=True)