# Very basic python listener in Flask - gets the result, writes to results.json file. For every new session,
# it starts from scratch and replaces results.json. At the end of the session, it writes the results to results.json.
# I was expecting something to work in real-time, so this project is a waste of time for me now.

# To run a full CURL Request from CLI:
#       curl -X POST \
#       http://SERVER_IP:5000/listener \
#       -H 'cache-control: no-cache' \
#       -H 'content-type: application/json' \
#       -d '{"actualdata1": "value1"}'

from flask import Flask, request, abort
import json

f = open("results.json", "w")

app = Flask(__name__)

@app.route('/listener', methods=['POST'])
def webhook():
    if request.method == 'POST':
        global splunk_log
        splunk_log = (request.json)
        print(splunk_log)
        k = json.dumps(splunk_log)
        # splunk_converted = json.loads(splunk_log)
        # splunk_bas = json.dumps(splunk_converted)
        f.write(k)
        return '', 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

f.close()
###
