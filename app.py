from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calculate_grade(score):
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be numeric.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 70:
        return "1"
    elif score >= 60:
        return "2_1"
    elif score >= 50:
        return "2_2"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


def read_student_file(filepath):
    """
    Reads a text file where each line is:
    name,score
    Returns a list of dicts: {name, score, grade}
    """

    students = []

    if not os.path.exists(filepath):
        raise FileNotFoundError("Student file not found.")

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            try:
                name, score_str = line.split(",")
                if name == "":
                    raise ValueError("Name must be a non-empty string.") 
                score = float(score_str)
                grade = calculate_grade(score)
                students.append({
                    "name": name.strip(),
                    "score": score,
                    "grade": grade
                })
            except ValueError as e:
                # Skip malformed lines
                students.append({
                    "name": e.args[0],
                    "score": -1,
                    "grade": -1
                    
                })
                continue
            except Exception:
                # Skip lines that cause other errors
                continue

    # Sort highest → lowest
    students.sort(key=lambda x: x["score"], reverse=True)
    return students


@app.route("/", methods=["GET", "POST"])
def index():
    grade = None
    error = None
    results = None

    if request.method == "POST":
        # Option 1: Single score input
        if "score" in request.form:
            user_input = request.form.get("score", "")
            try:
                score = float(user_input)
                grade = calculate_grade(score)
            except ValueError as e:
                error = str(e)

        # Option 2: Read file
        if "filename" in request.form:
            filename = request.form.get("filename", "")
            try:
                results = read_student_file(filename)
            except Exception as e:
                error = str(e)

    return render_template("index.html", grade=grade, error=error, results=results)
    

if __name__ == "__main__":
    app.run(debug=True)
