

def result(ticketPool, numPicked, won):

    """ Displays the final results of a draw. Returns a display of the numbers
        picked, the tickets generated and the number of tickets that win. """

    print("The numbers have been drawn, the tickets have been made. The results are as follows: \n")

    print(numPicked, sep= '  ')

    print("Tickets made are as follows: \n")

    for ticket in tickets:
        print(ticket, '\n')

    print(won, " tickets have won the bet!")



if __name__ == '__main__':
    result(ticketPool, numPicked, won)
