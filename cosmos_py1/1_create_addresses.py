# Primero hay que crear una cuenta en keyring-test y transferir 10M de tokens
# nombrar esta cuenta como master
# bcnad keys  add master --keyring-backend test
import os

#create 1000 accounts
for i in range(1000):
	output_cmd = os.popen('bcnad keys  add account'+str(i)+' --keyring-backend test').read()
	print("Output:\n", output_cmd) 
