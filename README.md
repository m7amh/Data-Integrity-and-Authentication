MAC Forgery Attack Demonstration

Project Overview

This project demonstrates a length extension attack against an insecure Message Authentication Code (MAC) implementation using MD5, as part of the "Data Integrity and Authentication" course assignment. The attack forges a valid MAC for an extended message without knowing the secret key, highlighting the vulnerability of the naive MAC construction. The secure implementation using HMAC is provided separately to show mitigation.

Submitted by:





Mohammed Abdulrahman Awad Khaled (ID: 2205114)



Mohammed Ahmed Ramadan Al-Arjawi (ID: 2205043)



Omar Ahmed Hameed Mohammed (ID: 2205213)

Submitted to: Dr. Maged Abdelaty
Submission Date: May 16, 2025

Files







File



Description





server.py



Insecure server using `MD5(secret





attack.py



Performs the length extension attack to forge a MAC for an extended message.

Prerequisites





Python 3.6+



Required library: pycryptodome

pip install pycryptodome

How to Run





Run the insecure server to generate and verify MACs:

python server.py

Expected Output:

=== Server Simulation ===
Original message: amount=100&to=alice
MAC: 614d28d808af46d3702fe35fae67267c

--- Verifying legitimate message ---
MAC verified successfully. Message is authentic.

--- Verifying naive forged message ---
MAC verification failed (as expected).

--- Verifying forged message from attack ---
MAC verified successfully (attack succeeded).



Run the attack script to perform the length extension attack:

python attack.py

Expected Output:

Forged Message: b'amount=100&to=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x01\x00\x00\x00\x00\x00\x00&admin=true'
Forged MAC: ec4488b7e7bd24418b8ab38b6e5ae927

Attack Explanation

The length extension attack exploits the Merkle-Damgård construction of MD5. Given a valid MAC pair (amount=100&to=alice, 614d28d808af46d3702fe35fae67267c), the attack:





Assumes a secret key length of 16 bytes.



Computes MD5 padding for the total length (secret + message).



Uses the original MAC as the MD5 state and continues hashing with the padding and appended data (&admin=true).



Produces a forged message and MAC, which the insecure server accepts, demonstrating the vulnerability.

Notes





The attack succeeds because MAC = MD5(secret || message) exposes the hash state, enabling extension.



The forged message includes MD5 padding, which is valid but may not be practical in all scenarios.



Refer to secure_server.py in the mitigation deliverable for a secure HMAC-based implementation.
