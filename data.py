
def validate(nullable, value):
    if nullable and value is not None:
        print(value)
    if not nullable and (value.isspace()):
        print("Cadena vacía")
    if not nullable and value is not None:
        print(value)



def run():
    print("1")
    validate(True, "hi")
    print("2")
    validate(False, "   ")
    print("3")
    validate(False, "hola")

    



if __name__ == '__main__':
    run()