# Week 10 assignment 2
# File opener/proof
# Date last modified: March 13, 2024
# Last modified by: Isaak Grettum
# ===============================
'''
You may name this text file whatever you want. 
Make a program that will open said text file and store every single letter into a list. 
Then count how many vowels, consonants, and other characters there are. 
Display the results.
'''
#create list to letters
importPy = []
cVow = 0
cCon = 0
cOth = 0

# open file in try except block
try:
    #open file for reading (in correct directory)
    f = open ("D:\College\SeniorYear\SpringSemester\IS-4485\WeeklyAssignments\W10A02.txt", 'r')
 
    #for each line of the file take each letter
    for line in f:
        for char in line:
            #append character to list
            importPy.append(char)

            #test if special character
            if (char in (',','.','*','-','!','\'','\n',' ')):
                cOth += 1
                #continue if is special character, as to not ("!").lower()
                continue
            #test if vowel
            elif (char.lower() in ('a','e','i','o','u')):
                cVow += 1
            #if not vowel or special character, then is consonant
            else:
                cCon += 1

    #close file
    f.close()
    print('File read correctly!')
#handle exception
except Exception as e:
    print("file failed to load!", e)
    pass

#display results
print(f'In that file I found {cVow} vowells (not including special cases of y), {cCon} constanants, and {cOth} special characters.')
#displaying the full list took an annoying amount of screen space
#print(f'Here is the list of all of them together: {importPy}')