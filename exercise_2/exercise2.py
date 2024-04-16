''' 
Exercise 2
Group 7
Erkam Dogan, Luca Hesse, Tobias Krumrein
'''
def donuts(count):
    if not isinstance(count, int):              # Error handling when not an int
        return "Error! You need an int as input for that function."
    if count < 10:                              # if count is less than 10 use count 
        return f'Number of donuts: {count}'
    return f'Number of donuts: many'            # else the count is 10 or more, then use the word 'many'

def verbing(s):
    if not isinstance(s, str):                  # Error handling when not a string
        return "Error! It's not a string!"
    if len(s) < 3:                              # if string length is less than three return only the string
        return s
    if s.endswith('ing'):                       # if string ends with 'ing', add 'ly'
        return f'{s}ly'
    return f'{s}ing'                            # else add 'ing' to string

def remove_adjacent(nums):
    if not (nums, list):                        # Error handling when not a list
        return 'Error! Not a list'
    final_list = []                             # create new list

    for num in nums:                            # iterate through the instances in nums
        if not isinstance(num, int) and not isinstance(num, float): # Error handling, when something else when a number is in the list
            return "Error! List contains instances, which are not numbers (int or float)."
        if not num in final_list:               # when number is not in the new list, add it to the list
            final_list.append(num)
    return final_list                           # return the final list


def main():
    print('donuts')
    print(donuts(4))
    print(donuts(9))
    print(donuts(10))
    print(donuts('twentyone'))
    print('verbing')
    print(verbing('hail'))
    print(verbing('swiming'))
    print(verbing('do'))
    print('remove_adjacent')
    print(remove_adjacent([1, 2, 2, 3]))
    print(remove_adjacent([2, 2, 3, 3, 3]))
    print(remove_adjacent([]))
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()