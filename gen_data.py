#/usr/bin/python

cont_dict = {}

with open("cont.txt", "r") as file:

	for line in file:
		if "|" in line and "sh" not in line:
			
			' '.join(line.split())
			(type, strike, month, qty) = line.split("|")			
			key = strike + type
			cont_dict[key] = cont_dict.get(key, 0) + int(qty)

for key in cont_dict.keys():
	print(key, "=>", cont_dict[key])
	
close = 7800
print("\nclose: ", close)

def exp_calls():
	print("\nExpiring Calls\n")
  
	for key in cont_dict.keys():
		if "CE" in key:
		
			' '.join(key.split())	
			(strike, type) = key.split()
			qty = cont_dict[key]
			
			deno = int(strike)
			con_val = deno * qty
			cls_val = close * -qty
			dif_val = con_val + cls_val
			
			#print(dif_val)
			
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
					
			print(strike, "=>", qty, "\t", "Exp Val:", net_val)
			

def exp_puts():
	print("\nExpiring Puts")
	
	for key in cont_dict.keys():
		if "PE" in key:
		
			' '.join(key.split())	
			(strike, type) = key.split()
			qty = cont_dict[key]
			
			deno = int(strike)
			con_val = deno * qty
			cls_val = close * -qty
			dif_val = con_val + cls_val
			
			#print(dif_val)
			
			if (close > deno):
				net_val = 0
			else:
				net_val = dif_val;
				
			print(strike, "=>", qty, "\t", "Exp Val:", net_val)


def exp_futs():
	print("\nExpiring Futures")
  
exp_calls()
exp_puts()
#exp_futs()