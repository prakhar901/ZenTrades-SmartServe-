import pandas as pd
import requests
from flask import Flask, render_template, request
from io import StringIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    response = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
    data = response.json()

    df = pd.DataFrame(data)

    fields_to_display = []

    if request.method == 'POST':
        fields_to_display = request.form.getlist('fields_to_display')

        df = df[fields_to_display]

        df = df.sort_values(by=['Title', 'Price'], ascending=[True, False])

    return render_template('index.html', table=df.to_html(classes='data', header=True, index=False), fields_to_display=fields_to_display)

@app.route('/upload', methods=['POST'])
def upload():
    pass

if __name__ == '__main__':
    app.run(debug=True)