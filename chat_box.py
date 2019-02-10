from nltk.chat.util  import Chat,reflections
pairs = [
[
    r"Where did i go",
    ["You went to Shimoga",]
],
[
    r"Hii I am (.*)",
    ["Hello %1 How are you doing today??" ],
],
[
    r"How are you doing??",
    ["I am doing Good,Thank you"],
],
[
    r"quit",
    ["Bye take care"]
],
]
myreflection ={
"go":"went"
}

def chatty():
    print("Hi I am Chatty,You can chat with me.Say quit to exit")
    chat = Chat(pairs,reflections)
    chat.converse()

if __name__ == "__main__"    :
    chatty()
