bit = [128, 64, 32, 16, 8, 4, 2, 1]
net = [2, 4, 8, 16, 32, 64, 128, 256]
host = [256, 128, 64, 32, 16, 8, 4, 2]
c = ['/25', '/26', '/27', '/28', '/29', '/30', '/31', '/32']

ip = input("What is the main network IP address? ")
b = ip.split(".")


networks = input("How many networks would you like to create? ")

# Number of Networks to Create
a=0
mask = bit[a]
for i in net:
	if i - 2 >= int(networks):
		print("Number of Networks that can be created: ",i)
		print("\n")
		break
	else:
		a = a + 1
		mask = mask + bit[a]

avail = ["Network ID:", "Range:", "Broadcast"]
print(avail)


H = host[a+1] #Hosts per Subnet
J = H	#Host
m = 0


while m < i - 1:
	# Network ID
	b[3] = str(J)
	ID = ".".join(b)
	

	
	# Range
	range1 = J + 1 	#Starting Range
	range2 = J + H - 2	#End Range
	Range = ("." + str(range1) + "-." + str(range2))

	# Broadcast
	bc = J + H - 1
	b[3] = str(bc)
	broadcast = ".".join(b)


	subnet = [ID, Range, broadcast]
	print(subnet)

	J = J + H
	m = m + 1


print("\nSubnet Mask:")
subnet_mask = "255.255.255." + str(mask)
print(subnet_mask)

cidr = c[a]
print("\nCIDR Notation:")
print(cidr)	

