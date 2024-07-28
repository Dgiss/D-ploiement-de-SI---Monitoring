from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

@app.route('/')
def hello_world():
    return 'Hello, Mr. Mokrmñ!'

@app.route('/sum', methods=['GET'])
def sum_route():
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            return jsonify({"error": "Les paramètres 'a' et 'b' sont requis"}), 400

        result = add(a, b)
        return jsonify({"a": a, "b": b, "sum": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/subtract', methods=['GET'])
def subtract_route():
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            return jsonify({"error": "Les paramètres 'a' et 'b' sont requis"}), 400

        result = subtract(a, b)
        return jsonify({"a": a, "b": b, "difference": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
