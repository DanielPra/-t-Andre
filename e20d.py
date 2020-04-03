#Jag får bara koden från Repl att stämma för det lägsta nummret dvs 3 i det här fallet. Är det här pga av att koden inte kollar på elementet '
#som den skalar bort utan endast på det sista kvarvarande nummret?

#Jag la till de här två raderna:

#if num_int == number:
#            return("True!")
            
#Hela programmet nedan. Är det en vettig lösning?



def split_lst(number, lst):
    print(f"looking for {number} in {lst}")
    length = len(lst)
    if length == 0:
        return False
    elif length == 1:
        if lst[0] == number:
            return True
        else:
            return False
    else:
        middle_index = length // 2 # Ger ett heltal. 9/2 = 4
        num_int = lst[middle_index] # lst[4] Mittersta talet dvs '7', 4, etc
        if num_int == number:
            return("True!")
        if num_int < number:        # Om mittentalet (7) är mindre än 3
            new_lst = lst[middle_index:] #
        else:
            new_lst = lst[:middle_index]
        return split_lst(number, new_lst)


print(split_lst(8, [1, 2, 4, 5, 6, 7, 8, 30, 88, 99, 111]))
