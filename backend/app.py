from flask import Flask, jsonify, request
from flask_cors import CORS
from pipeline import PipelineCloud

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:8000"])
pc = PipelineCloud(token="pipeline_sk_2PBTkb8o4F51fJqBK5fVztNhSfMXQERw")

@app.route("/hello")
def hello_world():
    return "Hello, world!"

@app.route("/gptj", methods=["POST"])
def generate_gptj():
    print(request.__dict__)
    prompt = request.json["prompt"]
    run = pc.run_pipeline(
        "pipeline_6908d8fb68974c288c69ef45454c8475",
        [
            prompt,
            {
            "response_length": 64,
            "include_input": False,
            "temperature": 1.0,
            "top_k": 50
            },
        ],
    )
    response = jsonify({"result": run["result_preview"][0][0]})
    return response
