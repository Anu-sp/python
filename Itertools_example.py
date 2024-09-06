#Infinite Iterators

#1)count(start=0, step=1): Creates an iterator that returns evenly spaced values starting with start. 
# It's useful for generating an infinite sequence of numbers.
#2)cycle(iterable): Repeats an iterable indefinitely. 
# It's useful when you need to loop over the same sequence multiple times.
#)repeat(object, times=None): Repeats an object multiple times. 
# If times is specified, it stops after the given count; otherwise, it repeats indefinitely.

from itertools import count,cycle,repeat

#example of count
for i in count(5,2):  # Starts at 5, increments by 2
    if i > 15:
        break
    print(i)

#example of cycle
counter = 0
for item in cycle(['A','B','C']):
    if counter >= 9:
        break
    print(item)
    counter  += 1

# Example of repeat
for item in repeat('Hello', 3):
    print(item)


#Finite Iterators

#1)chain(*iterables): Combines multiple iterables into a single iterator.
#2)compress(data, selectors): Filters elements from data, 
# returning only those that have a corresponding element in selectors that evaluates to True.
#3)dropwhile(predicate, iterable): Drops items from the iterable as long as the predicate is true; afterwards, returns every element.
#4)takewhile(predicate, iterable): Returns items from the iterable as long as the predicate is true.
#5)accumulate(iterable, func=operator.add): Makes an iterator that returns accumulated sums or 
# the accumulated result of a binary function (e.g., multiplication).

from itertools import chain, compress, dropwhile, takewhile, accumulate

# Example of chain
print(list(chain([1, 2, 3], [4, 5], [6, 7])))

# Example of compress
print(list(compress('ABCDEF', [1, 0, 1, 0, 0, 1])))

# Example of dropwhile
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))) 

# Example of takewhile
print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  

# Example of accumulate
print(list(accumulate([1, 2, 3, 4]))) 


#Combinatoric Iterators

#1)product(*iterables, repeat=1): Computes the Cartesian product of input iterables. Equivalent to nested loops.
#2)permutations(iterable, r=None): Returns all possible permutations (order matters) of elements from the iterable.
#3)combinations(iterable, r): Returns all possible combinations (order doesn't matter) of elements from the iterable.
#4)combinations_with_replacement(iterable, r): Similar to combinations, but allows individual elements to be repeated.

from itertools import product, permutations, combinations, combinations_with_replacement

# Example of product
print(list(product('AB', '12')))  

# Example of permutations
print(list(permutations('ABC', 2)))  

# Example of combinations
print(list(combinations('ABC', 2)))

# Example of combinations_with_replacement
print(list(combinations_with_replacement('xy', 2)))


