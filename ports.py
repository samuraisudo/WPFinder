def check():
	with open("USE_PORTS.rf") as file:
		port_list = [row.strip() for row in file]
	return port_list
def passw():
	with open("USE_PASS.rf") as file:
		pass_list = [row.strip() for row in file]
	return pass_list
def logi():
	with open("USE_LOGINS.rf") as file:
		log_list = [row.strip() for row in file]
	return log_list
