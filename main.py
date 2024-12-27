from flask import Flask, request, render_template, jsonify
import pandas as pd
import joblib
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model_path = r'Rossmann_model_2024-10-20-13-50-57.pkl'  # Replace with your actual file name or path
model = joblib.load(model_path)

# Function to preprocess input data
def preprocess_input(data):
    # Assuming the data requires basic preprocessing
    # Convert dates to datetime objects, process IsHoliday, IsWeekend, etc.
    data['Date'] = pd.to_datetime(data['Date'])
    # Add other preprocessing steps based on your model's requirement
    return data

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input data
        Store = int(request.form.get('Store'))
        date = request.form.get('date')
        SchoolHoliday = int(request.form.get('SchoolHoliday'))
        IsWeekend = int(request.form.get('IsWeekend'))
        is_promo = int(request.form.get('is_promo'))
        CompetitionDistance =int(request.form.get("competitionDistance"))

        # Handle CSV file upload
        file = request.files.get('file')
        if file:
            input_df = pd.read_csv(file)
        else:
            input_df = pd.DataFrame({
                'Store': [Store],
                'Date': [date],
                'SchoolHoliday': [SchoolHoliday],
                'IsWeekend': [IsWeekend],
                'CompetitionDistance':[CompetitionDistance]
            })

        # Preprocess data
        processed_data = preprocess_input(input_df)

        # Make prediction
        predictions = model.predict(processed_data)
        predicted_sales = predictions[:, 0]  # Assuming sales is the first output
        predicted_customers = predictions[:, 1]  # Assuming customers is the second output

        # Return the results as JSON
        return jsonify({
            'predicted_sales': predicted_sales.tolist(),
            'predicted_customers': predicted_customers.tolist()
        })

    except Exception as e:
        return str(e), 400

# Run the app
if __name__ == '__main__':
    app.run(debug=True)