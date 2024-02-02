from flask import Flask,request
import socket
import subprocess
app = Flask(__name__)

@app.route("/")
def getHostName():
    return socket.gethostname()

@app.route("/", methods = ['POST'])
def runSubProcess():
    result = subprocess.Popen(["python3","stress_cpu.py"])
    return socket.gethostname()

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port=5000)
