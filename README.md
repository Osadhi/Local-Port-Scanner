<h1>Local Port Scanner</h1>
<p>Tooling that scan specific IP or <b>automates</b> scan all the local IPs on your network.</p>

## Table of contents
- [Installing Local Port Scanner](#installation)
- [Running Local Port Scanner](#running-local-port-scanner)
- [Updating Local Port Scanner](#updating-local-port-scanner)

## **Installation**
```elm
pip install local-port-scanner
```
__Important:__ depending on your system, make sure to use `pip3` and `python3` instead.


>If you would like to install a specific version of Local Port Scanner you may do so with:
>```elm
>pip install local-port-scanner==0.0.2
>```

#### Running Local Port Scanner

Local Port Scanner is not only a tool but also it is a module

##### Use as a tool
Run the port scanner as the following Example.
```elm
python port_scanner -a
```
There are specific commands to use in Port Scanner.
<br />
'-a' command is used to auto-discover host in your local network and scan if there are open ports.
<br/>
'-H' command is used to specify the host.
<br/>

If you want to know more commands use '-h' command.

Run the netdiscover as the following Example.
```elm
python netdiscover 
```
It just discovers all the host IPs and Mac addresses.
##### Use as a module

There are two classes you can use.
- port_scanner
  * To scan specific target
 ```elm
from loacl_scanner import Scan
Scan(target='127.0.0.1')
```
- netdiscover
  * To discover host in the Local network
 ```elm
from loacl_scanner import NetDiscover
NetDiscover(output=True)
```
#### Updating Local Port Scanner
```elm
pip install local-port-scanner -U
```



---

> **Disclaimer**<a name="disclaimer" />: Please Note that this is a research project. I am by no means responsible for any usage of this tool.
