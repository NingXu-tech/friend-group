# my_group ={
#     'Jill':{
#         'age':26,
#         'job':'Biologist',
#         'relationship':{
#             'Zalika':'friend',
#             'John':'partner',
#         }
#     },
#     'Zalika':{
#         'age':28,
#         'job':'Artist',
#         'relationship':{
#             'Jill':'friend',
#         }
#     },
#     'John':{
#         'age':27,
#         'job':'Writer',
#         'relationship':{
#             'Jill':'partner',
#         }
#     },
#     'Nash':{
#         'age':34,
#         'job':'Chef',
#         'relationship':{
#             'Jill':'cousin',
#             'Zalika':'landlord'
#         }
#     }
# }

# print(my_group)
# If you prefer building the group programmatically, use the functions below.
# We'll create a fresh `group` dictionary and add people correctly.
group = {}
def add_person(name, age, job, relationships):
    if relationships is None:
        relationships = {}
    group[name] = {
        'age': age,
        'job': job,
        'relationship': relationships
    }
def add_relationships(person1, person2, relation):
    """Add a relationship from person1 to person2.

    Both persons must already exist in `group`.
    """
    if person1 in group and person2 in group:
        group[person1]['relationship'][person2] = relation
    else:
        print("One or both persons not found in the group.")
add_person("Jill", 26, "biologist", {})
add_person("Zalika", 28, "artist", {})
add_person("John", 27, "writer", {})
add_person("Nash", 34, "chef", {})
add_relationships("Jill", "Zalika", "friend")
add_relationships("Jill", "John", "partner")
add_relationships("Nash", "John", "cousin")    
add_relationships("Nash", "Zalika", "landlord")
add_relationships("Zalika", "Jill", "friend")
add_relationships("John", "Jill", "partner")
print(group)    

def forget(person1,person2):
    """Remove the relationship from person1 to person2."""
    if person1 in group and person2 in group[person1]['relationship']:
        del group[person1]['relationship'][person2]
    if person2 in group and person1 in group[person2]['relationship']:
        del group[person2]['relationship'][person1]
    else:
        print("One or both persons not found in the group or no such relationship exists.")
forget("Nash","John")
print(group)
def average_age():
    """Calculate the average age of all people in the group."""
    if not group:
        return 0
    total_age = sum(person['age'] for person in group.values())
    return total_age / len(group)
print("Average age:", average_age())