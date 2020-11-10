from flask import Flask

app = Flask(__name__)


# Escape characters

@app.route('/')
def hello_world():
    split_string = "This string has been\nsplit\nover\nseveral\nlines"
    print(split_string)
    print("Hello, everyone")
    return split_string


if __name__ == '__main__':
    app.run()
