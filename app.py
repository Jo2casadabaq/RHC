from flask import Flask, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/habitaciones', methods=['GET'])
def habitaciones():
    return render_template("habitaciones.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)