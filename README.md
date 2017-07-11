# RvfbRobot Flask API
Kick off [RobotFramework](http://robotframework.org/) tests through a [Flask](http://flask.pocoo.org/) API.

## Setup
```
git clone git@github.com:ogryzek/rvfb_robot_flask.git
cd rvfb_robot_flask

pip install -r requirements.txt

export FLASK_APP=app.py
flask run
```

Then open up [localhost:5000](http://localhost:5000) to run the tests. View results at [localhost:5000/log](http://localhost:5000/log), [localhost:5000/report](http://localhost:5000/report), or [localhost:5000/output](http://localhost:5000/output).
