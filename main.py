

from flask import Flask, render_template, request, jsonify

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_content
from learning_path import create_learning_path

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/health")
def health():
    return jsonify({
        "status": "success",
        "message": "EduGenie Python backend is running!"
    })


@app.route("/api/learn", methods=["POST"])
def learn():
    data = request.get_json(silent=True) or {}
    topic = data.get("topic", "")
    level = data.get("level", "Beginner")

    result = explain_topic(topic, level)
    return jsonify({"result": result})


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    result = answer_question(question)
    return jsonify({"result": result})


@app.route("/api/quiz", methods=["POST"])
def quiz():
    data = request.get_json(silent=True) or {}
    topic = data.get("topic", "")
    count = data.get("number_of_questions", 5)

    try:
        count = int(count)
    except (ValueError, TypeError):
        count = 5

    result = generate_quiz(topic, count)
    return jsonify(result)


@app.route("/api/summary", methods=["POST"])
def summary():
    data = request.get_json(silent=True) or {}
    content = data.get("content", "")

    result = summarize_content(content)
    return jsonify({"result": result})


@app.route("/api/learning-path", methods=["POST"])
def learning_path():
    data = request.get_json(silent=True) or {}
    goal = data.get("goal", "")
    level = data.get("level", "Beginner")

    result = create_learning_path(goal, level)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, port=5000)