from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    todo_list = [
        "1. Create a <strong>new directory</strong> for your project.",
        "2. Navigate to the directory and create a <strong>virtual environment</strong>.",
        "3. Install Flask using: <strong>pip install Flask</strong>",
        "4. Create a new file called <strong>app.py</strong> and add the required code.",
        "5. Create a new directory called templates and create a new file called <strong>index.html</strong> with the required code.",
    ]
    return render_template("index.html", todo_list=todo_list)

if __name__ == "__main__":
    app.run(debug=True)
