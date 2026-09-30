"""
OTP Encryption & Digital Harassment Protection System
Author: Sumeeth
Description: Implements secure dynamic OTP verification, encrypted message dataflow,
and harassment/toxic content detection to secure user communications.
"""

import time
import random
import hashlib
import base64

class SecurityPipeline:
    def __init__(self):
        # Sample blacklisted toxic keywords for digital harassment prevention
        self.flagged_words = ["harass", "threat", "abuse", "kill", "idiot", "spam"]
        self.active_otps = {}

    def generate_otp(self, user_id, expiry_seconds=60):
        """Generates a secure 6-digit OTP with time-based validity"""
        otp = str(random.randint(100000, 999999))
        expiry_time = time.time() + expiry_seconds
        
        # Store hashed OTP for security
        hashed_otp = hashlib.sha256(otp.encode()).hexdigest()
        self.active_otps[user_id] = {
            "hash": hashed_otp,
            "expiry": expiry_time
        }
        return otp

    def verify_otp(self, user_id, input_otp):
        """Verifies the OTP against stored hash and checks expiry"""
        if user_id not in self.active_otps:
            return False, "User verification record not found."
            
        record = self.active_otps[user_id]
        if time.time() > record["expiry"]:
            del self.active_otps[user_id]
            return False, "OTP has expired. Please request a new one."
            
        hashed_input = hashlib.sha256(input_otp.encode()).hexdigest()
        if hashed_input == record["hash"]:
            del self.active_otps[user_id]
            return True, "Identity verified successfully!"
        else:
            return False, "Invalid OTP provided."

    def detect_harassment(self, message):
        """Audits text content to prevent harassment and abuse"""
        lowered_msg = message.lower()
        found_keywords = [word for word in self.flagged_words if word in lowered_msg]
        
        if found_keywords:
            return True, found_keywords
        return False, []

    def encrypt_message(self, message, secret_key):
        """Encrypts sensitive communication payload using XOR-Base64 pipeline"""
        encrypted_chars = []
        for i, char in enumerate(message):
            key_char = secret_key[i % len(secret_key)]
            encrypted_chars.append(chr(ord(char) ^ ord(key_char)))
        encrypted_text = "".join(encrypted_chars)
        return base64.b64encode(encrypted_text.encode('utf-8')).decode('utf-8')

    def decrypt_message(self, cipher_text, secret_key):
        """Decrypts the cipher text payload back to readable string"""
        try:
            decoded_text = base64.b64decode(cipher_text.encode('utf-8')).decode('utf-8')
            decrypted_chars = []
            for i, char in enumerate(decoded_text):
                key_char = secret_key[i % len(secret_key)]
                decrypted_chars.append(chr(ord(char) ^ ord(key_char)))
            return "".join(decrypted_chars)
        except Exception:
            return "Decryption Error: Invalid key or corrupted payload."


# ── Interactive Demonstration ──────────────────────────────────────────
if __name__ == "__main__":
    app = SecurityPipeline()
    print("=" * 60)
    print("🛡️  OTP ENCRYPTION & DIGITAL HARASSMENT PROTECTION SYSTEM  🛡️")
    print("=" * 60)

    # 1. OTP Verification Flow
    user = input("\nEnter User ID (e.g., sumeeth@test.com): ").strip()
    generated_code = app.generate_otp(user)
    print(f"[System] Generated 6-digit OTP: {generated_code} (Valid for 60 seconds)")

    entered_otp = input("Enter OTP to verify authentication: ").strip()
    success, status = app.verify_otp(user, entered_otp)
    print(f"Status: {status}")

    if not success:
        print("Authentication failed. Pipeline terminating.")
        exit()

    # 2. Harassment Filter Check
    print("\n--- Secure Messaging Channel ---")
    user_msg = input("Type a message to transmit: ")
    is_toxic, detected = app.detect_harassment(user_msg)

    if is_toxic:
        print(f"\n⚠️ SECURITY ALERT: Message blocked! Harassment keywords detected: {detected}")
    else:
        # 3. Payload Encryption
        key = "Secr3tK3yPass"
        cipher = app.encrypt_message(user_msg, key)
        print(f"\n🔒 Transmitted Ciphertext: {cipher}")

        # Decryption check
        decrypted = app.decrypt_message(cipher, key)
        print(f"🔓 Decrypted Verification: {decrypted}")

    print("\nWorkflow completed successfully.")
