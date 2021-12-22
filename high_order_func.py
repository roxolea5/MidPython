from functools import reduce

def run():
    # Filter

    my_list = [1,6,9,5,11,13,8,22,14]

    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)

    #Map
    #Firsr challenge wth comprehensions

    print([x**2 for x in range(1,6)])

    other_list = [1,2,3,4,5]

    squares = list(map(lambda x: x**2, other_list))

    print(squares)

    #Reduce

    last_list = [2,2,2,2,2]

    multiplied = 1

    for i in last_list:
        multiplied = multiplied * i

    print(multiplied)

    reduced = reduce(lambda x, y: x*y, last_list)

    print(reduced)


if __name__ == "__main__":
    run()