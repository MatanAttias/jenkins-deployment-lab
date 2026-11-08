from flask import Flask

app = Flask (__name__)

@app.route("/")
def home():
    return "Hello from Jenkins Deployment Pipeline!"

@app.route("/health")
def health():
    return {"status": "healthey"}


if __name__ == main():
    app.run(host="0.0.0.0", port=5000)