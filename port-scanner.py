import socket
import sys
from optparse import OptionParser
from queue import Queue
from threading import Lock, Thread
from time import sleep, time

parser = OptionParser()
parser.add_option("-H", "--host", dest="host", help="host address")
(options, arguments) = parser.parse_args()
socket.setdefaulttimeout(0.25)
print_lock = Lock()
q = Queue()


def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((t_IP, port))
        with print_lock:
            print(f'{port}\t open')
        s.close()
    except:
        pass


def threader():
    while True:
        port_g = q.get()
        port_scan(port_g)
        q.task_done()


print(r"""
    ____             __     _____                                 
   / __ \____  _____/ /_   / ___/_________ _____  ____  ___  _____
  / /_/ / __ \/ ___/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / /  / /_    ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/    \____/_/   \__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     

""")
target = options.host
if not target:
    target = input('Enter the host to be scanned: ')

try:
    t_IP = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved")
    sleep(3)
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sleep(3)
    sys.exit()

print(f'Starting scan on host: {t_IP}\n')
print('Port\tStatus')
startTime = time()

for _ in range(100):
    t = Thread(target=threader, daemon=True)
    t.start()

for port_p in range(1, 1024):
    q.put(port_p)

q.join()
print('\nTime taken:', str(int(time() - startTime)) + 's')
