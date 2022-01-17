import pytest

# from app.main import make_a_person
# from app.main import Person

from app.reference import make_a_person
from app.reference import Person

@pytest.mark.parametrize(
    'person,name,age',
    [

        ({'name': 'Ross', 'age': 30, 'wife': 'Rachel'}, 'Ross', 30),
        ({'name': 'Joey', 'age': 29, 'wife': None}, 'Joey', 29)
    ]
)
def test_person_class_name_age(person, name, age):
    person_inst = Person(person['name'], person['age'])
    assert person_inst.name == name, (
        f"Attribute 'name' for Person instance for {person} "
        f"should equal to {name}"
    )
    assert person_inst.age == age, (
        f"Attribute 'age' for Person instance for {person} "
        f"should equal to {age}"
    )


def test_make_a_person_all_persons():
    people = [
        {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
        {'name': 'Joey', 'age': 29, 'wife': None},
        {'name': 'Phoebe', 'age': 31, 'husband': None},
        {'name': 'Chandler', 'age': 30, 'wife': 'Monica'},
        {'name': 'Monica', 'age': 32, 'husband': 'Chandler'},
        {'name': 'Rachel', 'age': 28, 'husband': 'Ross'},
    ]
    person_list = make_a_person(people)
    assert all(isinstance(i, Person) for i in person_list), (
        "All elements in result of 'make_a_person' should be instance "
        "of Person class"
    )


def test_make_a_person_order():
    people = [
        {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
        {'name': 'Joey', 'age': 29, 'wife': None},
        {'name': 'Phoebe', 'age': 31, 'husband': None},
        {'name': 'Chandler', 'age': 30, 'wife': 'Monica'},
        {'name': 'Monica', 'age': 32, 'husband': 'Chandler'},
        {'name': 'Rachel', 'age': 28, 'husband': 'Ross'},
    ]
    person_list = make_a_person(people)
    for i in range(len(people)):
        assert people[i]['name'] == person_list[i].name and people[i]['age'] == person_list[i].age, (
            "Order in function result should be the"
        )

def test_make_a_person_has_wife():
    people = [
        {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
        {'name': 'Joey', 'age': 29, 'wife': None},
        {'name': 'Phoebe', 'age': 31, 'husband': None},
        {'name': 'Chandler', 'age': 30, 'wife': 'Monica'},
        {'name': 'Monica', 'age': 32, 'husband': 'Chandler'},
        {'name': 'Rachel', 'age': 28, 'husband': 'Ross'},
    ]
    person_list = make_a_person(people)
    assert hasattr(person_list[0], 'wife'), (
        f"For 'people' equals to {people} "
        f"Person with 'name' {person_list[0].name} should have "
        f"attribute 'wife' with name {person_list[0].wife.name}"
    )


def test_make_a_person_has_wife_and_wife_have_husband():
    people = [
        {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
        {'name': 'Joey', 'age': 29, 'wife': None},
        {'name': 'Phoebe', 'age': 31, 'husband': None},
        {'name': 'Chandler', 'age': 30, 'wife': 'Monica'},
        {'name': 'Monica', 'age': 32, 'husband': 'Chandler'},
        {'name': 'Rachel', 'age': 28, 'husband': 'Ross'},
    ]
    person_list = make_a_person(people)
    assert hasattr(person_list[0], 'wife') and person_list[0].wife.husband == person_list[0], (
        f"For 'people' equals to {people} "
        f"Person with 'name' {person_list[0].name} should have "
        f"attribute 'wife' with name {person_list[0].wife.name} and "
        f"Person.wife.husband should links to that Person"
    )


def test_make_a_person_has_no_wife():
    people = [
        {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
        {'name': 'Joey', 'age': 29, 'wife': None},
        {'name': 'Phoebe', 'age': 31, 'husband': None},
        {'name': 'Chandler', 'age': 30, 'wife': 'Monica'},
        {'name': 'Monica', 'age': 32, 'husband': 'Chandler'},
        {'name': 'Rachel', 'age': 28, 'husband': 'Ross'},
    ]
    person_list = make_a_person(people)
    assert hasattr(person_list[1], 'wife') is False, (
        f"For 'people' equals to {people} "
        f"Person with 'name' {person_list[1].name} should not have "
        f"attribute wife"
    )

