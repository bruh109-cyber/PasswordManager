from cryptography.fernet import Fernet


""" 
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key) """

def load_key():
    with open("key.key", "rb")as f:
        return f.read()


pwd = input("what is the master password? ")
  
key = load_key() + pwd.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            parts = data.split("|")
            
            
            user = parts[0]
            passw = "|".join(parts[1:])
            
            
           decrypted = fer.decrypt(passw.encode()).decode()
            
            print(f"User: {user} | Password: {decrypted}") 
   
   
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        encrypted = fer.encrypt(pwd.encode()).decode()
        f.write(f"{name}|{encrypted}\n")
        
        



while True:
    mode = input("Would you like to add a new password or vue existing ones (view, add), press q to quit?  ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue