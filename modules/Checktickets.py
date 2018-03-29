

        
def check(numPicked, ticketPool):
    """ Requires two arguments - List of numbers picked and list of tickets
        generated. Returns number of tickets that have won """

    for ticket in ticketPool:
        if ticket.issubset(numPicked):
            won += 1
        else:
            continue
    
    return won




if __name__ == '__main__':
    check(numPicked, ticketPool)


    
    
