# Written by: Yuval Quina
# This script was written in order to reveal the credentials of the Fortress CTF challenge of THM
# This script is intended to be run on python version 2.x
from Crypto.Util.number import long_to_bytes
s = input("Enter the credentials in their Non-transparent representation (the long format):")
s = long_to_bytes(s).decode('utf-8')
print("The credential as a string is: " + s)
