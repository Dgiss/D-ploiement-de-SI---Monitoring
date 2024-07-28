from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import os
from pythonjsonlogger import jsonlogger

app = Flask(__name__)

# Ensure the log directory exists
log_dir = './projectTest'
log_file = os.path.join(log_dir, 'app.log')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Setup logging configuration
handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

# Custom JSON formatter
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record['timestamp'] = self.formatTime(record, self.datefmt)
        log_record['action'] = record.getMessage()
        log_record['ip'] = request.remote_addr

formatter = CustomJsonFormatter('%(timestamp)s %(action)s %(ip)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

@app.route('/')
def hello_world():
    app.logger.info('Accès à la route /')
    return 'Hello'

@app.route('/sum', methods=['GET'])
def sum_route():
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            app.logger.error("Les paramètres 'a' et 'b' sont requis")
            response = {"error": "Les paramètres 'a' et 'b' sont requis"}
            return jsonify(response), 400

        result = add(a, b)
        app.logger.info(f'Somme de {a} et {b} est {result}')
        response = {"a": a, "b": b, "sum": result}
        app.logger.info(f'Réponse: {response}')
        return jsonify(response)

    except Exception as e:
        app.logger.error(f'Erreur : {str(e)}')
        response = {"error": str(e)}
        app.logger.info(f'Réponse: {response}')
        return jsonify(response), 500

@app.route('/subtract', methods=['GET'])
def subtract_route():
    try:
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        if a is None or b is None:
            app.logger.error("Les paramètres 'a' et 'b' sont requis")
            response = {"error": "Les paramètres 'a' et 'b' sont requis"}
            return jsonify(response), 400

        result = subtract(a, b)
        app.logger.info(f'La différence entre {a} et {b} est {result}')
        response = {"a": a, "b": b, "difference": result}
        app.logger.info(f'Réponse: {response}')
        return jsonify(response)

    except Exception as e:
        app.logger.error(f'Erreur : {str(e)}')
        response = {"error": str(e)}
        app.logger.info(f'Réponse: {response}')
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
