import json
import os

listOfFiles = os.listdir("rake_me_harder")
print("Fadi and Olive's bizarre code: Part 3, Stardust Crusaders")
holder = []
for i, file in enumerate(listOfFiles):
    with open(os.path.join("rake_me_harder", file)) as f:
        print("Dealing with file:", file)
        text = f.read()
        list = text.split("\n")
        print("The length of this file is", len(list))
        holder += (list)  # this fucks up


print("The line-size of the file is:", len(holder))
print("I'm doing creative writing...")
with open(os.path.join(('FINAL-OUTPUT.txt')), "w") as file:
    for i,element in enumerate(holder):
        try:
            if i:
                file.write("\n"+str(element))
            else:
                file.write(str(element))
        except:
            print("Non-fatal error while saving: your bitch ass file.")
