import hashpumpy
from server import verify, SECRET_KEY  # استيراد المفتاح السري من server.py

def perform_attack():
    original_message = b"amount=100&to=alice"
    original_mac = "616843154afc11960423deb0795b1e68"
    data_to_append = b"&admin=true"

    key_len = len(SECRET_KEY)  # نستخدم طول المفتاح السري الحقيقي مباشرة

    new_mac, new_message = hashpumpy.hashpump(
        original_mac,
        original_message.decode(),
        data_to_append.decode(),
        key_len
    )

    forged_message = new_message
    forged_mac = new_mac

    print(f"Using key length = {key_len}")
    if verify(forged_message, forged_mac):
        print("[+] Attack successful!")
        print("Forged message:", forged_message)
        print("Forged MAC:", forged_mac)
    else:
        print("[-] Attack failed.")

if __name__ == "__main__":
    perform_attack()
