import requests
import string
import random

print("Ghostbin Searcher by Flamestyx#2076")

abc = "abcdefghijklmnopqrstuvwxyz1234567890"

def id_generator(size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

while(True):
    link = id_generator(8, abc)
    link1 = ("https://ghostbin.com/62dbb" + link + "/raw")
    f = open("bad.txt", "r")
    e = open("bad.txt", "a")
    q = open("good.txt", "a")
    data = f.read()
    if link1 in data:
        print("Duplicate Link Found!")
    f.close
    r = requests.get(link1)
    status = r.status_code
    print(status)
    if status == 404 or 200:
        print("Bad Link found")
        e.write(link1)
        e.write("\n")
    else:
     print("Good Link Found")
     q.write(link1)
     q.write("\n")
     q.close

