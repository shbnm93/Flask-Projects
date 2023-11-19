from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_variable = "Rose"
    return render_template('index1.html', my_variable = my_variable)


if __name__ == '__main__':
    app.run(debug=True)


