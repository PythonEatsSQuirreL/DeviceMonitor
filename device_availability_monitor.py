import platform
import subprocess
import time

hostList = []

def ping(host):
    """
    Respond with True if the (str) host will respond to the request.
    A host may not respond to a ping even if the host name is valid.
    """
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, "1", host]
    status = subprocess.run(command, capture_output=True, text=True)
    if "unreachable" in str(status) or "Request time out" in str(status) or "Received = 0" in str(status) or "Lost = 1" in str(status):
        if host == "192.168.1.100":
            pr = "The TV under the host " + host + " is Offline"
            hostList.append(pr)
        elif host == "192.168.1.111":
            pr = "The phone under the host " + host + " is Offline"
            hostList.append(pr)
        elif host == "192.168.1.109":
            pr = "The media server under the host " + host + " is Offline"
            hostList.append(pr)
        else:
            pr = "The host " + host + " is Offline"
            hostList.append(pr)
    else:
        if host == "192.168.1.100":
            pr = "The TV under the host " + host + " is Online"
            hostList.append(pr)
        elif host == "192.168.1.111":
            pr = "The phone under the host " + host + " is Online"
            hostList.append(pr)
        elif host == "192.168.1.109":
            pr = "The media server under the host " + host + " is Online"
            hostList.append(pr)
        else:
            pr = "The host " + host + " is Online"
            hostList.append(pr)

for i in range(100000000000):
    time.sleep(30)
    ping("google.com")
    ping("192.168.1.100")
    ping("192.168.1.111")
    ping("192.168.1.109")
    ping("192.168.1.104")

    print(hostList)