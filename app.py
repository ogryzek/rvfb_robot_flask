from flask import Flask, request
import os
import json
import xmltodict

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def run_tests():
    results = setup_results(request.args)
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

@app.route('/output.json', methods=['GET'])
def get_output_json():
    return jsonize('static/results/output.xml')

def jsonize(xml_file, xml_attributes=True):
    with open(xml_file, "rb") as f:
        d = xmltodict.parse(f, xml_attribs=xml_attributes)
        return json.dumps(d, indent=2)

def setup_results(params):
    if 'include' not in params:
        results = os.popen("pybot -d static/results tests/tests.robot")
    else:
        results = os.popen("pybot -d static/results -i {} tests/tests.robot".format(params['include']))
    return results.read()

# run on 0.0.0.0 so Docker can expose to the outside
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
