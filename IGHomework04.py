import Customer as c
import MonthlyMember as m
import AnnualMember as a

#create lists to store members
Members = {}
Amemb = {}
Mmemb = {}
header = []

#create try catch for file handling errors and debugging
try:
    #open file for reading (in correct directory)
    f = open ('D:\College\SeniorYear\SpringSemester\IS-4485\Homeworks\Input2.txt', 'r')

    #for each line of the file split on the | in order to
    #one get rid of the unessesary |
    #two store member info
    for line in f:
        attributes = line.split('|')
        #type management
        if (attributes[0].isdigit()):
            #create and store customer objects
            if(int(attributes[4]) == 1):
              Mmemb[attributes[0]] = m.MonthlyMember(attributes[0], attributes[1], attributes[2], attributes[3], attributes[5], attributes[6])
            if(int(attributes[4]) == 2):
              Amemb[attributes[0]] = a.AnnualMember(attributes[0], attributes[1], attributes[2], attributes[3], attributes[5], attributes[6])
        else:
          #deal with header
          header = attributes

    #close file
    f.close()
    print('File read correctly!')
#handle exception
except Exception as e:
    print("file failed to load!", e)
    pass

#collate
Members.update(Amemb)
Members.update(Mmemb)
header.append(None)
#print(Members)

'''Once you have read in the contents of the file you will need to loop through all of your members and call the formatDateWithSlashes() method.
 This will update their dates with the correct format.'''

for i in Members:
  Members[i].formatDateWithSlashes()

'''
Finally, you will create a members.xls file and write out the members information in a comma delimited form.
You will add an additional column that includes the member’s fee.
Example of first three lines should be something like this with an annual sign-up fee of $48:
CID,NAME,EMAIL,MEMBERSHIP_START,MEMBERSHIP_TYPE,FEE
83947,MARK L. PHILLIPS,mphilips@gmail.com,11/21/23,1,124
76856,ALICE B. WILSON,wila125@gmail.com,10/10/21,2,1248
'''

#create try catch for file handling errors and debugging
try:
    #open file for writing (in correct directory)(rewrite, don't append)
    k = open ('members.csv', 'w')

    #create header
    if (header):
      k.write(f'{header[0]},{header[1]},{header[2]},{header[3]},{header[-2]}')
      pass
    #write to file only if customer objects were stored
    if(Members):
        for c in Members:
            #write all customers in comma seperated rows
            #print(f'{Members[c].CID},{Members[c].name},{Members[c].email},{Members[c].MSD},{str(Members[c].getType())},${str(Members[c].getMembershipFee())}')
            k.write(f'{Members[c].CID},{Members[c].name},{Members[c].email},{Members[c].MSD},${str(Members[c].getMembershipFee())}\n')
    #close file
    k.close()
    print('Output file created!')
#handle exceptions
except Exception as e:
    print("file failed to write!", e)
    pass

'''
Make sure to use try except on all reading and writing of files. This is necessary to capture
errors such as file not found and/or data read/write errors.
    '''