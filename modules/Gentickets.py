
def generate():
    """ Generates random tickets. Returns a list of tickets generated."""

    numTickets = int(input("Enter the number of tickets you wish to generate: "))
    myrange = [x for x in range(1,49)]
    ticket = []
    lot = []

    for i in  range(numTickets):
        ticket = []
        while len(ticket) < 6:
            x = random.choice(myrange)
            if x in ticket:
                continue
            else:
                ticket.append(x)
        lot.append(set(ticket))
    return lot



if __name__ == '__main__':
    pass
else:
    import random
