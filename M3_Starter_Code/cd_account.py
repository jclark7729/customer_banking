"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_CD_account(balance, interest_rate, months):
    CD_account = CD_account(balance, interest_rate)
    CD_account.add_interest(months)
    return CD_account

    """Creating an Account class with methods"""
    def __init__(self, balance, interest_rate, initial_interest=0): 
        self.balance = balance
        self.interest_rate = interest_rate 
        self.interest = initial_interest 

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    # This method to update the balance to add interest earned.
    def update_balance(self, interest_earned):
        """Updates the account balance by adding the interest earned."""
        self.balance += interest_earned  
        return self.balance 
    
    # Define 'apr', 'months'
    apr = 5
    months = 12
    
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account_class = Account(initial_balance, o)
    account_class.set_interest(initial_interest)
    interest_rate = account_class.interest_rate
    account_class.set_balance(initial_balance)
    account_class.update_balance(initial_interest)
    interest_earned = account_class.interest

    # Define the variables 'apr', 'months', 'interest rate before using them in the calculation
    apr = 5
    months = 12
    initial_balance = 20000
    interest_rate = 0.059
    intitial_interest = initial_balance * interest_rate * months
    print(f"Interest Earned: {initial_interest}")

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest = initial_balance * (apr/100 * months/12)

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    CD_account_balance = account_class.update_balance(interest)

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    account_class.set_balance(CD_account_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    return_interest = account_class.interest

    # Return the updated balance and interest earned.
    return_balance = account_class.update_balance(0)
    print(f"The updated balance is {updated_balance} and the interest earned is {interest_earned}")

  

