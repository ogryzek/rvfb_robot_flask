from flask import Flask
import os

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def run_tests():
    results = os.popen('pybot -d static/results tests/tests.robot').read()
    return results

@app.route('/log.html', methods=['GET'])
def get_log():
    return app.send_static_file('results/log.html')

@app.route('/report.html', methods=['GET'])
def get_report():
    return app.send_static_file('results/report.html')

@app.route('/output.xml', methods=['GET'])
def get_output():
    return app.send_static_file('results/output.xml')

# run on 0.0.0.0 so Docker can expose to the outside
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
