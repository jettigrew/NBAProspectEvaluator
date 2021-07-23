import flask
from flask import render_template, request
import pandas as pd
import prediction
import logging
from visualization import start_visualization

app = flask.Flask(__name__)

logging.basicConfig(filename='logger.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s : %(message)s')

start_visualization(app)

prospect_df = pd.read_csv('2021_NBA_prospects.csv')
prospect_df = prospect_df.set_index("Player")
prospect_df.index = prospect_df.index.str.lower()
prospect_df = prospect_df.fillna(0)

training_df = pd.read_csv('NBA_training_dataset.csv')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def search_players():
    text = request.form['player']
    return render_template(
        "results.html",
        player=text.upper(),
        description=prediction.make_prediction(text, prospect_df)
    )


@app.route('/dashboard')
def dash():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
