from flask import Flask
from config import build
from services import get_output
app = Flask(__name__)

@app.route("/")
def hello():
    return get_output(build)

if __name__ == "__main__":
    app.run()
