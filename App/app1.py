from flask import Flask, render_template, request, jsonify
import os

# Initialize the Flask application
app = Flask(__name__)

# Set a variable for the microservice version, reading from environment variables
VERSION = os.environ.get('VERSION', 'v1.0.0')

@app.route('/')
def index():
    """
    Renders the HTML form for data input (index.html).
    This is the default view.
    """
    # Use render_template to serve the index.html file
    return render_template('form.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    """
    Handles the POST request from the HTML form.
    It extracts the form data and displays a confirmation message.
    """
    # 1. Ingest the values submitted in the form
    # request.form.get('field_name') safely extracts data from the POST request
    user_name = request.form.get('user_name')
    favorite_color = request.form.get('favorite_color', 'not specified')

    # 2. Log the received data (useful for microservices monitoring)
    print(f"--- Data Received (Version {VERSION}) ---")
    print(f"Name: {user_name}")
    print(f"Color: {favorite_color}")
    print(f"--------------------------------------")

    # 3. Create a result message
    result_message = f"Thank you, {user_name}! We successfully ingested your data (Color: {favorite_color})."

    # 4. Re-render the form page, passing the result message
    # so the user can see the confirmation at the top.
    return jsonify({"result":result_message})

if __name__ == '__main__':
    # Runs the application on host 0.0.0.0 and port 8080
    # 0.0.0.0 means listen on all network interfaces, essential for containers
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))