def split_lst(number, lst):
    length = (len(lst)) # How many numbers does the list have
    middle_value = length / 2 # Find the median
    midint = int(middle_value) # Vi tar medelvärdet och gör om det till ett heltal
    num_int = int(number[0]) # Det här är 3 som int
    if num_int < lst[midint]:
        new_lst = (lst[:midint])
        print(f"This is your new list: {new_lst}")
        split_lst([3],new_lst)


split_lst([3], [3, 4, 5, 6, 7, 8, 8, 9, 99, 111])
