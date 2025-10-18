"""An example of how to represent a group of acquaintances in Python."""

my_group = {'Jill':{
    'name': 'Jill',
    'age' : 26,
    'job' : 'biologist',
    'relations' :{
        'friend': ['Zalika', 'A', 'B'],
        'partner': ['John'],
        'colleague': []
    }
    
}}

# print(my_group['Jill'].get('job'))

def getJob(name): # getter
    print(my_group[name].get('job'))

def addPerson(name, job, age， relations):
    print('added person: ', name, job, age, relations)
    # add the person into the dictionary my_group

addPerson('Zalika', 'artist', 28, {'friend' :['jill']})

# def setJob(name, jobName): # setter
#     my_group[name].job = jobName

# print(getJob('Jill'))