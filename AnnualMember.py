import Customer as c

class AnnualMember(c.customer):
  def __init__(self, CID, name, email, MSD, fee, FTS):
    #override init and add annual member features if necessary
    super().__init__(CID, name, email, MSD, fee, FTS)
    self._membershipFee = 1200

  def getMembershipFee(self):
    #override get to add annual fee to base
    if (self.FTS):
      return (self._membershipFee + int(super().getMembershipFee()))
    else:
      return (self._membershipFee)

  def getType(self):
    #override get type
    #super().getType()
    return 2