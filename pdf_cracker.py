import pikepdf
from termcolor import colored
from datetime import timedelta
from time import time


file = open("yourpasswordlist.txt")

count = 1
start = time()

for password in file:
    try:
        count += 1
        with pikepdf.open("locked.pdf", password.strip()) as pdf:
            print(colored("Password found: {}".format(password), 'green'),
            f"Attempts: {count}  |  Elapsed Time: {timedelta(seconds=time()-start)}", '-'*88)
            break
    
    except:
        print(colored("Trying password: {}".format(password), 'red'))
        continue
