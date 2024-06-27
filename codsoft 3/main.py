import json

with open("ai.json","r") as ai:
    ai_data=json.load(ai)

while True:
    a=input("you :").lower()
    if a in ai_data:
        print(f"AI: {ai_data[a]}")
    else:
        print("Sorry, i didn't get you can u assist me to answer that")
        b = input("you :").strip()
        ai_data[a]=b
        with open("ai.json","w") as ai:
            json.dump(ai_data,ai,indent=4)
        print("AI: Thank you! I've learned something new.")
