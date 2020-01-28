import User

user1 = User.User()
user2 = User.User()


def main():
    print("______________ Starting Transmission ________________")
    start_transmission = user2.start_transmission()
    if start_transmission:
        public_key = user1.get_public_key()
        print("  Generating RSA public key... " + str(public_key))
        vigenere_key = user2.generate_vigenere_key()
        print("  Generating Vigenere key... " + str(vigenere_key))
        encrypted_key_rsa = user2.encrypt_rsa(vigenere_key,  public_key)
        print("  Encrypted RSA message... " + str(encrypted_key_rsa))
        print("______________________________________________________\n")
        if user1.decrypt_rsa(encrypted_key_rsa):
            encrypted_text_vigenere = user2.encrypt_text_vigenere()
            print("______________________________________________________")
            print("  Encrypted Vigenere message... " + str(encrypted_text_vigenere))
            decrypted_vigenere_text = user1.decrypt_text_vigenere(encrypted_text_vigenere)
            print ("  Decrypted Vigenere message: " + decrypted_vigenere_text)

if __name__== "__main__":
 main()