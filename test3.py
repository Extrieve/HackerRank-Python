
mystring = r'D:\Documents\OneDrive - University of South Florida\Semesters\Spring 2022\QMB 6304 Analytical Methods for Bus\Module 1\Submissioin'

newstring = ''
for letter in mystring:
    if letter == '\\':
        newstring += '/'
    else:
        newstring += letter

print(newstring)
