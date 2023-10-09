```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chart_of_accounts', methods=['GET'])
def get_chart_of_accounts():
    access_token = request.headers.get('netsuite_access_token')
    if not access_token:
        return jsonify({"error": "No access token provided"}), 400

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    response = requests.get('https://netsuite.com/api/chart_of_accounts', headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch chart of accounts"}), 500

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
```