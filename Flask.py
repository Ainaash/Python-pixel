from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def main():
    return "Hello, world!"

@app.route("/second")
def second():
    return "<h1> Hello world! </h1>"

@app.route("/pixel")
def pixel():
    return  render_template("index.html")



app.run()