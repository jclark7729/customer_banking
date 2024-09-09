"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    interest = Account(starting_balance)
    starting_balance = float(input)

    # Calculate interest earned
    # ADD YOUR CODE HERE
    print('Your interest is $', format(interest.get_balance(), ',.2f'))

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    def interest(account, amount):        
        account.balance += amount

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    account.balance = balance(interest)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
    print('Your account balance is $', format(Account.get_balance(), ',.2f'))
