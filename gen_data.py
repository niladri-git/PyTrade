#/usr/bin/python

cont_dict = {}

with open("cont.txt", "r") as file:

	for line in file:
		if "|" in line and "sh" not in line:
			
			' '.join(line.split())
			(type, strike, month, qty) = line.split("|")			
			key = strike + type
			#cont_dict[key] = qty
			cont_dict[key] = cont_dict.get(key, 0) + int(qty)

for key in cont_dict.keys():
	print(key, "=>", cont_dict[key])