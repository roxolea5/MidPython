def run():
    

    for elem in range(1, 10):
        if elem % 3 == 0:
            print(elem**2)

    print([elem**2 for elem in range(1,10) if elem % 3 == 0])

    # Reto: Generate a list comprehension retrieving only numbers divisibles 
    # by 4, 6 and 9 with max lenght of 5 digits

    print([i for i in range(1,100000) if i%4==0 and i%6==0 and i%9==0])



if __name__ == '__main__':
    run()