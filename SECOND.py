# question

'''logs = ["192.168.1.2, tried to access this server but failed",
	"192.123.23.22, tried to access this server but failed",
	"172.23.44.51, tried to access this server but failed",
	"192.43.22.1, tried to access this server but failed",
	"192.123.23.22, tried to access this server but failed",
	"192.123.23.22, tried to access this server but failed"
	"172.23.44.51, tried to access this server but failed"]
you are given this log containing a list of users who tried accessing the company server and failed, write a python program to prints out the IP address with the most failed attempt.'''

# solution


logs = ["192.168.1.2, tried to access this server but failed", "192.123.23.22, tried to access this server but failed", "172.23.44.51, tried to access this server but failed", "192.43.22.1, tried to access this server but failed", "192.123.23.22, tried to access this server but failed", "192.123.23.22, tried to access this server but failed", "172.23.44.51, tried to access this server but failed"]

peter = max(logs, key=logs.count)
rita = peter[:-40]
print(rita)
