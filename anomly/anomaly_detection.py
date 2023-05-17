import pandas as pd
from sklearn.cluster import KMeans

def perform_anomaly_detection(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Filter out non-numeric columns
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    data = df[numeric_columns]

    # Perform anomaly detection
    kmeans = KMeans(n_clusters=5).fit(data) 
    labels = kmeans.labels_

    # Prepare the results
    anomaly_results = {
        'data': df.values.tolist(),
        'labels': labels.tolist()
    }

    return anomaly_results
