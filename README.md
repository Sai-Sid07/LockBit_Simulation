# LockBit 2.0 Ransomware

Simulation and Implementation of LockBit 2.0 for Computer Security Case Study.

## Description

This project simulates the LockBit 2.0 ransomware in a simple way by running a python script and encrypting all the files in the directory using AES256 and a 16-byte initialization vector. Once the files are encrypted, it simulates the actual action of a LockBit attack by creating a README file containing all the necessary instructions to get the decryption key to retrieve the data. Once the decryption program is also executed, the encrypted files get decrypted and we get the original data with no loss.

We have also simulated our proposed solution in identifying a LockBit 2.0 attack by using the concept of entropy to check whether files have been encrypted or not.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages.

```bash
pip install python-dotenv
```
The cryptography package is used to run the encryption and decryption algorithm.
```bash
pip install cryptography
```

## Usage
### The project is divided into two parts.
### 1. Simulation of LockBit 2.0

Clone this repository and replace `user_directory` with your local directory name.

You can then delete the files with the prefix `enc_` and `dec_` in the Data directory.

Just run this following command and the files inside Data would've been encrypted.
```bash
python .\ransomeware_py.py
```

To decrypt and get back the original file content, run the following command.
```bash
python .\solution.py
```

### 2. Simulation of the proposed solution
The proposed solution uses the concept of entropy to identify the readability of a particular file.

For now, the assumption is that the files inside LockBit_2.0_Solution/Data/files are either in .txt or .csv format.

If the entropy of a particular file is very high, then the file is considered to be not readable. This could be because of 2 factors, either the file encrypted, or the file is in a different format.

Normally the entropy of a file in .txt or .csv format will be in the range 3 to 5.

An encrypted file will have an entropy around 5.8.

The entropyCalculation.py file will iterate through every file and calculate its entropy. If the entropy is found to increase, it indicates that an attack is in place and it will automatically take a backup of all files in that directory and place it in another directory called success. 

After cloning the directory, delete the success folder before running the `.py` file.

Just run the following command and a new directory called `/success` should be created.
```bash
python .\encryptioner.py
```

## Team Members

#### Members:
| S.No      | Name | Roll No     |
| :---:        |    :----:   |          :---: |
| 1.      | Pranav Deepak       | CB.EN.U4CSE20346   |
| 2.      | Raj Mota       | CB.EN.U4CSE20349   |
| 3.   | Sai Sidharth S      | CB.EN.U4CSE20352      |
| 4.      | Tejesh Kumar       | CB.EN.U4CSE20366   |
| 5.   | Uvan Shankar       | CB.EN.U4CSE20368      |

## Contributions
Pull requests are welcome. To report any bugs or fix them, please open an issue first
to discuss what you would like to change.
