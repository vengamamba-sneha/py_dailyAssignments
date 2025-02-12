from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        
    @abstractmethod
    def work(self):
        pass
    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    
    def work(self):
        return f'{self.name} manages team'
    def get_salary(self):
       return self.sal

class Developer(Employee):
   
    def work(self):
        return f'{self.name} is a tester'
    def get_salary(self):
        return self.sal

class Department:
    def __init__(self):
        self.empuu=[]
    def hire(self,employee:Employee):
        self.empuu.append(employee)
        print(f'{employee.name} hired')
    def fire(self,employee:Employee):
        if employee in self.empuu:
           self.empuu.remove(employee)
           print(f'{employee.name} fireddddddd')
        else:
           print('not in this dept')
    def get_total_sal(self):
        return sum(emp.get_salary() for emp in self.empuu )
    def show_emp_details(self):
        for emp in self.empuu:

            print(emp.name,emp.work(),emp.get_salary())        

def main():
    m1=Manager('kk',22)
    d1=Developer('jj',99)
    d2=Developer('oo',99)

    d=Department()
    d.hire(m1)
    d.hire(d1)
    d.hire(d2)
    
    print(d.get_total_sal())
    d.show_emp_details()
    d.fire(d1)
    d.show_emp_details()
main()

