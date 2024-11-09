bill_amt=int(input("Enter the total bill amount\t"))
tip_perc=int(input("Enter the percentage u want to give the waiter\t"))
def total_bill(bill_amt , tip_perc):
    total_bill=(bill_amt*tip_perc/100)+bill_amt
    print("The total bill needed to be paid is" , total_bill)

total_bill(bill_amt,tip_perc)