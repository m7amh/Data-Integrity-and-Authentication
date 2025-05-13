# secure_server.py
import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_hmac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

def verify_hmac(message: bytes, mac: str) -> bool:
    expected = generate_hmac(message)
    return hmac.compare_digest(expected, mac)

def main():
    # رسالة أصلية
    message = b"amount=100&to=alice"
    mac = generate_hmac(message)

    print("=== Secure Server Simulation ===")
    print(f"Original message: {message.decode()}")
    print(f"HMAC: {mac}")

    print("\n--- Verifying legitimate message ---")
    if verify_hmac(message, mac):
        print("✅ HMAC verified successfully. Message is authentic.\n")

    # رسالة مزورة من attack.py
    forged_message = b"amount=100&to=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x01\x00\x00\x00\x00\x00\x00&admin=true"
    forged_mac = "ec4488b7e7bd24418b8ab38b6e5ae927"

    print("--- Verifying forged message with HMAC ---")
    if verify_hmac(forged_message, forged_mac):
        print("❌ Forgery succeeded unexpectedly!")
    else:
        print("✅ Forgery detected and rejected!")

if __name__ == "__main__":
    main()