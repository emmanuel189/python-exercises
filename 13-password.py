import random
c = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!-#$%&/()=?¿[]{}"
p = random.sample(c, 16)
pw = ""
for i in range(len(p)):
    pw += p[i]
print("Password:", pw)
