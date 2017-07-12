# RvfbRobot Flask API
Kick off [RobotFramework](http://robotframework.org/) tests through a [Flask](http://flask.pocoo.org/) API.

## Setup
```
git clone git@github.com:ogryzek/rvfb_robot_flask.git
cd rvfb_robot_flask && git checkout dockerize

docker-compose build    # build docker image
docker-compose up -d    # run in the background

# to take down run:
docker-compose down --volumes
```

Then open up [localhost:3000](http://localhost:3000) to run the tests. View results at [localhost:3000/log.html](http://localhost:3000/log.html), [localhost:5000/report.html](http://localhost:3000/report.html), or [localhost:3000/output.xml](http://localhost:3000/output.xml).
