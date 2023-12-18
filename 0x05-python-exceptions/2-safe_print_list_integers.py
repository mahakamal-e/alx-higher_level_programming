def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
    except IndexError:
        pass  # Handle the scenario if x is greater than the length of my_list

    print()  # New line after printing integers
    return count
