import hmac
import hashlib


secret_key = b"gmiumysecretkey"


message = input("Enter Message: ").encode()

mac = hmac.new(
    secret_key,
    message,
    hashlib.sha256
).hexdigest()

print("\nGenerated MAC:", mac)


received_message = input("\nEnter Message For Verification: ").encode()

verify_mac = hmac.new(
    secret_key,
    received_message,
    hashlib.sha256
).hexdigest()

if hmac.compare_digest(mac, verify_mac):
    print("\nMessage Authenticated Successfully")
    print("Integrity Maintained")
else:
    print("\nAuthentication Failed")
    print("Message Tampered")
