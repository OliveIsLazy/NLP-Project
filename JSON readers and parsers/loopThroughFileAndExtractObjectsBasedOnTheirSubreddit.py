import json
import os

#listOfFiles = os.listdir("rakeme")
print("Fadi and Olive's bizarre code: Part 2, Battle Tendency")
men = []
women = []
#for i, file in enumerate(listOfFiles):
 
   
with open('FINAL-OUTPUT.txt') as f:
    #print("Dealing with file:",)
    text = f.read()
    list = text.split("\n")

for item in list:
    if ('\"subreddit\":\"AskMen\"' in item):
        men.append(item)
    else:
        women.append(item)


print("The line-size of the file is:", len(men), "and", len(women), " for men and women respectively.")
print("I'm doing creative writing...")
with open(os.path.join(('MEN-OUTPUT.txt')), "w") as file:
    for i,element in enumerate(men):
        try:
            if i:
                file.write("\n"+str(element))
            else:
                file.write(str(element))
        except:
            print("Non-fatal error while saving: your bitch ass file.")

print("Now for my magnum opus!")
with open(os.path.join(('WOMEN-OUTPUT.txt')), "w") as file:
    for i,element in enumerate(women):
        try:
            if i:
                file.write("\n"+str(element))
            else:
                file.write(str(element))
        except:
            print("Non-fatal error while saving: your bitch ass file.")
