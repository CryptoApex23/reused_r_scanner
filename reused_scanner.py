import json
import requests
import sys
from tqdm import tqdm

def print_logo():
    logo = r"""
  ______   _______   __      __  _______   ________  ______  
 /      \ /       \ /  \    /  |/       \ /        |/      \ 
/$$$$$$  |$$$$$$$  |$$  \  /$$/ $$$$$$$  |$$$$$$$$//$$$$$$  |
$$ |  $$/ $$ |__$$ | $$  \/$$/  $$ |__$$ |   $$ |  $$ |  $$ |
$$ |      $$    $$<   $$  $$/   $$    $$/    $$ |  $$ |  $$ |
$$ |   __ $$$$$$$  |   $$$$/    $$$$$$$/     $$ |  $$ |  $$ |
$$ \__/  |$$ |  $$ |    $$ |    $$ |         $$ |  $$ \__$$ |
$$    $$/ $$ |  $$ |    $$ |    $$ |         $$ |  $$    $$/ 
 $$$$$$/  $$/   $$/     $$/     $$/          $$/    $$$$$$/                                                
  ______   _______   ________  __    __                      
 /      \ /       \ /        |/  |  /  |                     
/$$$$$$  |$$$$$$$  |$$$$$$$$/ $$ |  $$ |                     
$$ |__$$ |$$ |__$$ |$$ |__    $$  \/$$/                      
$$    $$ |$$    $$/ $$    |    $$  $$<                       
$$$$$$$$ |$$$$$$$/  $$$$$/      $$$$  \                      
$$ |  $$ |$$ |      $$ |_____  $$ /$$  |                     
$$ |  $$ |$$ |      $$       |$$ |  $$ |                     
$$/   $$/ $$/       $$$$$$$$/ $$/   $$/

###############################
#                             #
#        CryptoAppex          #
# BTC Reused R Value Scanner  #
#            Tool             #
#            V0.1             #
#                             #
###############################
    """
    print(logo)


def get_address_data(address):
    url = f"https://blockchain.info/rawaddr/{address}"
    response = requests.get(url)
    return response.json()

def main():
    print_logo()
    print("WELCOME TO Reused R Scanner 0.1!\n")
    
    address = input("Enter the Bitcoin address to scan: ")
    print(f"Fetching data for address: {address}")
    
    address_data = get_address_data(address)
    num_txs = address_data['n_tx']
    
    print(f"\nData for address: {address}")
    print(f"Number of transactions: {num_txs}\n")

    inputs = []
    for tx in tqdm(address_data['txs'], desc="Processing transactions", unit="tx"):
        print("#################################################################################")
        print(f"Transaction hash: {tx['hash']}")
        print(f"Number of inputs: {tx['vin_sz']}")
        
        for input_script in tx['inputs']:
            script = input_script.get('script', '')
            if script:
                inputs.append(script)
    
    print("\nComparing input scripts for reused R values...\n")
    
    alert_count = 0
    input_len = len(inputs)
    with tqdm(total=(input_len - 1) * input_len // 2, desc="Comparing inputs", unit="cmp") as pbar:
        for i in range(input_len - 1):
            for j in range(i + 1, input_len):
                if inputs[i][10:74] == inputs[j][10:74]:
                    print(f"Reused R-Value found between inputs:\n{inputs[i]}\n{inputs[j]}\n")
                    alert_count += 1
                pbar.update(1)

    if alert_count == 0:
        print("No Reused R values Found, seems safe!")
    else:
        print(f"Total reused R values found: {alert_count} Wallet is not safe!")

if __name__ == "__main__":
    main()

    sys.exit()
