



def split_lst(number, lst):
    print("looking for %d in %s" % (number, lst))
    length = len(lst) # How many numbers does the list have
    if length == 0:
      return False
    elif length == 1:
      if lst[0] == number:
        return True
      else:
        return False
    else:
      middle_index = length // 2 # Find the median
      num_int = lst[middle_index] # Det här är 3 som int
      if num_int < number:
        new_lst = lst[middle_index:]
      else:
        new_lst = lst[:middle_index]
      return split_lst(number, new_lst)
        

print(split_lst(4, [3, 4, 5, 6, 7, 8, 8, 9, 99, 111]))
