from flask import Flask, Response, json , send_from_directory , request

app = Flask(__name__)

@app.route("/home")
def serve_home():
    return send_from_directory("static", "index.html")

@app.route("/plus")
def calculate_sum():
    arguments = request.args
    number1 = float(arguments.get("number1"))
    number2 = float(arguments.get("number2"))

    response_data = {
        "number1" : number1,
        "number2" : number2,
        "result" : number1 + number2
    }
    return response_data

@app.errorhandler(404)
def page_not_found(error_code):
    response ={
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(json_response, status=404, mimetype="application/json")
    return http_response
app.run(host="127.0.0.1", port=3000, use_reloader=True)