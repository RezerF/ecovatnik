from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/ajax')
def ajax():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = a + b
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
