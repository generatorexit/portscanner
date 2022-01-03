from socket import *
from threading import *
import optparse

def port_scan(targethost,targetport):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((targethost,targetport))
        print(f"[+] {targetport} => Port Open")
    except:
        print(f"[-] {targetport} => Port Close")
    finally:
        sock.close()

def host_scan(targethost,targetports):
    try:
        target_ip = gethostbyname(targethost)
        print("*"*15,"*"*len(target_ip),sep="")
        print(f"[+] IP Address: {target_ip}")
        try:
            target_name = gethostbyaddr(target_ip)
            print(f"[+] IP path: {target_name[0]}")
            print("*"*13,"*"*len(target_name[0]),sep="")
        except:
            print(f"[-] Path not found")
            print("*"*15,"*"*len(target_ip),sep="")
    except:
        print(f"[-] Host not found: {targethost}")

    setdefaulttimeout(1)
    for targetport in targetports:
        try:
            t = Thread(target=port_scan,args=(targethost,int(targetport)))
            t.start()
        except ValueError:
            print("Incorrect")

def main():
    parser = optparse.OptionParser("Usage: -H <Host Address> -p <Port Adress>")
    parser.add_option("-H", dest="targetHost", type="string", help="Target hostname")
    parser.add_option("-p", dest="targetPort", type="string", help="Specify port without (,) or (,)")
    options = parser.parse_args()[0]
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(",")
    if (targetHost == None) or (targetPorts[0] == None):
        print(parser.usage)
        exit(0)
    host_scan(targetHost,targetPorts)

if __name__ == "__main__":
    main()