'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

i = int(input("Please enter the number, enter 0 for exiting: "))
numbers = {"odd":[],"even":[]}
while i != 0:
    if i % 2 == 1:
       numbers["odd"].append(i)
    else:
        numbers["even"].append(i) 
    i = int(input("Please enter the number, enter 0 for exiting: "))
print(numbers)