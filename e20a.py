# Fråga - Om jag nu skriver det så här bör jag nämna om variablerna på rad 30 till
# t.ex length2, midint2 etc?

number = [3]

lst = [3, 4, 5, 6, 8, 9, 99, 111]

length = (len(lst)) # How many numbers does the string have

middle_value = length / 2 # Find the median number

midint = int(middle_value) # Get a whole number from the median
                           # Vi tar medelvärdet och gör det till ett heltal

num_int = int(number[0]) # Det här är 3 som int
                         # Talet vi vill kolla mot en lista

if num_int < lst[midint]:   # Om 3 < 7 = True
    new_lst = (lst[:midint]) # Skapa ny lista  med element 0-> midint (4)
    print(f"The first split list is {new_lst}")
    #print("\nYour number is bigger than the median number")


#-------------------------------------------------------------------
# Ta lista 2 (new_lst) och dela den igen:
# ta samma nummer och jämför med den nya listan


length = (len(new_lst)) # Längden av den nya listan

middle_value = length / 2 # Hälften av nya listan

midint = int(middle_value) # Gör till heltal

num_int = int(number[0]) # Talet 3

if num_int < new_lst[midint]:   # Om 3 <
    third_lst = (new_lst[:midint]) #
    print(f"The second split list is {third_lst}")
