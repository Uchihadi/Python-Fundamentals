#lex_auth_012693788748742656146

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount = 0
    bank_emi_expected = 0
    eligible_loan_amount = 0
    
    #Start writing your code here
    if len (account_number) != 4:
        print ("Invalid account number")
    else:
        if loan_type == "Car" and customer_emi_expected <= 36 and salary > 25000 and loan_amount_expected <= 500000:
            print("Account number:", account_number)
            print("The customer can avail the amount of Rs.", 500000)
            print("Eligible EMIs :", 36)
            print("Requested loan amount:",loan_amount_expected )
            print("Requested EMI's:",customer_emi_expected)
        elif loan_type=="Car" and customer_emi_expected <= 36 and salary <= 25000 and loan_amount_expected <= 500000:
            print("Invalid loan type or salary")
            
    
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)