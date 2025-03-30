from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
     # read the JSON file
    with open('items.json', 'r') as items_file:
        # Gets the dictionary with the list
        item_data = json.load(items_file)

    # item.data.get extracts the list and passes to template
    return render_template('items.html', items=item_data.get("items"))

if __name__ == '__main__':
       app.run(debug=True, port=5000)