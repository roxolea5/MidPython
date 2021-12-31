def divisor(num):
    divisors = []

    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    
    return divisors


def run():
    try:
        num = int(input("Ingresa un numero: "))
        if num <= 0:
            raise Exception("Ingresa números mayores a 0")
        else:
            print(divisor(num))
            print("Terminó el programa")
    except ValueError as ve:
        print("El valor ingresado no es un número")    
    

if __name__ == "__main__":
    run()
