

        
def check(mylist, pool):
    """ Requires two arguments - List of numbers picked [mylist] and list of tickets
        generated [pool]. Returns number of tickets that have won """
    won = 0

    for ticket in pool:
        if ticket.issubset(mylist):
            won += 1
        else:
            continue
    
    return won




if __name__ == '__main__':
    check(list, pool)


    
    
