#AUTHOR: Ikenna
#DATE: 10/31/2023
#PURPOSE: A15


def compare_int(a, b):
    return a <= b

def compare_str(s1, s2):
    return len(s1) <= len(s2)

# print(compare_func(1, 2)

def partition(the_list, p, r, compare_func):

    i = p - 1
    j = p
    pivot  = the_list[r]

    while j < r:
        if compare_func(the_list[j], pivot): #returns true if A compares as less than or equals to B
            i += 1
            the_list[i],the_list[j] = the_list[j], the_list[i]
            j += 1
        else:
            j += 1

    the_list[i+1], the_list[r] = the_list[r], the_list[i+1]
    return i + 1

def quicksort(the_list, p, r, compare_func):
    if r > p:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)

    return the_list

def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)
    return the_list




