# bitmask-root
Administrative service for bitmask client.

# Installation
1- Install TAP driver for windows in third-party\tap-windows directory.<br />
2- Copy .ovpn config file to third-party\openvpn.<br />
3- Add an environment variable named BITMASK_HOME and save bitmask-root directory as value.<br />
4- Install windows service by following command (Run command prompt as administrator): <br />

```batch
windows_installer.py -install
```

5- Then start windows service:<br />

```batch
windows_installer.py -start
```

# Usage
bitmask-root has four functionality that you can call them as a rpcclient, functionalities that bitmask-root supports are :
<br />
1- start_firewall<br />
2- stop_firewall<br />
3- start_openvpn<br />
4- stop_openvpn<br />

# Example
```code
client = RPCClient("tcp://%s:%s" % (127.0.0.1, 8080))
client.start_firewall()
```

