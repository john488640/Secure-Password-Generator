"""函数定义"""
import secrets
import random
import string
import os
import secrets
password_character_pool = string.ascii_letters + string.digits + string.punctuation
def clear():    os.system("cls" if os.name == "nt" else "clear")
def generate_token(numeral,token_length = 8):
    global token
    clear()
    print(f"将生成一个长度为{token_length}，进制为{numeral}的token\n")
    if numeral == "byte":
        token = secrets.token_hex(token_length)
        print(token)
    elif numeral == "hex":
        token = secrets.token_hex(token_length)
        print(token)
    return token
def generate_password(password_length = 8):
    clear()
    password = ''.join(secrets.choice(password_character_pool) for i in range(password_length))
    print(f"将生成一个长度为{password_length}")
    print(password)
    return password
def pin(pin_length = 8):
    clear()
    pin_numbers_pool = string.digits
    print(f"将生成一个长度为{pin_length}的PIN")
    p_in = ''.join(secrets.choice(pin_numbers_pool) for i in range(pin_length))
    print(p_in)
    return p_in
