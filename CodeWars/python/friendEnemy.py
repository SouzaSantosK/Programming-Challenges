# Friend or Enemy: https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

def friend(x):
    shouldbe = []
    for name in x:
        if len(name) == 4:
            shouldbe.append(name)
    return shouldbe


print(friend(["Ryan", "Kieran", "Jason", "Você"]))

# Outra solução:


def friend2(x):
    # shouldbe = [name for name in x if len(name) == 4]
    # return shouldbe
    return [name for name in x if len(name) == 4]


print(friend2(["Ryan", "Kieran", "Jason", "Você"]))
