from flask import Flask, request, jsonify, send_file
import matplotlib
import requests
from flask_cors import CORS
import matplotlib.pyplot as plt
import io
import threading
import time
import pandas as pd

app = Flask(__name__)
CORS(app)

conversion_history = []
rate_alerts = []

@app.route('/convert', methods=['GET'])
def convert_currency():
    base = request.args.get('base')
    target = request.args.get('target')
    amount = request.args.get('amount')
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{base}')
    data = response.json()
    rate = data['rates'][target]
    converted_amount = float(amount) * rate
    conversion = {
        'base': base,
        'target': target,
        'amount': amount,
        'converted_amount': converted_amount
    }
    conversion_history.append(conversion)
    return jsonify({'converted_amount': converted_amount})

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(conversion_history)

@app.route('/set_alert', methods=['POST'])


# Function to get top 10 currencies (for demonstration, replace with actual API if needed)
def get_top_currencies():
    # This URL is just an example; replace it with a reliable source or API
    # Here we are assuming a simple static list for demonstration.
    return {
        'Currency': ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD'],
        'ExchangeRate': [1.0, 0.85, 110.5, 0.75, 1.35, 1.25, 0.93, 6.5, 8.5, 1.4]
    }

@app.route('/top-currencies', methods=['GET'])
def get_graph():
    # Get data for top currencies
    data = get_top_currencies()
    df = pd.DataFrame(data)

    # Generate Pie Chart
    plt.figure(figsize=(10, 10))
    plt.pie(
        df['ExchangeRate'],
        labels=df['Currency'],
        autopct='%1.1f%%',
        colors=plt.cm.tab20.colors,
        startangle=140,
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'}
    )
    plt.title('Top 10 Currencies by Exchange Rate', fontsize=16)

    plt.legend(
        df['Currency'], 
        title="Currencies", 
        loc="center left", 
        bbox_to_anchor=(1, 0.5),
        fontsize=10
    )
    plt.tight_layout()

    # Convert plot to image and send as response
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

def check_rate_alerts():
    while True:
        for alert in rate_alerts:
            base = alert['base']
            target = alert['target']
            threshold = alert['threshold']
            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{base}')
            data = response.json()
            rate = data['rates'][target]
            if rate >= threshold:
                print(f'Alert: {base} to {target} rate has reached {rate}')
        time.sleep(60)  # Check every minute

if __name__ == '__main__':
    threading.Thread(target=check_rate_alerts).start()
    app.run(debug=True)
