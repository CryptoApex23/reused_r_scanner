# BTC P2PKH Adress Reused R value Scanner

```bash
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
```

The BTC Reused R Value Scanner (R-scan) is a tool designed to detect reused R values in Bitcoin transactions. Reused R values can indicate potential security issues with the associated Bitcoin address. This script scans the transactions of a given Bitcoin address and identifies any reused R values, helping to assess the security of the address.

Telegram:
https://t.me/vertexapex_hub

Discord:
https://discord.gg/P265G7Ex

## Reused R Value Attack

In Bitcoin transactions, signatures are generated using the Elliptic Curve Digital Signature Algorithm (ECDSA). Each transaction input includes a digital signature composed of two values: `r` and `s`. These values are essential for validating and authenticating the transaction.

### What is a Reused R Value Attack?

A **reused R value attack** occurs when the same `r` value is used in multiple signatures across different transactions. This scenario poses significant security risks for several reasons:

1. **Private Key Exposure**: If an attacker observes that the same `r` value has been used in multiple signatures, they might be able to exploit this information to deduce the private key used for signing those transactions. This is because the `r` value is part of the signature and, when reused, can be used in conjunction with other known data to potentially reveal the private key.

2. **Increased Risk**: Reusing `r` values across transactions can compromise the security of the Bitcoin wallet. Attackers could exploit this vulnerability to gain unauthorized access to the wallet or steal funds.

### Why is it a Problem?

Using the same `r` value in multiple transactions can weaken the security of a wallet by exposing it to attacks. Each signature should have a unique `r` value to maintain robust security and prevent potential vulnerabilities.

### How to Avoid It?

To avoid the reused R value attack, ensure that each transaction uses a unique `r` value. Proper cryptographic practices and careful management of transaction signing processes can help mitigate this risk and keep your Bitcoin wallet secure.

## Features

- Scans transactions for reused R values
- Shows the transaction ID in which it occurred 

## Setup

### Prerequisites

Ensure you have Python 3.8 or later installed on your system.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/CryptoApex23/reused_r_scanner.git
   cd reused_r_scanner
   ```

2. **Create and activate a virtual environment:**

   ```bash
   $python -m venv venv        # Or python3
   $source venv/bin/activate   # On Windows, use `$venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt  # Or pip3
   ```

## Usage

1. **Run the script:**

   ```bash
   python partial_recovery.py # Or python3
   ```

2. **Follow the prompts:**

   - When prompted, enter the Bitcoin address you want to scan.

   Example input:

   ```bash
    Enter the Bitcoin address to scan: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
    Fetching data for address: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
   ```

   Results will be displayed in the terminal, showing any reused R values found.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. Contributions are welcome!

## Donation

Help me keep the light on and maintane all the projects <3

BTC

```bash
bc1qxwlpy6fx33e968uqhw7pr030kvyr3pel0ptxt3
```

ETH

```bash
0x8a530A5eC57d7D7944E23Ffc5D85dA09c52C8eda
```

SOL

```bash
FCfyeS5LwsjjgGiJKAikYFwPoweBcVLYASjRstEhHaAs
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
