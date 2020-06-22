import sys
import telnetlib
import getpass

HOST = "192.168.122.72"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("admin\n")
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name Python_VLAN_2\n")
tn.write("vlan 3\n")
tn.write("name Python_VLAN_3\n")
tn.write("vlan 4\n")
tn.write("name Python_VLAN_4\n")
tn.write("vlan 5\n")
tn.write("name Python_VLAN_5\n")
tn.write("end\n")
tn.write("exit\n")

print (tn.read_all())