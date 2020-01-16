def basic():
    for x in range(0, 151, 1):
        print(x)
# basic()

def mult_5():
    for x in range(5, 1001, 5):
        print(x)
# mult_5()

def the_dojo():
    for x in range(1, 101):
        if x % 10 == 0:
            print("Coding Dojo")
        elif x % 5 == 0:
            print("Coding")
        else: print(x)

# the_dojo()

def woah_huge():
    final = 0
    for x in range(0, 500001, 1):
        if x % 2 != 0:
            final += x
    print(final)

# woah_huge()

def countdown():
    for x in range(2018,0,-4):
        if x % 2 == 0:
            print(x)

# countdown()

def flexible_count(lowNum, highNum, mult):
    for x in range(lowNum, highNum + 1):
        if x % mult == 0:
            print(x)

# flexible_count(2, 9, 3)
