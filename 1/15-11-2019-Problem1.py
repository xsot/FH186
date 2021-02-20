import sys

for line in sys.stdin :
    a,b = map(str, line.split())
    if (a == "Rock" and b == "Scissors") or (a == "Scissors" and b == "Paper") or (a == "Paper" and b == "Rock") :
        print(a)
    else :
        print(b)
