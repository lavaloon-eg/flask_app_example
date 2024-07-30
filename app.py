from flask import Flask, render_template, jsonify
from endpoints import create_app

app = create_app()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
