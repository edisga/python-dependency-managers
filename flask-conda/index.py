import requests, os
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    response = requests.get('https://httpbin.org/ip')
    return 'Your IP is {0}'.format(response.json()['origin'])

if __name__ == '__main__':
    port= os.environ.get('PORT')
    app.run(host='0.0.0.0', debug=False, port=port)
