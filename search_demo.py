from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/search")
def search():
    query = request.args.get("q", "")

    subprocess.run(
        ["grep", "-R", "--", query, "."],
        shell=False,
        check=False,
        timeout=5,
        capture_output=True,
        text=True,
    )

    return "Search completed"
