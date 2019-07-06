import requests
import feedparser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# how to read a file from the web
# page = requests.get("http://google.com")
# print(page.text)

# how to read with feedparser
magazine = feedparser.parse("http://www.slate.com/all.fulltext.all.rss")


question = int(input("Choose an article to read: "))
print("You can see that article at ", magazine.entries[question].link)

print(question)

space = input("Hit key to continue ")
for i in range(len(magazine.entries)):
    if i == question:
        print("Title:" , magazine.entries[i].title)
        print("Description: ", magazine.entries[i].description)
        print(magazine.entries[i].link)
    else:
        print("* Title:", magazine.entries[i].title)
        print("Description: ", magazine.entries[i].description)
        print(magazine.entries[i].link)

