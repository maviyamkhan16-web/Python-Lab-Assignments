class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Address: {self.address}")


class Manager(Employee):
    def process_info(self):
        print("\n--- Manager Information ---")
        self.display()


# Process 10 managers
managers = []
for i in range(10):
    print(f"\nEnter details for Manager {i+1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    address = input("Address: ")
    managers.append(Manager(name, age, salary, address))

print("\n===== Manager Details =====")
for m in managers:
    m.process_info()