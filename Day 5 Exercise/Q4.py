#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    price_per_litre = 70
    mileage = distance / 10
    price_litre = price_per_litre * mileage
    price_passengers = no_of_passengers * 80
    
    if price_litre > price_passengers:
        return -1
    else:
        profit = price_passengers - price_litre
        return profit
    #Remove pass and write your logic here



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))