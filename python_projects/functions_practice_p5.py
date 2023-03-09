#lambda function

grades = [("English", 88), ("Science", 90), ("Maths", 97), ("Social Sciences", 82)]

sorted_grades = sorted(grades, key = lambda c: c[1])

#print(sorted_grades)


cubed = lambda iterable: [element**3 for element in iterable]

#print(cubed([3, 6, 9, 2]))
#print(cubed([i for i in range(1, 101)]))


is_even = lambda n: True if n%2 == 0 else False

# print([is_even(k) for k in [3, 6, 9, 2]])


#print([i for i in range(1, 101)])


sentence = "The quick brown fox jumped over the fence"

#print({word: len(word) for word in sentence.split()})


