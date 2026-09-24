for symbol in [".","-"," ","*"]:
    if symbol==".":
        kind="dot"
    elif symbol=="-":
        kind="dash"
    elif symbol==" ":
        kind="word_gap"
    else:
        kind="unknown"
        print(symbol,kind)

grade=input("enter a grade: ")
if (int(grade) > 90):
    print("A")