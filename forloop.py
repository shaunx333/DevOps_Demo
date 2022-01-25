"""
For loop
 #.isnumeric method helps to identify for numeric value in a string
"""

book="Norwegian woods"
seperators=""

for i in book:
    print(i)

numbers=input("Enter a series of numbers along with seperators :\n") # like for example 203:12'456,34;
for i in numbers:
    if not i.isnumeric(): #.isnumeric method helps to identify for numeric value in a string
        seperators=seperators+i
print(seperators)






# #Challenge to print all capital letters
# char="Alright, but apart from the Sanitation, the Medicine, Education, Wine,Public Order, Irrigation, Roads, the Fresh-Water System,and Public Health, what have the Romans ever done for us?"
# sum=""
# for i in char:
#     if i not in i.casefold():
#         sum=sum+i
# print(sum)