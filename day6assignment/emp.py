class Employee:
    def _init_(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

class Manager(Employee):
    def _init_(self, name, age, salary, department):
        super()._init_(name, age, salary, department)

class Engineer(Employee):
    def _init_(self, name, age, salary, department, skills):
        super()._init_(name, age, salary, department)
        self.skills = skills

class Company:
    def _init_(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_manager(self, department):
        for emp in self.employees:
            if isinstance(emp, Manager) and emp.department == department:
                return emp.name
        return "No manager found for this department."

    def count_employees_in_department(self, department):
        return sum(1 for emp in self.employees if emp.department == department)

    def engineers_with_skill(self, skill):
        return sum(1 for emp in self.employees if isinstance(emp, Engineer) and skill in emp.skills)

    def total_employees_per_department(self):
        department_count = {}
        for emp in self.employees:
            department_count[emp.department] = department_count.get(emp.department, 0) + 1
        return department_count

    def total_employees(self):
        return len(self.employees)

# Creating company instance
company = Company()

# Taking user input for at least 3 employees per department
num_departments = int(input("Enter the number of departments: "))

for _ in range(num_departments):
    department = input(f"\nEnter department name: ")

    # Adding Manager
    print(f"Enter manager details for {department}:")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    company.add_employee(Manager(name, age, salary, department))

    # Adding Engineers
    for _ in range(3):  # Minimum 3 employees per department
        print(f"\nEnter engineer details for {department}:")
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))
        skills = input("Enter skills (comma-separated): ").split(",")
        company.add_employee(Engineer(name, age, salary, department, skills))

# (b) Find manager for a given department
dept = input("\nEnter department to find manager: ")
print(f"Manager of {dept}: {company.get_manager(dept)}")

# (c) Count employees in a given department
dept = input("\nEnter department to count employees: ")
print(f"Total employees in {dept}: {company.count_employees_in_department(dept)}")

# (d) Count engineers with a given skill
skill = input("\nEnter skill to find how many engineers have it: ")
print(f"Number of engineers with {skill}: {company.engineers_with_skill(skill)}")

# (e) Total employees per department
print("\nTotal employees in each department:")
for dept, count in company.total_employees_per_department().items():
    print(f"{dept}: {count}")

# (f) Total employees in all departments
print(f"\nTotal employees in the company: {company.total_employees()}")

