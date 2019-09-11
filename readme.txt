This script is a very basic HTTP listener built with Flask.

Precautions:
* Make sure that you have Flask installed in your pipenv.
* Make sure that you have disabled firewalld & iptables OR modified the rules to allow incoming traffic to 5000 port.
* All data in results.json will be replaced anytime you start script.
* There is no authentication as I was just experimenting Flask and it was not needed on that stage.

How-to use:
* Start the script. In default it listens from: http://IP_ADDRESS:5000/listener
* Send data using HTTP POST method. I suggest using Postman for this. Curl is also OK, for example:
    * curl -X POST http://SERVER_IP:5000/listener -H 'cache-control: no-cache' -H 'content-type: application/json' -d '{"actualdata1": "value1"}'
* After you stop the script, all received data will be written into results.json.

Reason I worked on this:
Splunk has a feature to export any Alert data to a HTTP webhook as an "Alert Action". I was planning to run a simple HTTP listener to collect this alert data from Splunk and start using in my scripts. I have first tried to write the listened results to a file in disk to understand how it works.

I was expecting script to append data to file whenever it receives a new data. Unfortunately it was not working in real time - to write data to file, I had to stop the script. My use-case requires a streaming session and it seems like it is not possible with this approach.
