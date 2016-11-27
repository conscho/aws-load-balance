from flask import Flask, g, render_template, request, redirect, abort, url_for

app = Flask(__name__)

@app.route('/')
def root(post=0):


if __name__ == '__main__':
    app.run()
