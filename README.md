# tap-exchangeratesapi

A [Singer](https://singer.io) Tap to extract currency exchange rate
data from [exchangeratesapi.io](http://exchangeratesapi.io).

---

Copyright &copy; 2017 Stitch

### config.json:
```
{
    "base": "AUD",
    "start_date": "2017-02-02",
    "api_key": "123abc456def"
}

```

### state.json
```
{"start_date": "2021-03-31"}
```

## Installation
### Prepare Server

1. Installation of Ubuntu 18.04
2. Install python 3.7.1 from source code
```
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
cd /tmp
wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz
tar –xf Python-3.7.1.tgz
```

Info: https://phoenixnap.com/kb/how-to-install-python-3-ubuntu

3. Install pip3
See here: https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/

4. Install setuptools for pip
```
pip install setuptools
```

### Create python environments
We use different environments for each pymodul from singer.io to avoid version conflicts
1. Create tap-exchangeratesapi environment
```
#Create environment
python3 -m venv .virtualenvs/tap-exchangeratesapi
#Activate environment
source .virtualenvs/tap-exchangeratesapi/bin/activate
# Go to exchangeratesapi repo
cd tap-exchangeratesapi
#Install requierements
pip install -r requirements.txt
# Install tap-exchangeratesapi as py modul in environment
python setup.py build --force
python setup.py install
```

2. Create environment for target for example stitch or csv
```
# Install target-stitch in its own virtualenv
python3 -m venv .virtualenvs/target-stitch
source .virtualenvs/target-stitch/bin/activate
pip install target-stitch
deactivate


# Install target-csv in its own virtualenv
python3 -m venv .virtualenvs/target-csv
source .virtualenvs/target-csv/bin/activate
pip install target-csv
deactivate
```

## EXECUTE THE PACKAGE (with a target)

.virtualenvs/tap-exchangeratesapi/bin/tap-exchangeratesapi --config "config_fil" --state "state-file" | .virtualenvs/target-csv/bin/target-csv