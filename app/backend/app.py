from flask import Flask, send_from_directory, jsonify
import os
import json

# Adjust the path to frontend
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data'))

app = Flask(__name__, static_folder=frontend_path, template_folder=frontend_path)

@app.route('/')
def serve_index():
    return send_from_directory(frontend_path, 'index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory(frontend_path, 'style.css')

@app.route('/script.js')
def serve_js():
    return send_from_directory(frontend_path, 'script.js')

@app.route('/api/user-data')
def get_user_data():
    try:
        with open(os.path.join(data_path, 'sample_user_data.json')) as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
