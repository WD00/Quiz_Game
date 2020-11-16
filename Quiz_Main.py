nr1 = """What are the three colors of the RGB model?
a. red, green, blue
b. red, purple, white
c. black, white, grey
d. red, green, white
"""
nr2 = """What is the name of an English mathematician and computer scientist?
a. Joan Clarke
b. Isaac Newton
c. Plato
d. Alan Turing
"""
nr3 = """What is the parent organization of Google?
a. Youtube
b. Alphabet Inc.
c. I have no idea
d. Berkshire Hathaway
"""
nr4 = """Who was C++ designed by?
a. Bjarne Stroustrup
b. Guido van Rossum
c. James Gosling
d. Dennis Ritchie"""
nr5 = """1+1 =?
a. 1
b. 2
c. 3
d. 4"""

q = {nr1: "a", nr2: "d", nr3: "b", nr4: "a", nr5: "a"}

print("Welcome! I hope you're ready for the quiz.")
player_score = 0

for i in q:
    print(i)
    answer = input("Answer (a/b/c/d): ")
    if answer == q[i]:
        print("Correct.")
        player_score = player_score + 1
    else:
        print("Wrong.")
        player_score = player_score - 1

print("Your score:", player_score)