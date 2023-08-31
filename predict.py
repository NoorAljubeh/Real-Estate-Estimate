from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace this with the actual API URL for prediction
AI_API_URL = 'https://your-prediction-api-url.com/predict'

@app.route('/', methods=['GET', 'POST'])
def index():
    print("request.args")
    if request.method == 'POST':
        # Collect form data into a dictionary
        data = {
            'longitude': request.form.get('longitude'),
            'latitude': request.form.get('latitude'),
            'totalRooms': request.form.get('totalRooms'),
            'totalBedrooms': request.form.get('totalBedrooms'),
            'population': request.form.get('population'),
            'households': request.form.get('households'),
            'medianIncome': request.form.get('medianIncome'),
            'oceanProximity': request.form.get('oceanProximity'),
            'housingMedianAge': request.form.get('housingMedianAge'),
        }
        
        print("Collected data:", data)  # Print the collected data
        
        try:
            # Send a POST request to your prediction API
            response = requests.post(AI_API_URL, json=data)
            response.raise_for_status()  # Raise an exception for bad responses
            prediction = response.json().get('prediction', None)
            
            if prediction is not None:
                # If it's an AJAX request, return JSON
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return jsonify({'prediction': prediction})
                
                # Otherwise, render the template with the prediction
                return render_template('index.html', prediction=prediction)
            else:
                # Handle the case where the API did not return a prediction
                return render_template('index.html', prediction=None, error="No prediction available.")
        
        except requests.exceptions.RequestException as e:
            # Handle request-related errors (e.g., connection error)
            return render_template('index.html', prediction=None, error="Error connecting to the prediction service.")

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
