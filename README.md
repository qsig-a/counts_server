# counts_server
 A basic TwiML/LiML server that counts yes and no answers based on calls coming in.

 ## Prerequisites

* A Twilio or Signalwire account
* A Number on said Twilio or Signalwire account
* Flask python library installed

## Running

In order to use this with Twilio or Signalwire, you will have to have a system that is either publicly accessible or use a service like [Ngrok](https://ngrok.com/) (which forwards local traffic to a publicly accessible host to your local machine)

In order for the digits to be captured properly, you do need to set the port of the server and the URL of the server.

### Setting the port

By default the app will being listening on port 8080.  You can set this to another port in 2 ways:

* SERVER_PORT Environment Variable

You can set an environment variable of SERVER_PORT to the chosen port.  For example, if choosing port 80, the environment variable would be set to `80`

* p or port argument

You can run the server with an argument of `-p` or `--port` and the port chosen.  For example, if choosing port 80, you would run the server as `python main.py -p 80`

### Setting the base URL

By default, the app will set `localhost` as the base URL

* PUBLIC_URL Envrionment variable

You can set an envrionment variable of `PUBLIC_URL` to your DNS name or IP.  For example, if using a server with a public IP of 12.34.56.78, the environment variable would be set to `http://12.34.56.78`

* url or public_url argument

You can run the server with an argument of `-url` or `--public_url` and the url in order to set it.  For example, for a URL of counts.mydomain.com, you would run it as `python main.py -url counts.mydomain.com`

 ### Setting your phone number to reach the server

 Go to your number settings in Twilio or Signalwire and set the Voice URL section (May be called something else) to go to your public URL and add a suffix of `/begin`.  So if your URL is `counts.mydomain.com` then you would enter `http://counts.mydomain.com/begin`
 
 ## Getting the counts
 
 You can see the current yes and no counts by going to the URL with a path of `getcounts`.  For example, if your URL is `counts.mydomain.com`, you would browse to `http://counts.mydomain.com/getcounts`

 ## Docker

 You can also build the docker image and use environment variables as shown above in order to run this in a Docker environment
