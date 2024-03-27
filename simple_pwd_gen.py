import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 12

pwd = "".join(random.sample(total,length))
print(f'Your generated password is {pwd}.')
