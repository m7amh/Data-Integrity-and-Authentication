# 🔐 MAC Forgery Attack Simulation

**Fortifying Data Integrity in the Digital Era**

---

## 🎯 Overview

This project demonstrates how insecure MAC constructions using MD5 can be exploited via a **Length Extension Attack**, and how this vulnerability can be mitigated with a secure HMAC-based solution. It’s a practical case study developed as part of the *Data Integrity and Authentication* course at Alexandria National University, showcasing both offensive and defensive security in action.

> **We don’t just expose the weakness — we build the fix.**

---

## 🧠 Team Behind the Code

* **Mohammed Abdulrahman Awad Khaled** (ID: 2205114)
* **Mohammed Ahmed Ramadan Al-Arjawi** (ID: 2205043)
* **[Omar Ahmed Hameed Mohammed](https://github.com/Magical1337)** (ID: 2205213)

**Supervised by:** Dr. Maged Abdelaty
📅 **Submission Date:** May 16, 2025

---

## 🧩 Project Structure

| File Name                 | Purpose                                                                |   |            |
| ------------------------- | ---------------------------------------------------------------------- | - | ---------- |
| `server.py`               | Simulates an insecure server using \`MD5(secret                        |   | message)\` |
| `client.py`               | Launches a length extension attack to forge a valid MAC                |   |            |
| `secure_server.py`        | Provides a secure implementation using **HMAC** to mitigate the attack |   |            |
| `Background Write-Up.pdf` | Theoretical explanation of the attack and its mechanics                |   |            |
| `Mitigation Write-Up.pdf` | Technical analysis of secure alternatives using HMAC                   |   |            |

---

## ⚙️ Requirements

* **Python 3.6+**
* **Dependencies:**
  Install cryptographic library:

```bash
pip install pycryptodome
```

---

## 🚀 How to Run

### 1. Launch the Insecure Server

```bash
python server.py
```

**Expected Output:**

```
Original message: amount=100&to=alice
MAC: 614d28d808af46d3702fe35fae67267c
...
MAC verification failed (as expected).
MAC verification succeeded (attack succeeded).
```

---

### 2. Execute the Forgery Attack

```bash
python client.py
```

**Expected Output:**

```
Forged Message: b'amount=100&to=alice...[padding]...&admin=true'
Forged MAC: ec4488b7e7bd24418b8ab38b6e5ae927
```

✅ The forged message is accepted by the insecure server — attack successful.

---

## 🧠 Attack Logic Explained

This is a textbook **Length Extension Attack** that exploits the internal structure of the MD5 hash function, which follows the **Merkle–Damgård construction**. Here's what we do:

1. Start with a valid message and its MAC (e.g., `amount=100&to=alice`)
2. Assume a key length (e.g., 16 bytes)
3. Apply MD5-compatible padding
4. Continue hashing with `&admin=true`
5. Recreate a valid forged MAC without knowing the secret key

> This is a demonstration of **cryptographic exploitation with mathematical precision**.

---

## 🔐 The Fix: Secure Implementation with HMAC

HMAC solves the problem by introducing a fundamentally different construction:

* Immune to length extension
* Relies on inner and outer padding with the secret key
* Supported by all modern cryptographic libraries

Check the secure implementation in `secure_server.py`.

---

## 📈 Real-World Applications

This demonstration maps directly to real-world systems:

* 💳 **Fintech Transactions:** Protect financial data from tampering
* 📡 **IoT Commands:** Ensure device integrity and trust
* 🔐 **API Security:** Prevent forged requests and injections
* 🏥 **Healthcare Systems:** Safeguard patient records and medical logs

---

## 🌟 Why This Project Matters

* ✅ **Realistic Threat Simulation**
* ✅ **Educational Value**
* ✅ **Hands-on Defensive Techniques**
* ✅ **Easily Extendable to SHA-1, SHA-256, etc.**

> We don’t just stop at proof-of-concept — we deliver secure, production-ready alternatives.

---

## 🤝 Let’s Build Secure Systems Together

We're open to collaboration, integration, and research partnerships. Whether you're in education, software development, or cybersecurity consulting, this project serves as a launchpad for better systems.

---

📂 **GitHub Repo:** [github.com/m7amh/Data-Integrity-and-Authentication](https://github.com/m7amh/Data-Integrity-and-Authentication)

---

> “Hackers find flaws. Professionals patch them. Visionaries prevent them.”
