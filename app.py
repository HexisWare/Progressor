from flask import Flask, render_template, jsonify
import datetime
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-contributions')
def get_contributions():
    contributions = generate_mock_data()
    return jsonify(contributions)

def generate_mock_data():
    today = datetime.date.today()
    last_year = today - datetime.timedelta(days=365)
    contributions = []

    date = last_year
    while date <= today:
        contributions.append({
            "date": date.strftime('%Y-%m-%d'),
            "count": random.randint(0, 10)  # Random contribution count
        })
        date += datetime.timedelta(days=1)
    
    return contributions

if __name__ == '__main__':
    app.run(debug=True)
