import random


def generate():
    """ Generates random tickets. Returns a list of tickets generated."""

    num_tickets = int(input("Enter the number of tickets you (first) wish to generate: "))
    my_range = [x for x in range(1,49)]
    lot = []

    for i in range(num_tickets):
        ticket = []
        while len(ticket) < 6:
            x = random.choice(my_range)
            if x in ticket:
                continue
            else:
                ticket.append(x)
        lot.append(set(ticket))
    return lot


if __name__ == '__main__':
    pass

