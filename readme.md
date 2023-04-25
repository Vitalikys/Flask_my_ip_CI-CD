## FLASK application  
- simple one-page app for uploading to AWS EC2 by Jenkins or other CI-CD
- returns server/host IP addresses by different cases
- Deployed by Elastic Beanstalk 


### Technology stack
[![version](https://img.shields.io/badge/python-3.10-green)](https://semver.org)
[![version](https://img.shields.io/badge/AWS-4.2-green)](https://semver.org)
[![version](https://img.shields.io/badge/Flask-2.2.3-green)](https://semver.org)


### - Case how to start project
Start Redis in redis-cli :
```shell
sudo apt-get update
sudo apt-get install python3-venv
```
Clone Project and install dependencies:
```shell
git clone https://github.com/Vitalikys/test_DocuSt.git
cd test_DocuSt/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 wsgi.py
```

run without any wsgi files:
```shell
export FLASK_RUN_PORT=7778
flask --app src.main run
```

Run when main app is named 'app.py' file in the current directory:
```shell
export FLASK_RUN_PORT=7778
flask run
```