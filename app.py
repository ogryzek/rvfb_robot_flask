from flask import Flask
import os

app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'])
def run_tests():
    results = os.popen('pybot -d static/results tests/tests.robot').read()
    return results

@app.route('/log', methods=['GET'])
def get_log():
    return app.send_static_file('results/log.html')

@app.route('/report', methods=['GET'])
def get_report():
    return app.send_static_file('results/report.html')

@app.route('/output', methods=['GET'])
def get_output():
    return app.send_static_file('results/output.xml')
