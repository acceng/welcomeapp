from flask import Flask

app = Flask(__name__)

@app.route('/welcome/')
@app.route('/welcome/<nama>')
def welcome(nama=None):
    if not nama:
        nama = "anonymous"
    return f"Selamat datang {nama}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

