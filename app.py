from flask import Flask

app = Flask(__name__)


# Escape characters

@app.route('/')
def hello_world():
    split_string = "This string has been\nsplit\nover\nseveral\nlines"
    print(split_string)
    tabbedString = "1\t2\t3\t4\t5"
    name = input("Please enter name")
    print("Hello, everyone")
    print(type(name))
    print(name + " is " + " hello ")
    print(tabbedString)
    return "Hello", name


#Practice Scratches
coolRunning = "A cool jamaican movie"
print(coolRunning[2], coolRunning[4], coolRunning[7], coolRunning[9])
if __name__ == '__main__':
    app.run()
