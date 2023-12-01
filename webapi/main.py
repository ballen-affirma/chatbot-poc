import json
import os
import call_chat_bison
from flask import Flask, request, jsonify

app = Flask(__name__)
call_chat_bison.init()

@app.route("/")
def root():
    return json.dumps({})

@app.route("/predict", methods=['GET'])
def handleRequest():
    text = request.args.get("msg")
    response = jsonify({'response': call_chat_bison.predict(text)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    print(text)
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))