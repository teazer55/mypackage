def top_n (items, n):
    """
    Return the top n items in an array in decending order

    Args:
    items (Array) list or array-like objct
    n (int) num of items to return

    Egs:
        >>>top_n([8,3,2,7,4], 3)
        returns [8,7,4]
    """
    for i in range(n): # keep sorting until we have the top items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:  #if this item is bigger than the next one
                items[j],items[j+a] = items[j+1],items[j] #swap the order

    top_n=items[-n:] # get the last n items

    return top_n[::-1]