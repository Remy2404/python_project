import itertools as its

# a set of password characters
words = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+=-"
# random combination of 8 characters
r = its.product(words, repeat=8)

with open("pwd.txt", "w") as dic:
    for i in r:
        dic.write("".join(i))
        dic.write("\n")
        dic.close()