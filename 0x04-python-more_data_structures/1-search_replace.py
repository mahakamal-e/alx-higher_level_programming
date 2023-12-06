#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []

    # Iterate through the original list
    for item in my_list:
        # If the element matches the 'search' element, replace it with 'replace'
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)  # Otherwise, keep the original element

    return new_list  # Return the new list with replaced elements

