from flask import Flask, render_template
from court_data import fetch_sample_data

app = Flask(__name__)

@app.route('/')
def index():
    data = fetch_sample_data()
    return render_template('index.html', court_data=data)

if __name__ == '__main__':
    app.run(debug=True)

