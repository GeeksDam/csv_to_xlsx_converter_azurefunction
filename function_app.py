import azure.functions as func
import logging
import pandas as pd
import base64
import io

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="csvtoxls")
def csvtoxls(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON in request body.",
            status_code=400
        )

    csv_file = req_body.get('csv_file')
    if not csv_file:
        return func.HttpResponse(
            "Missing 'csv_file' in request body.",
            status_code=400
        )

    try:
        # Decode base64 CSV and read into DataFrame
        csv_bytes = base64.b64decode(csv_file)
        csv_io = io.BytesIO(csv_bytes)
        df = pd.read_csv(csv_io)

        # Write DataFrame to Excel in memory
        excel_io = io.BytesIO()
        with pd.ExcelWriter(excel_io, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        excel_io.seek(0)
        excel_base64 = base64.b64encode(excel_io.read()).decode('utf-8')

        return func.HttpResponse(
            excel_base64,
            mimetype="text/plain",
            status_code=200
        )
    except Exception as e:
        logging.error("Error processing file: {e}")
        return func.HttpResponse(
            "Error processing file.",
            status_code=500
        )