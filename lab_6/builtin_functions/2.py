def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    print("Uppercase: ", upper)
    print("Lowercase: ", lower)

s = input()
count_case(s)
