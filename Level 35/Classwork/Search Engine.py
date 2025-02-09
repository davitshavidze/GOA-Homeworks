
text = input("Enter a text: ")

word = input("Enter a word: ")

def search():
    if word in text:
        print("Word Found")
    else:
        print("Word Not found")

search()