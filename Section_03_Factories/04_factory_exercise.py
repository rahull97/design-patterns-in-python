class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"


class PersonFactory:
    ID = 0

    def create_person(self, name):
        p = Person(PersonFactory.ID, name)
        PersonFactory.ID = PersonFactory.ID + 1
        return p


if __name__ == '__main__':
    person1 = PersonFactory().create_person("Bob")
    person2 = PersonFactory().create_person("Charles")
    print(person1)
    print(person2)
