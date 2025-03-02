import random

def generator(text, sep, option = None):
    if not isinstance(text, str) or not isinstance(sep, str) or sep == "":
        yield("ERROR")
        return
    if option == None:
        txt = text.split(sep)
        for x in txt:
            yield(x)
    elif option == "ordered":
        txt = sorted(text.split(sep))
        for x in txt:
            yield(x)
    elif option == "unique":
        txt = list(dict.fromkeys(text.split(sep)))
        for x in txt:
            yield(x)
    elif option == "shuffle":
        txt = sorted(text.split(sep), key=lambda x: random.random())
        for x in txt:
            yield(x)
    else:
        yield("ERROR")
        return
        
if __name__ == "__main__":
    text = "Le Lorem Ipsum est simplement du faux texte."

    for word in generator(text, sep=" ", option="shuffle"):
        print(word)
    print("**********************************************")
    for word in generator(text, sep=" ", option="unique"):
        print(word)
    print("**********************************************")
    for word in generator(text, sep=" ", option="ordered"):
        print(word)
    print("**********************************************")
    for word in generator(text, sep=" "):
        print(word)
    print("**********************************************")
    for word in generator(text, sep=" ", option="none"):
        print(word)
    print("**********************************************")
    txt = 1
    for word in generator(txt, sep=" ", option="ordered"):
        print(word)