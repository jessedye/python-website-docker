from flask import Flask  
from flask import render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/healthz/ready')
def health_check_ready():
    # Perform any necessary checks here (e.g., database connectivity)
    # For simplicity, we'll just return a 200 OK response
    return jsonify(status="ready"), 200

# run the application
if __name__ == "__main__":  
    app.run(host='0.0.0.0',debug=True,port=8080)
