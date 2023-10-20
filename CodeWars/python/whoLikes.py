# Who likes this? https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python

def likes(names):
    users_count = len(names)
    if users_count == 0:
        return "no one likes this"
    elif users_count == 1:
        return '{} likes this'.format(names[0])
    elif users_count == 2:
        return '{} and {} like this'.format(names[0], names[1])
    elif users_count == 3:
        return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    else:
        return '{}, {} and {} others like this'.format(names[0], names[1], len(names[2:]))

print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

# Outras soluções:

def likes2(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'


print(likes2(['Alex', 'Jacob', 'Mark', 'Max']))
# --------------------------------------------------------------------------------------------

def likes3(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


print(likes3(['Alex', 'Jacob', 'Mark', 'Max']))
