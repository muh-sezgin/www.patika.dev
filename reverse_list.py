def reverse_list(list_to_reverse):
    list_to_reverse.reverse()
    for i in range(len(list_to_reverse)):
        if isinstance(list_to_reverse[i], list):
            list_to_reverse[i].reverse()
      
    return list_to_reverse