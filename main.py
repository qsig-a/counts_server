from flask import Flask,request,Response
from functools import wraps
import os,argparse

yes_count = 0
no_count = 0

parser = argparse.ArgumentParser()
parser.add_argument("-url", "--public_url", action="store")
parser.add_argument("-p", "--port", action="store")
args = parser.parse_args()

def get_port(args):
    if os.environ.get('SERVER_PORT'):
        server_port = int(os.environ.get('SERVER_PORT'))
        return server_port
    elif args.port:
        server_port = int(args.port)
        return server_port
    else:
        server_port = 8080
        return server_port

server_port = get_port(args)

def get_url(args):
    if os.environ.get('PUBLIC_URL'):
        public_url = os.environ.get('PUBLIC_URL')
        return public_url
    elif args.public_url:
        public_url = args.public_url
        return public_url
    else:
        public_url = "http://localhost:" + str(server_port)
        return public_url

public_url = get_url(args)

resp_get_digits = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather input="dtmf" timeout="10" numDigits="1"  action="{public_url}/count">
        <Say>Please press 1 for yes and 2 for no.</Say>
    </Gather>
</Response>
"""

resp_recorded = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
     <Say>Your Response has been recorded.</Say>
</Response>
"""

resp_nodigit = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Wrong Digit Entered, please try again./Say>
    <Gather input="dtmf" timeout="10" numDigits="1" action="{public_url}/count">
        <Say>Please press 1 for yes and 2 for no.</Say>
    </Gather>
</Response>
"""

resp_retry = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say>Wrong Digit Entered, please try again./Say>
    <Gather input="dtmf" timeout="10" numDigits="1"  action="{public_url}/count">
        <Say>Please press 1 for yes and 2 for no.</Say>
    </Gather>
</Response>
"""

app = Flask(__name__)

@app.route("/")
# Home/Health Check?
def home():
    return "Hello! I am the counts bot"

@app.route("/begin")
# Beginning XML
def begin():
    return Response(resp_get_digits,mimetype='text/xml')


@app.route("/count",methods=['POST'])
# Add to counts
def count():
    global yes_count
    global no_count
    data = request.form
    if "Digits" in data:
        digitToProc = data.get("Digits")
        if digitToProc == "1":
            yes_count += 1
            return Response(resp_recorded,mimetype='text/xml')
        elif digitToProc == "2":
            no_count += 1
            return Response(resp_recorded,mimetype='text/xml')
        else:
            return Response(resp_retry,mimetype='text/xml')
    else:
        return Response(resp_nodigit,mimetype='text/xml')

@app.route("/getcounts",methods=['GET'])
# Get Counts
def getcounts():
    global yes_count
    global no_count
    return "Yes Counts: " + str(yes_count) + "\nNo Counts: " + str(no_count)

# Run the thing
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=False,port=server_port)