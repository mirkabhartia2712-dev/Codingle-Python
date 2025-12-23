print ("Hello, I am Mirka's AI bot. What is your name?")
name=input()
print (f"Nice to meet you,{name}!")
print ("How are you feeling today: good/bad?")
mood= input().lower()
if mood=="good":
    print ("I'm so glad to hear that!")
elif mood=="bad":
    print ("I'm sorry to hear that. I hope you feel better soon!")
else:
    print ("I understand, feelings can pften be hard to express easily.")
print (f"It was nice meeting you {name}. Goodbye!")