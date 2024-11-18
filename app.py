from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Home route for greeting
@app.route('/')
def home():
    return render_template('index.html')

# API route to check server status
@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"message": "Server is up and running"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

