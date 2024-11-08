from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Помилка: ділення на нуль"
            return redirect(url_for("result", result=result))
        except ValueError:
            return redirect(url_for("result", result="Помилка: введіть числа коректно"))

    return render_template("index.html")

@app.route("/result")
def result():
    result = request.args.get("result", "")
    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
