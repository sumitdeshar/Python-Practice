from UnitTesting.pytest_tryout.person import Person
import pytest

@pytest.fixture()
def person():
    return Person('Ethan Henderson', 24, jobs=['Software Engineer'])


def test_init(person : Person):
    assert person.name == 'Ethan Henderson'
    assert person.age == 24
    assert person.jobs == ['Software Engineer']
    
    
def test_forename(person : Person):
    assert person.forename == 'Ethan'
    
def test_surname(person : Person):
    assert person.surname == 'Henderson'
    
def test_no_surname(person : Person):
    person.name = 'Ethan'
    assert not person.surname
    
def test_celebrate_birthday(person : Person):
    person.celebrate_birthday()
    assert person.age ==25
    
def test_add_job(person : Person):
    person .add_job('Backend Developer')
    assert person.jobs == ['Software Engineer', 'Backend Developer']
    