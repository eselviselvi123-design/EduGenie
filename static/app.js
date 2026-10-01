
async function callAPI(endpoint, data, resultId) {
    const result = document.getElementById(resultId);
    result.textContent = "Please wait... AI is processing.";

    try {
        const response = await fetch(endpoint, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const output = await response.json();

        if (!response.ok) {
            throw new Error(output.error || "Request failed.");
        }

        if (output.error) {
            result.textContent = output.error;
        } else if (output.questions) {
            displayQuiz(output.questions, result);
        } else {
            result.textContent = output.result || "No response received.";
        }
    } catch (error) {
        result.textContent = "Error: " + error.message;
    }
}

function learnTopic() {
    const topic = document.getElementById("topic").value.trim();
    const level = document.getElementById("level").value;

    callAPI("/api/learn", {
        topic: topic,
        level: level
    }, "learnResult");
}

function askQuestion() {
    const question = document.getElementById("question").value.trim();

    callAPI("/api/ask", {
        question: question
    }, "answerResult");
}

function generateQuiz() {
    const topic = document.getElementById("quizTopic").value.trim();
    const count = Number(document.getElementById("quizCount").value);

    callAPI("/api/quiz", {
        topic: topic,
        number_of_questions: count
    }, "quizResult");
}

function summarizeContent() {
    const content = document.getElementById("content").value.trim();

    callAPI("/api/summary", {
        content: content
    }, "summaryResult");
}

function createPath() {
    const goal = document.getElementById("goal").value.trim();
    const level = document.getElementById("pathLevel").value;

    callAPI("/api/learning-path", {
        goal: goal,
        level: level
    }, "pathResult");
}

function displayQuiz(questions, container) {
    container.replaceChildren();

    if (!Array.isArray(questions) || questions.length === 0) {
        container.textContent = "No quiz questions were returned.";
        return;
    }

    questions.forEach((item, index) => {
        const card = document.createElement("div");
        card.className = "quiz-question";

        const heading = document.createElement("h3");
        heading.textContent = `${index + 1}. ${item.question}`;
        card.appendChild(heading);

        if (Array.isArray(item.options)) {
            item.options.forEach(option => {
                const label = document.createElement("label");
                const radio = document.createElement("input");

                radio.type = "radio";
                radio.name = `quiz-${index}`;
                radio.value = option;

                label.appendChild(radio);
                label.appendChild(document.createTextNode(" " + option));
                card.appendChild(label);
                card.appendChild(document.createElement("br"));
            });
        }

        const answer = document.createElement("p");
        answer.textContent = "Correct answer: " + (item.answer || "Not provided");
        card.appendChild(answer);

        if (item.explanation) {
            const explanation = document.createElement("p");
            explanation.textContent = "Explanation: " + item.explanation;
            card.appendChild(explanation);
        }

        container.appendChild(card);
    });
}