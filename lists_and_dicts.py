def run():
    my_list = [1, True, "Hola", 4,5]
    my_dict = {"first_name": "Roxana", "last_name": "Olea"}

    super_list = [
        {"first_name": "Roxana", "last_name": "Olea"},
        {"first_name": "Betty", "last_name": "Sanchez"},
        {"first_name": "Israel", "last_name": "Olea"},
        {"first_name": "Luisa", "last_name": "Bravo"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integers_nums": [-1,-2,0,1,2],
        "float_nums": [1.3, 2.0, 18.6]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for elem in super_list:
        print(elem)



if __name__ == '__main__':
    run()