"""
    You need to create a class hierarchy to store the data from the input file where you will make a MonthlyMember and AnnualMember class. 
    Each of these classes should be the child of a Member class.
    All of your classes should have initializers. 
    Your Member class initializer should take in CID, name, email and membership_start. 
    These values should be stored as variables inside of self.
    Through inheritance the child classes should then have access to these variables.
    Your Member class should have a getMembershipFee() method that will return a fee amount depending on what kind of gym member a person is. 
    All members pay an annual sign-up fee of between $20 and $132. 
    The monthly member pays part of this fee each month and the annual members pay the entire fee up front. 
    Normally a monthly member pays $120 a month to be a member and an annual member pays $1200 a year to be a member. 
    So for example if the annual sign-up fee was $48 then the total comes to $124 a month for a monthly member and $1248 a year for an annual member. 
    The parent Member class getMembershipFee() should return the annual sign-up fee base amount since that is used by all members. 
    Your code should be able to handle an annual sign-up fee range between $1 and $100,000.
    Your Member class should also have a method called formatDateWithSlashes(). 
    When called this method will reformat the variable for membership_start in self to use slashes(/) instead of dashes(-). For example a date of 01-02-20 should be formatted as 01/02/20.
"""
class Member():  
    CID = None
    name = None
    email = None
    start = None

    def __init__(self, CID, name, email, start):
        self.CID = CID
        self.name = name
        self.email = email
        self.start = start

        def getMembershipFee():
            pass

        def formatDateWithSlashes():
    
