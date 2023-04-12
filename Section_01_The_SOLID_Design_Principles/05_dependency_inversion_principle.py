# Dependency Inversion Principle:
# 1. High level module should not depend on low level modules.
# Both should depend on abstractions.
# 2. Abstractions should not depend on details.
# Details should depend on abstractions.
from enum import Enum
from abc import abstractmethod


# Not following DIP
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


# low level module.
class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )


# high level module
class Research:
    def __init__(self, relationships):
        # this is bad, as high level module depends on implementation details of low level module.
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

rel_ships = Relationships()

rel_ships.add_parent_and_child(parent, child1)
rel_ships.add_parent_and_child(parent, child2)

Research(rel_ships)


# implement dependency inversion principle solution by making low level and high level module
# dependent on the interface rather than on each other

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# low level module.
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# high level module -- not dependent on low level module.
class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

rel_ships = Relationships()

rel_ships.add_parent_and_child(parent, child1)
rel_ships.add_parent_and_child(parent, child2)

Research(rel_ships)
