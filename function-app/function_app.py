import azure.functions as func
import logging
import json
import urllib.request
import urllib.error

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

LOGIC_APP_URL = "https://prod-10.eastus.logic.azure.com:443/workflows/6542eb8ee3c1421292c5b06b706c3b11/triggers/When_an_HTTP_request_is_received/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2FWhen_an_HTTP_request_is_received%2Frun&sv=1.0&sig=PEMkf_WcNo6rl4LF0aUNGzm2NEvG5OLzMaKKjCwcTuE"

@app.route(route="send", methods=["POST"])
def send_email(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Email proxy function triggered')
    
    try:
        req_body = req.get_json()
        
        # Convert plain text body to HTML with proper line breaks
        body_text = req_body.get('body', '')
        html_body = body_text.replace('\n', '<br>')
        
        # Create payload with HTML body
        payload = {
            'to': req_body.get('to'),
            'subject': req_body.get('subject'),
            'body': html_body
        }
        
        data = json.dumps(payload).encode('utf-8')
        
        request = urllib.request.Request(
            LOGIC_APP_URL,
            data=data,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        
        with urllib.request.urlopen(request) as response:
            response.read()  # Consume the response
            return func.HttpResponse(
                json.dumps({"status": "success"}),
                status_code=200,
                mimetype="application/json"
            )
            
    except urllib.error.HTTPError as e:
        logging.error(f"HTTP Error: {e.code} - {e.read().decode()}")
        return func.HttpResponse(
            json.dumps({"error": f"Failed: {e.code}"}),
            status_code=e.code,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
