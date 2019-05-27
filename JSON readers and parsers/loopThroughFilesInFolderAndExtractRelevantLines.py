import json
import os

listOfFiles = os.listdir("Files_to_rake_through")
print("Fadi and Olive's bizarre code: Part 1, Phantom Blood")

for file in listOfFiles:

    with open(os.path.join("Files_to_rake_through", file)) as f:
        text = f.read()
        list = text.split("\n")  
    print(f, "has been opened.")
    holder = []
    for item in list:
        # find all "subreddit":"AskMen" and "subreddit":"AskWomen"
        if ('\"subreddit\":\"AskMen\"' in item or '\"subreddit\":\"AskWomen\"' in item):
                # find all "author_flair_css_class":"male" and "author_flair_css_class":"female"
            if ('\"author_flair_css_class\":\"female\"' in item or '\"author_flair_css_class\":\"male\"' in item):
                    # append user to the dictionary with their assigned gender
                    #temp = json.loads(item)
                    holder.append(item)
    print("'holder' has been made wtih this file with a size of", len(holder))
    print("Writing to a new file now.")

    with open(os.path.join("Files_to_rake_through", (file + '-OUTPUT.txt')), "w") as file:
        for i,element in enumerate(holder):
            try:
                if i:
                    file.write("\n"+str(element))
                else:
                    file.write(str(element))
            except:
                print("Non-fatal error while saving: your bitch ass file.")

            




