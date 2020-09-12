from encryptor import encryptor
from decryptor import decryptor
print("Do you want to encrypt or decrypt?")
usr_answer=input()
if usr_answer=="encrypt":
    print("Type your message")
    usr_input=input()
    print(f"Your text:\n {usr_input}")
    copiedtext=usr_input
    encryptor(copiedtext)
elif usr_answer=="decrypt":
    print("Type your message")
    usr_input=input()
    print(f"Your text:\n {usr_input}")
    copiedtext=usr_input
    decryptor(copiedtext)
