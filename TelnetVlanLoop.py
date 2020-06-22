import sys
import telnetlib
import getpass

HOST = ""
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

for i in range (2,101):
    tn.write("vlan " + i.str() + "\n")
    tn.write("name Python_VLAN_" + i.str() + "\n")
    tn.write("end\n")

tn.write("exit\n")

print (tn.read_all())