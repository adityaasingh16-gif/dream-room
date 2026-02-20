from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'dream_room_secret'

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/api/save-design', methods=['POST'])
def save_design():
    """
    API Endpoint to receive room data.
    In a real app, you would save this to a database (SQL/PostgreSQL).
    """
    data = request.json
    print(f"Received design configuration: {data}")
    
    # Simulate a processing delay
    # Here is where you could trigger an AI image generation (Stable Diffusion)
    
    return jsonify({"status": "success", "message": "Room design saved!"})

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(debug=True, port=5000)