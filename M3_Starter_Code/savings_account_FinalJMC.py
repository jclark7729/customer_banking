"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: The updated savings account balance and the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    account_class = Account(balance, 0)
    
    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = account_class.update_balance(interest_earned)

    # Pass the updated_balance to the set balance method using the instance of the Account class.
    account_class.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the Account class.
    account_class.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned

# Test the function with example values
initial_balance = 1000
interest_rate = 5  # Example APR
months = 12  # Example duration in months

updated_balance, interest_earned = create_savings_account(initial_balance, interest_rate, months)
print(f"The updated balance is {updated_balance} and the interest earned is {interest_earned}")


