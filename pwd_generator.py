import random
import math

pwd = []

def generate_pwd(length,array,is_alpha=False):
    for i in range(length):
        idx = random.randint(0,len(array)-1)
        char = array[idx]
        if is_alpha:
            case = random.randint(0,1)
            if case == 1:
                char = char.upper()
        pwd.append(char)

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
schar = "!@#$%&*"

pwd_len = int(input("Enter password length: "))

alpha_len = pwd_len//2
num_len = math.ceil(0.03*pwd_len)
schar_len = pwd_len-(alpha_len+num_len)

generate_pwd(alpha_len,alpha,True)
generate_pwd(num_len,num)
generate_pwd(schar_len,schar)

random.shuffle(pwd)

finalpwd = ""
for x in pwd:
    finalpwd = finalpwd + str(x)

print(f'Your generated password is: {finalpwd}')    