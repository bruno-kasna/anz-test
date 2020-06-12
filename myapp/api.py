import os
from flask import Flask

app = Flask(__name__)
app_name = 'myapplication'


@app.route('/version', methods=['GET'])
def home():
    response = {
        app_name: {
            "version": os.environ['VERSION'],
            "lastcommitsha": os.environ['LAST_COMMIT_SHA'],
            "description": "pre-interview technical test"
        }
    }
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
