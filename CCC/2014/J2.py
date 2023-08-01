input()
vote = input()
if vote.count("A") > vote.count("B"):
    print("A")
elif vote.count("B") > vote.count("A"):
    print("B")
else:
    print("Tie")
