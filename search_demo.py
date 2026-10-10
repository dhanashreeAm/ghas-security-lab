from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/search")
def search():
    query = request.args.get("q", "")
    command = "grep -R " + query + " ."
    subprocess.run(command, shell=True, check=False)
    return "Search completed"
