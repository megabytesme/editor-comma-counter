from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count_commas', methods=['GET'])
def count_commas():
    input_string = request.args.get('text', '')
    comma_count = input_string.count(',')
    return jsonify({'comma_count': comma_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    