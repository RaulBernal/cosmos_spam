import os
import time

#funds the accounts
for i in range(1000):
	output_cmd = os.popen('bcnad tx bank send $(bcnad keys show master   --keyring-backend test -a) $(bcnad keys show account'+str(i)+ '  --keyring-backend test -a) 100000000ubcna  --keyring-backend test --chain-id bitcanna-1 --node http://localhost:26657 -y --gas 200000 --gas-adjustment 1.5 --gas-prices 0.025ubcna  -y').read()
	print("Output:\n", output_cmd) 
	time.sleep(1)
