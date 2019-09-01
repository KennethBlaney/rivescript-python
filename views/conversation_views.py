from app import app

@app.route("/message", methods=["POST"]):
def message():
    raise NotImplemented