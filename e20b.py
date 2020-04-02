# Är det här då jag har en funktion som behöver t.ex num_int och den finns i en funktion som inte utförts än?

Traceback (most recent call last):
  File "e20b.py", line 20, in <module>
    split_lst()
  File "e20b.py", line 15, in split_lst
    if num_int < lst[midint]:
NameError: name 'num_int' is not defined
PS C:\Users\inbad\dantest\lpthw>             

--------------------------------------------
number = [3]

lst = [3, 4, 5, 6, 7, 9, 99, 111]

def find_length():
    length = (len(lst)) # How many numbers does the string have
    middle_value = length / 2 # Find the median number
    midint = int(middle_value) # Get a whole number from the median
                               # Vi tar medelvärdet och gör det till ett heltal
    num_int = int(number[0]) # Det här är 3 som int
    #print(lst[midint])       # Talet vi vill kolla mot en lista


def split_lst():
    if num_int < lst[midint]:
        new_lst = (lst[:midint])
        print(new_lst)


split_lst()
