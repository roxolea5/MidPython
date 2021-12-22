DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Rotz',
        'age': 31,
        'organization': 'Urbvan',
        'position': 'Backend Dev',
        'language': 'python',
    },
    {
        'name': 'Daniel',
        'age': 33,
        'organization': 'Luxoft',
        'position': 'Tech Lead',
        'language': 'javascript',
    },
    {
        'name': 'Octavio',
        'age': 28,
        'organization': 'Urbvan',
        'position': 'Backend Dev',
        'language': 'python',
    },
    {
        'name': 'Sheida',
        'age': 28,
        'organization': 'HCL',
        'position': 'Senior Dev',
        'language': 'java',
    },
    {
        'name': 'Jered',
        'age': 25,
        'organization': 'HCL',
        'position': 'Senior Dev',
        'language': 'java',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'javascript',
    },
    {
        'name': 'Lorena',
        'age': 15,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"]=="python"]
    all_urbvan_workers = [worker["name"] for worker in DATA if worker["organization"]=="Urbvan"]
    adults = list(filter(lambda worker: worker["age"] > 18,DATA))
    adult = list(map(lambda worker: worker["name"]))

    

if __name__ == "__main__":
    run()

