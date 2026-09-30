
# OTP Encryption & Digital Harassment Protection System

A Python-based communication security system designed to authenticate users via time-bound hashed OTPs, detect harassment/toxic patterns in incoming messages, and securely encrypt communication payloads.

---

## 📁 Project Structure

- `otp_security_system.py`: Contains the core `SecurityPipeline` class handling SHA-256 hashed OTP validation, keyword-based harassment filtering, and XOR/Base64 message payload encryption.

---

## ⚙️ Features

1. **SHA-256 OTP Verification:** Generates a 6-digit random token and verifies against a SHA-256 cryptographic hash with automatic expiration.
2. **Digital Harassment Prevention:** Scans text input against flagged abusive or threatening patterns before transmission.
3. **Payload Encryption:** Encrypts user messages before transmission across insecure channels to prevent snooping or tampering.

---

## 🚀 How to Run

No external third-party libraries required. Uses standard Python 3:

```bash
python otp_security_system.py
