import math, os
from pymemcache.client.base import Client

class MyLib:
    def __init__(self):
        MEMCACHED_SERVER = os.getenv('MEMCACHED_SERVER', '127.0.0.1')
        MEMCACHED_PORT = os.getenv('MEMCACHED_PORT', 11211)
        #self.client = Client(('127.0.0.1', 11211))
        self.client = Client((MEMCACHED_SERVER, MEMCACHED_PORT))
        self.chunk_size = 1000000.0

    def get_counts(self, file_size):
        return int(math.ceil(file_size / self.chunk_size))

    def set_file(self, name, obj_file):
        file_size = len(obj_file.read())
        if self.client.get("%s%s%s" % (name, "_", str(0))) is not None:
            return "File already exists."

        if file_size <= 50000000:
            obj_file.seek(0)
            counts = self.get_counts(file_size)
            self.client.set(name, counts)
            for i in range(counts):
                data = obj_file.read(int(self.chunk_size))
                self.client.set("%s%s%s" % (name, "_", str(i)), data)
            return "Done."
        else:
            return "Oversized, rejected."

    def get_file(self, name):
        if self.client.get("%s%s%s" % (name, "_", str(0))) is None:
            return "File doest not exists."
        try:
            counts = int(self.client.get(name))
            obj_file = b''
            for i in range(counts):
                data = self.client.get("%s%s%s" % (name, "_", str(i)))
                obj_file = obj_file + data
            file = open(name, 'wb')
            file.write(obj_file)
            file.close()
            return name
        except:
            return None
