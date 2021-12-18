from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Random import get_random_bytes
from Cryptodome.PublicKey import RSA

output_file = 'encrypteddor.bin' # Output file
data = b'dor the king' # Must be a bytes object
key = get_random_bytes(32) # Use a stored / generated key


cipher = AES.new(key, AES.MODE_CFB) # CFB mode
ciphered_data = cipher.encrypt(data) # Only need to encrypt the data, no padding required for this modeprint(ciphered_data)
print(ciphered_data)
file_out = open(output_file, "wb") # Open file to write bytes
file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)
file_out.write(ciphered_data) # Write the varying length ciphertext to the file (this is the encrypted data)
file_out.close()



input_file = 'encrypteddor.bin'
key1 = key # Use a stored / generated key

file_in = open(input_file, 'rb')
iv = file_in.read(16)
ciphered_data = file_in.read()
file_in.close()

cipher = AES.new(key1, AES.MODE_CFB, iv=iv)
original_data = cipher.decrypt(ciphered_data) # No need to un-pad
print(original_data)


#Generate public key and private key
# key = RSA.generate(2048)
# private_key = key.export_key()
# file_out = open("private.pem", "wb")
# file_out.write(private_key)
# file_out.close()
# print(private_key)

# public_key = key.publickey().export_key()
# file_out = open("receiver.pem", "wb")
# file_out.write(public_key)
# file_out.close()
# print(public_key)