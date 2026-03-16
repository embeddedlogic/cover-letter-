from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    company = request.form["company"]
    position = request.form["position"]
    skills = request.form["skills"]
    experience = request.form["experience"]

    cover_letter = f"""
Dear Hiring Manager,

My name is {name} and I am writing to apply for the {position} position at {company}.

I am interested in this opportunity because it matches my interest in learning and growing in the field. 
My skills in {skills} and my experience with {experience} have helped me build a strong foundation that I can bring to your team.

I am excited about the chance to contribute to {company} while continuing to develop my knowledge and professional abilities.

Thank you for your time and consideration. I look forward to the opportunity to speak with you.

Sincerely,
{name}
"""

    return render_template("result.html", letter=cover_letter)

if __name__ == "__main__":
    app.run(debug=True)