balance = 70000

def bank_transaction():
    question = input("What would you like to do - deposit, withdraw, check_balance")
    if(question == "deposit"):
        print("How much would you like to deposit?")
    elif(question == "withdraw"):
        print("How much would you like to withdraw?")
    elif(question == "check_balance"):
        print("Your balance is {} today".format(balance))

bank_transaction()
_____________________________________________
print("Welcome to Zero Interest bank.")
​
balance = '5000'
​
def transact(balance):
    print('Your current balance is')
    print('$' + balance)
    action = input('What would you like to do? (deposit, withdraw, check_balance) ')
    if action == 'deposit':
        deposit = input('How much would you like to deposit? ')
        print('Deposited $' + deposit + ' into your account')
        balance = int(balance) + int(deposit)
    elif action == 'withdraw':
        withdraw = input('How much would you like to withdraw from your account? ')
        print('Withdrew $' + withdraw + ' from your account')
        balance = int(balance) - int(withdraw)
    elif action == 'check_balance':
        balance = balance
    else:
        print('Sorry, we cannot do that')
        return
    print('Your current balance is')
    print(balance)
    done = input('Are you done yet? (yes or no) ')
    if done == 'yes':
        print('Ok!')
    else:
        print('Too bad, next!')
        
transact(balance)
​
print("Have a nice day!")
_____________________________________________



balance = 150000
done = "no"
def bank_balance(balance):
    global done
    while (done != "yes"):
        print(f"Your current balance is {balance}")
        what_it_do = input("What would you like to do: ")
        if (what_it_do == "deposit"):
            deposit_in = input("How much would you like to deposit: ")
            new_balance = balance + int(deposit_in)
            done = input("Are you done?\n")
            if (done == "no"):
                bank_balance(new_balance)
                f"Your balance after deposit: {new_balance}"
        elif (what_it_do == "withdraw"):
            withdraw_in = input("How much would you like to withdraw: ")
            new_balance = balance - int(withdraw_in)
            done = input("Are you done?\n")
            if (done == "no"):
                bank_balance(new_balance)
                f"Your balance after withdrawal is: {new_balance}"
        elif (what_it_do == "check_balance"):
            done = input("Are you done?\n")
            if (done == "no"):
                bank_balance(new_balance)
                f"Your current balance is: {balance}"
    if (done == "yes"):
        return new_balance
print(bank_balance(balance))