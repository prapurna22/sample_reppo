from flask import Flask, render_template, request
from anomaly_detection import perform_anomaly_detection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Handle file upload and perform tasks on the dataset
    file = request.files['file']
    if file:
        # Save the uploaded file
        file_path = 'uploads/' + file.filename
        file.save(file_path)

        # Perform anomaly detection
        anomaly_results = perform_anomaly_detection(file_path)

        # Render the result template and pass the anomaly results
        return render_template('result.html', results=anomaly_results)

    return "No file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
