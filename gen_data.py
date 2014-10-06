 #/usr/bin/python

cont_dict = {}

with open("cont.txt", "r") as file:

	for line in file:
		if "|" in line and "sh" not in line:
		
			' '.join(line.split())
			(type, strike, month, qty) = line.split("|")
			key = strike + type
			cont_dict[key] = cont_dict.get(key, 0) + int(qty)

	print("")

	for key in sorted(cont_dict):
		print(("%s  =>  % d") % (' '.join(key.split()), int(cont_dict[key])))

	print("\n")

def exp_calls():
	net_cal_val = 0
  
	for key in cont_dict.keys():
		if "CE" in key:
	
			' '.join(key.split())
			(strike, type) = key.split()
			qty = cont_dict[key]
			
			deno = int(strike)
			con_val = deno * qty
			cls_val = close * -qty
			dif_val = con_val + cls_val

			if (qty > 0):
				if (close > deno):
					net_val = -dif_val
				else:
					net_val = 0
			else:
				if (close > deno):
					net_val = -dif_val
				else:
					net_val = 0
					
			net_cal_val += net_val

	return(net_cal_val)

def exp_puts():
	net_put_val = 0

	for key in cont_dict.keys():
		if "PE" in key:

			' '.join(key.split())
			(strike, type) = key.split()
			qty = cont_dict[key]
			
			deno = int(strike)
			con_val = deno * qty
			cls_val = close * -qty
			dif_val = con_val + cls_val

			if (close > deno):
				net_val = 0
			else:
				net_val = dif_val;
				
			net_put_val += net_val

	return(net_put_val)


for close in range(7500, 8500, 50):

	net_value = 0
	
	net_cal_value = exp_calls()
	net_put_value = exp_puts()

	if not net_cal_value:
		net_cal_value = 0
		
	if not net_put_value:
		net_put_value = 0
		
	net_value = net_cal_value + net_put_value

	print("close = ", close, "\tNet Value: ", net_value)
