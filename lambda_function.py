from azure.storage.blob import BlobServiceClient
import pandas as pd
import io
import json

def process_data():
    # Use Azurite connection
    connect_str = "UseDevelopmentStorage=true"

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    container_name = "datasets"
    blob_name = "All_Diets.csv"

    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

        data = blob_client.download_blob().readall()

        df = pd.read_csv(io.BytesIO(data))

        avg = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()

        result = avg.reset_index().to_dict(orient='records')

        with open("results.json", "w") as f:
            json.dump(result, f)

        return "SUCCESS: Data processed"

    except Exception as e:
        return f"ERROR: {str(e)}"

print(process_data())
