cat example_tx2.py 
from cosmospy import Transaction
from cosmospy import BIP32DerivationError, seed_to_privkey
from concurrent.futures import ThreadPoolExecutor
import requests
import httpx

threads = 1
headers = {"accept": "application/json", "Content-Type": "application/json"}
url_lcd = "http://localhost:1317/auth/accounts/bcna1tqywev6xmvrnagfq57c0h5susdy3l789rumufz"


#bcna1tqywev6xmvrnagfq57c0h5susdy3l789rumufz
seed = (
    "ask ------ drive ------- video embrace inquiry endorse merit faith retire clip romance range already idea tape rare useless giant evolve resemble token faint"
)
try:
    privkey_seeds = seed_to_privkey(seed, path="m/44'/118'/0'/0/0")
except BIP32DerivationError:
    print("No valid private key in this derivation path!")




def req_get(url: str):
    try:
        req = requests.get(url=url, headers=headers)
        if req.status_code == 200:
            return req.json()

    except (RequestException, Timeout) as reqErrs:
        print(f'req_get ERR: {reqErrs}')

def main():

    account_info = req_get(url_lcd)


    tx = Transaction(
        #privkey=bytes.fromhex(privkey_seeds),
        privkey=privkey_seeds,
        account_num=int(account_info["result"]["value"]["account_number"]),
        sequence=int(account_info["result"]["value"]["sequence"]),
        fee=500000,
        gas=11800000,
        memo="Spam!",
        chain_id="bitcanna-testnet-3",
        sync_mode="async",
)

    for i in range(100): #Number of messages by TX
        tx.add_transfer(recipient="bcna1e3dg9wpxq9gkygdfessy8mwfs2cka6uqfy3345", amount=1)

    pushable_tx = tx.get_pushable()


# Optionally submit the transaction using your preferred method.
# This example uses the httpx library.

    api_base_url1 = "http://localhost:1317"
    api_base_url2 = "http://seed2.bitcanna.io:1317"

    r = httpx.post(api_base_url1 + "/txs", data=pushable_tx)
    print (r.status_code)
    print (r.text)

# thread pool loop
#while True:
with ThreadPoolExecutor(max_workers=threads) as executor:
    [executor.submit(lambda: main()) for i in range(threads)]
