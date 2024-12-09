from flask import Flask, render_template, request, jsonify
from pylint.lint import Run
import os

app = Flask(__name__)

def analyze_code(code: str):
    """
    Analyze the provided Python code using Pylint.

    Args:
        code (str): Python code snippet to analyze.

    Returns:
        dict: Analysis results with messages.
    """
    # Write the code to a temporary file
    temp_file = "temp_code.py"
    with open(temp_file, "w") as f:
        f.write(code)

    # Run Pylint
    results = Run([temp_file], do_exit=False)
    
    messages = []
    for msg in results.linter.reporter.messages:
        messages.append(f"{msg.msg_id}: {msg.msg} (line {msg.line})")

    # Cleanup the temporary file
    os.remove(temp_file)

    return {"messages": messages}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        code = request.form.get("code")
        if not code:
            return jsonify({"error": "No code provided!"}), 400

        analysis_results = analyze_code(code)
        return jsonify(analysis_results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
