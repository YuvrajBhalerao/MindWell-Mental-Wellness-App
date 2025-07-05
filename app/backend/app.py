from flask import Flask, send_from_directory, jsonify
import os
import json

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('frontend', 'index.html')

# Serve style.css
@app.route('/style.css')
def serve_css():
    return send_from_directory('frontend', 'style.css')

# Serve script.js
@app.route('/script.js')
def serve_js():
    return send_from_directory('frontend', 'script.js')

# API route to get sample user data
@app.route('/api/user-data')
def get_user_data():
    data_path = os.path.join('..', 'data', 'sample_user_data.json')
    try:
        with open(data_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run server
if __name__ == '__main__':
    app.run(debug=True)
