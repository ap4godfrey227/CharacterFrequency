import argparse
import string

ciphertext = open("ciphertext.txt", "rb").read()

#create an array where each index represents the frequency of each ASCII char (from A to Z)

arr_charFreq = [0] * 26

print("The text is " + str(len(ciphertext)) + " characters long")

for i in range(0, len(ciphertext)):
    if chr(ciphertext[i]) in string.ascii_uppercase:
            c = ciphertext[i]  #int(ciphertext[i], 2)
            index = c % 65
            arr_charFreq[index] = arr_charFreq[index] + 1

for i in range(0, 26):
    print("There are " + str(arr_charFreq[i]) + " " + str(chr(i+65)) + "\'s in the file")

print("\n")
print("Percentages of the letters are as follows: \n")

for i in range(0, 26):
    print(str(chr(i+65)) + " = " + str(float(arr_charFreq[i]/len(ciphertext) * 100)) + "%")
