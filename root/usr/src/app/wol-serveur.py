from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
import requests
from wakeonlan import send_magic_packet

hostName    = "0.0.0.0"
serverPort  = int(os.environ["SERVER_PORT"])
macAdress   = os.environ["MAC"]
domain      = os.environ["REDIRECT"]
timeout     = int(os.environ["TIMEOUT"])
ssl_verify  = os.environ["SSL_VERIFY"]
timewait    = 1

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        send_magic_packet(macAdress)
        self.waitForResourceAvailable(domain,timeout,timewait,ssl_verify)
        self.send_response(301)
        self.send_header('Location', domain)
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()

    def waitForResourceAvailable(self, domain, timeout, timewait, ssl_verify):
        timer = 0
        if ssl_verify != "False":
            self.checkAvailability(domain,timer)
        else:
            self.checkAvailabilityUnsecure(domain,timer)        
    
    def checkAvailability(self, domain, timer):
        while requests.get(domain).status_code == 502:
            print("Resource not available")
            time.sleep(timewait)
            timer += timewait
            if timer > timeout:
                print("Resource timeout")
                break
            if requests.get(domain).status_code == 200:
                print("Resource available")
                break     
    
    def checkAvailabilityUnsecure(self, domain, timer):
        while requests.get(domain, verify=False).status_code == 502:
            print("Resource not available")
            time.sleep(timewait)
            timer += timewait
            if timer > timeout:
                print("Resource timeout")
                break
            if requests.get(domain, verify=False).status_code == 200:
                print("Resource available")
                break


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
