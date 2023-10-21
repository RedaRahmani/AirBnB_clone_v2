from flask import Flask
app = Flask(__name__)

@app.route('/about', strict_slashes=False)
def Hello():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port=5000)
    app.run(host="0.0.0.0")

