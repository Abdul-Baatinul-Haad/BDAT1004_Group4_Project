
from flask import Flask, jsonify, request, render_template
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/divisions-piechart')
def divisions():
    return render_template('divisions.html')


@app.route('/teams-table')
def teams_table():
    return render_template('table.html')

@app.route('/conference')
def conference():
    return render_template('conference.html')


if __name__ == "__main__":
    app.run()