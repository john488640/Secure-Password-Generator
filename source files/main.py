"""导入库"""
import function as f
import time
def main():
    f.clear()
    choose = input("""
        =============密码生成器==============
        1.Token生成
        2.密码生成
        3.PIN生成
        Q.退出...
        选择模式：
    """)
    if choose == "1":
        while 1 :
            numeral = input("输入进制")
            if numeral == "byte" or "hex": break
        f.generate_token(numeral,int(input("输入Token的长度")))
    elif choose == "2":
        while 1:
            password_len = int(input("输入密码长度"))
            if password_len != 0 or  password_len <= 64:break
        f.generate_password(password_len)
    elif choose == "3":
        while 1:
            pin_len = int(input("PIN长度(如果出现重复情况那么请检查输入的参数)"))
            if pin_len != 0 and pin_len <=64 : break
        f.pin(pin_len)
    elif choose == "Q" or choose == "q" or choose == "exit":
        exit()
    else:
        print("请重新输入选择！")
        time.sleep(1.5)
if __name__ == '__main__':
    main()