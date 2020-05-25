import sys
import socket
from time import *
from threading import *
from queue import Queue

socket.setdefaulttimeout(0.25)
print_lock = Lock()
q = Queue()

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print(f'{port}\t open')
      con.close()
   except:
      pass

def threader():
   while (True):
      port = q.get()
      portscan(port)
      q.task_done()

print("""
    ____             __     _____                                 
   / __ \____  _____/ /_   / ___/_________ _____  ____  ___  _____
  / /_/ / __ \/ ___/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / ____/ /_/ / /  / /_    ___/ / /__/ /_/ / / / / / / /  __/ /    
/_/    \____/_/   \__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                                                                  
""")
try:  
      target = sys.argv[1]
      
except:
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
   t = Thread(target = threader,daemon = True)
   t.start()
   
for port in range(1, 1024):
   q.put(port)
   
q.join()
print('\nTime taken:', str(int(time() - startTime))+'s')
