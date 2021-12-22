def run():
    # Reto 1 Regresar un dicccionario cuyas llaves sean los primeros 100 numeros naturales y su valor sea ese numero elevado al cubo
    # my_dict = {}

    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # print(my_dict)

    print({value: value**3 for value in range(1,101) if value%3!=0})  

    #Otro reto dict comprehension keys primero 1000 numeros y valores la raiz cuadrada de key

    print({i: i**0.5 for i in range(1,1001)})  



if __name__ == '__main__':
    run()