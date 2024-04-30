#Base customer class for Gym members, (CustomerID, name, email, Member Start Date (mm/dd/yy), sign up fee, and first time status)
class customer():
  def __init__(self, CID, name, email, MSD, fee, FTS):
    self.CID = CID
    self.name = name
    self.email = email
    self.MSD = MSD
    self.formattedEmail = False
    self.base = int(fee)
    if (FTS == '0'):
      self.FTS = False
    if (FTS == '1'):
      self.FTS = True

  #format date from input source to correct format for storage
  def formatDateWithSlashes(self):
    #do not double format
    if (not self.formattedEmail):
      #remove uneeded characters and replace with slashes
      tempDate = self.MSD.split('-')
      x = ''
      x = tempDate[0] + "/" + tempDate[1] + "/" + tempDate[2]

      self.MSD = x
    #set flag
    self.formattedEmail = True

  #get for membership base fee
  def getMembershipFee(self):
    self.FTS = False
    return self.base

  #get for membership type
  def getType(self):
    return 0