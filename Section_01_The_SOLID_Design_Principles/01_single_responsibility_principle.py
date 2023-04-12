# SRP states that the class or module or function should have only single reason to change and that change should be
# somehow related to its primary responsibility. In other words it should have only one primary responsibility.


# Responsible for manipulating journal entries
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


# Responsible for saving the journal into the persistent storage
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate bug.")
print(f"Journal entries are:\n{j}")

PersistenceManager.save_to_file(j, 'sample.txt')
