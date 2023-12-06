#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}
    result_list = []
    result = 0
    for i in roman_string:
        result_list.append(roman_dict.get(i))

    for iterat in range(len(result_list)):
        if iterat == len(result_list) - 1:
            result += result_list[iterat]
        elif result_list[iterat] < result_list[iterat + 1]:
            result -= result_list[iterat]
        else:
            result += result_list[iterat]

    return result

