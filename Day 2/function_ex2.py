#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    adult_rate = 37550.0
    child_rate = adult_rate / 3
    adult_tix = no_of_adults * adult_rate
    child_tix = no_of_children * child_rate
    tax = (adult_tix + child_tix)*0.07
    cost = adult_tix + child_tix + tax    
    
    # Using the formatting below turns the float into string
    # Do not format if you wish to keep it as a float
    total_ticket_cost = "{:.2f}".format(0.9 * cost) 
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost = calculate_total_ticket_cost(5, 2)
print("Total Ticket Cost:", total_ticket_cost)