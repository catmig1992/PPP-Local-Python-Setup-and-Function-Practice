def name_args(**kwargs):
    for key in kwargs.keys():
        print(f"{key}: {kwargs[key]}")

#name_args(Catherine="me", Location="here", When="now")


def all_true(iter):
    return all(iter)

#print(all_true([True, True, True]))
#print(all_true([False, True, True]))


def one_true(iter):
    return any(iter)

#print(one_true([True, True, True]))
#print(one_true([False, False, True]))


def recursive_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)

#print(recursive_factorial(3))
#print(recursive_factorial(10))


def recursive_deduplicate(my_str, it = 0):
    #print(f"current string: {my_str}, iterator: {it}")
    if len(my_str)<= 1 or it == len(my_str) - 1:
        return my_str
    if my_str[it] == my_str[it + 1]:
        return recursive_deduplicate(my_str[0 : it] + my_str[it + 1:], it )
    else:
        return recursive_deduplicate(my_str, it + 1)


#print(recursive_deduplicate("aaaa"))
#print(recursive_deduplicate("bbababbbaaaabbb"))


def recursive_reverse(my_str, iter=0):
    #print(f"current string: {my_str}, iterator: {iter}")
    if len(my_str) == 0:
        return ""
    elif iter == len(my_str) - 1:
        return my_str[0]
    else:
        return my_str[-1 - iter] + recursive_reverse(my_str, iter + 1)

#print(recursive_reverse("Catherine Miguel"))

