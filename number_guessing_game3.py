from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def index():
    if request.method == "GET":
        minimum = 0
        maximum = 1000
        guess = int((maximum - minimum) / 2) + minimum
        return f"""
        <html>
            <body>
                <form method="POST">
                    Guessing: {guess}
                    <br>
                    <input type="hidden" name="min" value="{minimum}">
                    <input type="hidden" name="max" value="{maximum}">
                    <button type="submit" name="answer" value="low">Too low</button>
                    <button type="submit" name="answer" value="high">Too high</button>
                    <button type="submit" name="answer" value="win">You won</button>
                </form>    
            </body>
        </html>
        """
    else:
        minimum = int(request.form.get("min"))
        maximum = int(request.form.get("max"))
        if request.form.get("answer") == "low":
            minimum = int((maximum - minimum) / 2) + minimum
        elif request.form.get("answer") == "high":
            maximum = int((maximum - minimum) / 2) + minimum
        elif request.form.get("answer") == "win":
            return "I won!"

        guess = int((maximum - minimum) / 2) + minimum
        return f"""
        <html>
            <body>
                <form method="POST">
                    Guessing: {guess}
                    <br>
                    <input type="hidden" name="min" value="{minimum}">
                    <input type="hidden" name="max" value="{maximum}">
                    <button type="submit" name="answer" value="low">Too low</button>
                    <button type="submit" name="answer" value="high">Too high</button>
                    <button type="submit" name="answer" value="win">You won</button>
                </form>    
            </body>
        </html>
        """


if __name__ == '__main__':
    app.run(debug=True)

