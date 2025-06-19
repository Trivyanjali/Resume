from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    resume_data = {
        "name": "Trivyanjali Dasari",
        "title": "Software Engineer | Web Developer",
        "email": "trivyanjalidasari421@gmail.com",
        "phone": "7842523239",
        "location": "New York, NY",
        "linkedin": "linkedin.com/in/anjali",
        "github": "github.com/johndoe",
        "about": "Passionate HARDWARE engineer with 5+ years of experience building scalable web applications and services.",
        "skills": [
            "Python, JavaScript",
            "PRINTED CIRCUIT BOARD DESIGNING",
            "SQL, NoSQL Databases"
        ],
        "experience": [
            {
                "position": "Senior Software Engineer",
                "company": "Tech Innovators Inc.",
                "duration": "Jan 2022 - Present",
                "description": "Leading backend team in developing microservices architecture and improving system scalability."
            },
            {
                "position": "Fresher",
                "company": "Web Solutions LLC",
                "duration": "Jun 2018 - Dec 2021",
                "description": "Developed customer-facing web apps using Flask and React, increasing user engagement by 40%."
            }
        ],
        "education": [
            {
                "degree": "B tech",
                "school": "Sri vasavi engineering clg",
                "years": "2022-2026"
            }
        ],
        "projects": [
            {
                "description": "Printed circuit board designing."
            }
        ]
    }
    return render_template("index.html", resume=resume_data)

if __name__ == "__main__":
    app.run(debug=True)
