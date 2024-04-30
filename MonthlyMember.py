import Customer as c

class MonthlyMember(c.customer):
  def __init__(self, CID, name, email, MSD, fee, FTS):
    #override init and add monthly member features if necessary
    super().__init__(CID, name, email, MSD, fee, FTS)
    self._membershipFee = 120

  def getMembershipFee(self):
    #override get to add monthly fee to base
    if (self.FTS):
      return (self._membershipFee + super().getMembershipFee() / 12)
    else:
       return self._membershipFee

  def getType(self):
    #override get type
    #super().getType()
    return 1
