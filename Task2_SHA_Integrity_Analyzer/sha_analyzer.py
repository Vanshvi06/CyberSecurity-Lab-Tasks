import hashlib

# Input two messages
msg1 = input("Enter Original Message: ")
msg2 = input("Enter Modified Message: ")

def generate_hashes(message):
    print("\nMessage:", message)

    sha1 = hashlib.sha1(message.encode()).hexdigest()
    sha256 = hashlib.sha256(message.encode()).hexdigest()
    sha512 = hashlib.sha512(message.encode()).hexdigest()

    print("SHA-1   :", sha1)
    print("SHA-256 :", sha256)
    print("SHA-512 :", sha512)

print("\n--- Original Message Hashes ---")
generate_hashes(msg1)

print("\n--- Modified Message Hashes ---")
generate_hashes(msg2)

print("\nAvalanche Effect Demonstrated")
print("Small change in input causes large change in hash output.")
