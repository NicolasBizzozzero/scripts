from simplecrypt import encrypt, decrypt
from sys import argv

file = r"C:\Users\Nicolas\Documents\passwords\passwd_sessionfac.txt"

def decrypt_from_file(hashPassword, file):
	with open(file, "r") as fileContainingPassword:
		cipherPassword = fileContainingPassword.read()
	clearPassword = cipherPassword.decrypt(hashPassword, cipherPassword)
	return clearPassword


def encrypt_to_file(clearPassword, hashPassword, file):
	cipherPassword = fileContainingPassword.encrypt(hashPassword, clearPassword)
	with open(file, "w+") as fileContainingPassword:
		fileContainingPassword.write(cipherPassword)


if __name__ == '__main__':
	#encrypt_to_file(argv[1], argv[2], argv[3])
	print("Clear password  : CoucouLesAmis")
	encrypt_to_file("CoucouLesAmis", "MONMASTERPASSWORD", file)
	with open(file, "r") as file:
		print("Cipher password : ", end="")
		file.read()
	clearPassword = decrypt_from_file("MONMASTERPASSWORD", file)
	print("Clear password  :", clearPassword)


ciphertext = encrypt('password', plaintext)
plaintext = decrypt('password', ciphertext)