from nltk.chat.util  import Chat,reflections
pairs = [
[
    r"Where did i go",
    ["You went to Shimoga",]
],
[
    r"quit",
    ["Bye take care"]
],
]
print(reflections)

myreflection ={
"go":"went"
}

def chatty():
    print("Hi I am chatbox type quit exit")
    chat = Chat(pairs)
    chat.converse()

if __name__ == "__main__"    :
    chatty()
