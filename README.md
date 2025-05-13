🚀 MAC Forgery Attack Demonstration: Securing the Future of Data Integrity
🌟 Project Vision
Welcome to our cutting-edge demonstration of a Message Authentication Code (MAC) forgery attack, crafted for the Data Integrity and Authentication course at Alexandria National University. This project showcases our team's expertise in tackling real-world cybersecurity challenges with precision and innovation. By exposing the vulnerabilities of naive MAC constructions and delivering a robust HMAC-based solution, we empower systems to stay one step ahead of cyber threats. Our work reflects a strategic blend of technical mastery and forward-thinking problem-solving, designed to impress and inspire.
Crafted by Visionaries:

Mohammed Abdulrahman Awad Khaled (ID: 2205114)
Mohammed Ahmed Ramadan Al-Arjawi (ID: 2205043)
Omar Ahmed Hameed Mohammed (ID: 2205213)

Guided by Excellence: Dr. Maged AbdelatySubmission Date: May 16, 2025
🔒 Why This Matters
In today's digital landscape, ensuring data integrity and authenticity is non-negotiable. Our project dives deep into the mechanics of a length extension attack, revealing how insecure MAC implementations can be exploited. By demonstrating this vulnerability and countering it with a state-of-the-art HMAC solution, we provide a blueprint for building secure systems that protect sensitive transactions—like amount=100&to=alice—from malicious tampering. This is not just an academic exercise; it's a strategic investment in the future of cybersecurity.
📂 Project Components



Component
Purpose



server.py
Simulates an insecure server using `MD5(secret


client.py
Executes a sophisticated length extension attack to forge a valid MAC for an extended message.


🛠️ Setup for Success
To replicate our groundbreaking work, ensure the following:

Environment: Python 3.6+ 🐍
Dependency: Install pycryptodome for cryptographic excellence:pip install pycryptodome



🚀 How to Launch

Ignite the Insecure Server:Run server.py to witness the vulnerability in action:
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


Unleash the Attack:Execute client.py to forge a MAC with surgical precision:
python client.py

Expected Output:
Forged Message: b'amount=100&to=alice\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00X\x01\x00\x00\x00\x00\x00\x00&admin=true'
Forged MAC: ec4488b7e7bd24418b8ab38b6e5ae927



🧠 The Genius Behind the Attack
Our length extension attack leverages the Merkle-Damgård construction of MD5, turning a weakness into an opportunity for learning. Starting with a valid MAC pair (amount=100&to=alice, 614d28d808af46d3702fe35fae67267c), we:

Strategically assume a 16-byte secret key length.
Compute precise MD5 padding to align with the original message's length.
Use the original MAC as the MD5 state, extending it with padding and the payload &admin=true.
Generate a forged MAC that deceives the insecure server, proving the attack's success.

This isn't just code—it's a masterclass in exploiting vulnerabilities with elegance and precision.
💡 Strategic Insights

Impact: The attack exposes the fragility of MAC = MD5(secret || message), a critical lesson for securing real-world systems.
Innovation: Our use of pycryptodome ensures compatibility and reliability, showcasing our commitment to cutting-edge tools.
Next Steps: See our secure implementation in secure_server.py, where HMAC shuts down this attack with unyielding strength.

🔮 What's Next?
Our team is poised to redefine cybersecurity standards. This project is a stepping stone to building systems that are not just secure but unbreakable. Stay tuned for our mitigation deliverable, where we deploy HMAC to fortify data integrity and set a new benchmark for excellence.
Invest in Security. Invest in Us.
