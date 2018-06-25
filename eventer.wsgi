activate_this = '/home/host1423612/eventer-env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from index3 import app as application