print("Python OOPs Project: Employee Management System.")

class Employee:
    def __init__(self,emp_id=None,name=None,age=None,salary=None):
        self.__emp_id = emp_id
        self.name = name
        self.age = age 
        self.__salary = salary


    def set_id(self,emp_id):
            self.__emp_id = emp_id

    def get_id(self):
        return self.__emp_id 

    def set_salary(self,salary):
        self.__salary = salary
        
    def get_salary(self):
        return self.__salary


    def display(self):
        print(f"Employee ID is : {self.__emp_id}")
        print(f"Employee Name is : {self.name}")
        print(f"Employee Age is : {self.age}")
        print(f"Employee Salary is : {self.__salary}")

    def __del__(self):
       print("Destructor called")


class Manager(Employee):
    def __init__(self,emp_id,name,age,salary,department):
        super(). __init__(emp_id,name,age,salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Employee Department is {self.department}")


class Developer(Employee):
    def __init__(self, emp_id, name, age, salary,programming_lang):
        super().__init__(emp_id, name, age, salary)
        self.programmming_lang = programming_lang

    def display(self):
        super().dispaly()
        print(f"Employee Programming Language is:  {self.programmming_lang}")


person = None
employee = None
manager = None


while True:
    print()
    print("\nSelect an Option :")
    print("1. Create a Person")
    print("2. Create an Employee ")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        person = Employee(name=name, age=age)
        print(f"Person created with name: {name} and age: {age} ")
 
    elif choice == 2:
        emp_id = int(input("Enter Employee Id: "))
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        salary = int(input("Enter your salary: "))
        employee = Employee(emp_id, name, age, salary)
        print(f"Employee created with employee Id: {emp_id}, name: {name}, age: {age} and salary: {salary}")

    elif choice == 3:
        emp_id = int(input("Enter Employee Id: "))
        name = input("Enter Empoyee Name: ")
        age = int(input("Enter Employee Age: "))
        salary = int(input("Enter Employee Salary: "))
        department = input("Enter Department Name: ")
        manager = Manager(emp_id, name, age, salary, department)
        print(f"Manager created with manager Id: {emp_id}, name: {name}, age: {age}, salary: {salary} and department name: {department}")
        print()

    elif choice == 4:
        print("Select an option:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager" )

        ans = int(input("Enter your choice: "))

        if ans == 1:
            if person != None: 
                person.display()
            else:
                print("Notfound")

        elif ans == 2:
             if employee != None :
                employee.display()
             else:
                print("Notfound")
                
        elif ans == 3:
            if manager != None :
                manager.display()
            else:
                print("Notfound")

        else:
            print("invalid Input")

    elif choice == 5:
        print("Exited The Programe")
        break

    else:
        print("Invalid choice")


print(f"Is Manager Class Sub Class of Employee Class - {issubclass(Manager,Employee)}")
print(f"Is Developer Class Sub Class of Employee Class - {issubclass(Developer,Employee)}")