def encrypt(text,s):
	result = ""

	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)

		else:
			result += chr((ord(char) + s - 97) % 26 + 97)

	return result

print("Roll No: 2453046\n")
text = input("enter text:")
s =  3
print ("Text : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))
