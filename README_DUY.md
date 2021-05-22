## Install packages
$ pip install -r requirements.txt
## input Memcached server address to the lib file
replace the self.client = Client(('127.0.0.1', 11211)) with the real Memcached server address
## Running
python api.py