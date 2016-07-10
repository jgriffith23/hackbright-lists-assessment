"""List Assessment

Edit the functions until all of the doctests pass when
you run this file.
"""


def all_odd(numbers):
    """Return a list of only the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

    #Initialize a list to contain all odd numbers, according to the base case.
    #Since the list should be empty if there are only even numbers, the initial
    #list is empty.
    odd_list = []

    #Check each number in the passed list. An even number gives a remainder of zero
    #when divided by 2, so use that to check for oddness. if the number is not even,
    #then it must be odd, so add it to the list.
    for number in numbers:
        if number % 2 != 0:
            odd_list.append(number)
    return odd_list


def print_indices(items):
    """Print index of each item in list, followed by item itself.

    Do this without using a "counting variable" --- that is, don't
    do something like this::

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this::

        >>> print_indices(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo
    """

    #To get the index without a counting variable, loop over the length of the
    #list, rather than the list itself. Use format strings to insert the index
    #and the element in the string to print.
    for index in range(len(items)):
        print "{} {}".format(index, items[index])


def foods_in_common(foods1, foods2):
    """Find foods in common.

    Given 2 lists of foods, return the items that are in common
    between the two, sorted alphabetically.

    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists). Is there another that would be a good idea?

    For example::

        >>> foods_in_common(
        ...     ["cheese", "bagel", "cake", "kale"],
        ...     ["hummus", "beets", "bagel", "lentils", "kale"]
        ... )
        ['bagel', 'kale']

    If there are no foods in common, return an empty list::

        >>> foods_in_common(
        ...     ["lamb", "chili", "cheese"],
        ...     ["cake", "ice cream"]
        ... )
        []

    """

    #Convert the two food lists to sets, since sets have handy built-in
    #operations we can use to easily compare groups of items.
    food_set_1 = set(foods1)
    food_set_2 = set(foods2)

    #Use the intersection operator (&) to get the common food items, and
    #cast the result to a list.
    common_foods = list(food_set_1 & food_set_2)

    #Sort the list and return it!
    return sorted(common_foods)


def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    #Start at index 0 and use a step value of 2 to get every other element
    #in the list. Use no stop value so the slice goes all the way to the end.
    return items[0::2]


def largest_n_items(items, n):
    """Return the `n` largest integers in list, in ascending order.

    You can assume that `n` will be less than the length of the list.

    For example::

        >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [59, 700, 6006]

    It should work when `n` is 0::

        >>> largest_n_items([3, 4, 5], 0)
        []

    If there are duplicates in the list, they should be counted
    separately::

        >>> largest_n_items([3, 3, 3, 2, 1], 2)
        [3, 3]
    """

    #Sort list from smallest to largest, in-place.
    items.sort()

    #Initialize an empty list for the base case. If the passed list had
    #nothing in it, then the list of largest numbers is empty.
    largest_items = []

    #Loop over indices for a number of times equal to the number of largest
    #values the user wants.
    for index in range(n):

        #At each index, fetch the smallest of the largest values, and add it to
        #the list to be returned.
        largest_items.append(items[index - n])

        """
        For reference, here's how I got to (index - n):
            Say you have the list [1, 2, 3, 4, 5] and want the 3 biggest values.

            Those values are 3, 4, and 5.

            3 is at index -3, 4 is at index -2, and 5 is at index -1

            In this loop, index will hit 0, 1, and 2.

            -3 = 0 - 3   ------|        In all cases, the difference between
            -2 = 1 - 3   ------|----->  index and the reverse index is equal
            -1 = 2 - 3   ------|        to 3, which is the value of n.
        """

    return sorted(largest_items)


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
