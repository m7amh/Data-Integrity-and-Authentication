# 🚀 MAC Forgery Attack Demo

**Securing the Future of Data Integrity**

---

## 🌍 Vision-Driven Cybersecurity

Welcome to a live demonstration of how **weak MAC constructions** can collapse under modern cryptographic attacks—and how we fix them.
This project was developed for the **Data Integrity and Authentication** course at *Alexandria National University*, blending **real-world security challenges** with **cutting-edge countermeasures**.

> **Bottom Line:** We don't just break things. We secure them better.

---

### 👨‍💻 Crafted by:

* **Mohammed Abdulrahman Awad Khaled** (ID: 2205114)
* **Mohammed Ahmed Ramadan Al-Arjawi** (ID: 2205043)
* **Omar Ahmed Hameed Mohammed** (ID: 2205213)

### 🎓 Supervised by:

**Dr. Maged Abdelaty**
📅 Submission: *May , 2025*

---

## 🔒 Why It Matters

In today's connected world, a forged message like:

```
amount=100&to=alice&admin=true
```

...should never be accepted as valid.

Yet many systems rely on insecure MAC constructions like:

```
MAC = MD5(secret || message)
```

This project proves how that approach **fails under attack**, and how **HMAC** saves the day.

---

## 📦 Project Structure

| Component                          | Purpose                                                              |   |            |
| ---------------------------------- | -------------------------------------------------------------------- | - | ---------- |
| `server.py`                        | Simulates a server using insecure MAC logic: \`MD5(secret            |   | message)\` |
| `client.py`                        | Performs a precise length extension attack to forge a valid MAC      |   |            |
| `secure_server.py` *(coming soon)* | Reinforces the system with **HMAC**, immune to this class of attacks |   |            |

---

## ⚙️ Environment Setup

### Requirements:

* Python 3.6+
* `pycryptodome`:

```bash
pip install pycryptodome
```

---

## 🚀 How to Run

### Step 1: Launch the Insecure Server

```bash
python server.py
```

✅ You’ll see:

```
Original message: amount=100&to=alice
MAC: 614d28d808af46d3702fe35fae67267c
...
MAC verification failed (as expected).
MAC verification succeeded (attack succeeded).
```

---

### Step 2: Execute the Forgery Attack

```bash
python client.py
```

🔓 Expected output:

```
Forged Message: b'amount=100&to=alice...[padding]...&admin=true'
Forged MAC: ec4488b7e7bd24418b8ab38b6e5ae927
```

✅ *Forged message accepted by insecure server.*

---

## 🧠 How the Attack Works

* Uses the **Merkle-Damgård weakness** in MD5
* Assumes a known message and MAC
* Rebuilds internal state, appends new data (`&admin=true`)
* Computes a **valid forged MAC** without knowing the key

> It's not hacking. It's **mathematical precision**.

---

## 🔐 Our Secure Countermeasure: HMAC (in `secure_server.py`)

* HMAC resists length extension and state forgery
* Our upcoming secure implementation follows best practices from **RFC 2104**

---

## 📈 Strategic Takeaways

* **Impact**: Demonstrates real, practical risks in insecure systems
* **Solution**: Builds a bridge to secure MAC use via HMAC
* **Scalability**: Easily extendable to secure APIs, financial apps, and identity verification systems
* **Innovation**: Combines clarity, cryptographic depth, and developer usability

---

## 🌟 Beyond the Classroom

This is more than a course project. It’s a **security blueprint** for the next generation of systems.

We envision our work being integrated into:

* Fintech platforms
* IoT device firmware
* Secure messaging apps
* Compliance-oriented APIs (e.g., HIPAA, GDPR)

---

## 🤝 Join the Security Revolution

📩 **Reach out to the team** for collaboration, consultation, or integration discussions.
Let's build systems that **can't be tricked—only trusted**.

---

**🔐 Invest in Security. Invest in Us.**

---

> “Hackers find the flaw. Professionals close it. Visionaries prevent it.”
