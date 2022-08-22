For this problem, you will be writing a "retirement savings" calculator. We
will remove the effects of inflation by keeping everything in "today's
dollars" and using a "rate of return" that is in terms of "more than
inflation." 
 
 1. Create a file called "retirement.py".

 2. We're going to model both savings (while working) and expenditure
    (while retired). It turns out that both of these require the same 
    basic information, so we will use a tuple to represent that. 
    This tuple has three fields:
    (1) an integer "months" for the number of months it is applicable to;
    (2) a floating point number "contribution" for how many dollars are
        contributed (or spent if negative) from the account per month;
    (3) a floating point number "rate_of_return" for the rate of returns
        (which we will assume to be "after inflation").
 
 3. Write the function 
      calculateRetirement(start_age,  #in months
                          initial,    #initial savings in dollars
                          working,    #info about working
                          retired)    #info about being retired
    This function should perform two tasks (which are similar---look
    for a chance to abstract something out into a function!).
  
    First, it should compute your retirement account balance each month
    while you are working. To do this, you need to calculate the account
    balance increase from returns (balance * rate of return), and add that
    to the current balance. You then need to add the monthly contribution
    to the balance.
    
    For example, if you have $1,000 in the account, earn a 0.5% rate of
    return per month, and contribute $100 per month, you would compute 1000
    * 0.005 = $5 in interest earned. You would then add this plus the
    monthly contribution to the balance to end up with $1105 in the account
    at the end of the month. 

    At the start of each month (before the balance changes), you should
    print out the current balance with the following format:
      'Age {:3d} month {:2d} you have ${:.2f}'
    The first two format conversions are the savers age in years and
    months. The third format conversion is the account balance This
    calculation goes on for the number of months specified in the "working"
    tuple.

    Second, you should perform a very similar calculation for each month of
    retirement. The difference here is that you will use the information in
    the "retired" tuple instead of the information in the "working"
    tuple. As with working, you should print out the same information as
    before.

    Hint: since you are performing a very similar computation, think about
    how you can abstract that part out into a function, and reuse it,
    rather than rewriting it. 

 4. Write a main function which computes the retirement assuming
      Working:
      --------
      Months: 489
      Per Month Savings: $1000
      Rate of Return:  4.5% per year (0.045/12 per month) 
                       [above inflation]
      Retired:
      --------
      Months: 384
      Per Month Spending: -4000
      Rate of Return: 1% per year ( 0.01/12 per month) 
                      [above inflation]
      Starting conditions:
      -------------------
      Age: 327 months (27 years, 3 months)
      Savings: $21,345

    Note that this main should  be called under
    
    if __name__ == "__main__":

    so that it only runs if this module is run as the main
    program, and not loaded as part of something else
    (e.g., if we load it into the grader to run other test cases!)

 5. Run your code and test it (we provided the output:
    retirement_ans.txt). 

 6. Submit retirement.py