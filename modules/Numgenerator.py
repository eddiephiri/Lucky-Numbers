
def draw():
    """ Generates  35 numbers between 1 to 48 inclusive. This is the list of
    numbers drawn in each game instance. Returns a set"""

    picked = []
    lot = [x for x in range(1,49)]
    while len(picked) != 35:
        num = random.choice(lot)
        if num in picked:
            continue
        else:
            picked.append(num)
            
    return set(picked)




if __name__ == '__main__':
    pass
else:
    import random
