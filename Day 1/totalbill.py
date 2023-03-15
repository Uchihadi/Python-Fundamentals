# Tax Bill is a percentage amount
def total_bill(bill_amt, tax):
    total_amt = bill_amt + ((tax / 100) * bill_amt)
    print(total_amt)

# (Default argument is at the end, non-default argument is at the beginning
total_bill(100, 20)