from flask import Flask, request

app = Flask(__name__)

@app.route('/count_words', methods=['POST'])
def count_words():
    line = request.data.decode()
    return str(len(line.split()))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)