from flask import Flask, render_template
app = Flask (__name__)

@app.route ('/')
def index ():
    name="Obie"
    nameChars= []

    days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    for char in name:
        nameChars.append(char)

    return render_template('exercise2.html', my_name=name, characters=nameChars, week=days)

if __name__ == '__main__':
    app.run(debug=True)