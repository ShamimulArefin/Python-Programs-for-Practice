# Write a program to display customer information using multilevel inheritance.

class CustomerName:
    def name(self):
        print("name: Mr.X")

class CustomerJob:
    def job(self):
        print("Job : YY")

class Customer(CustomerName, CustomerJob):
    def info(self):
        print("Information: ")
        CustomerName.name(self)
        CustomerJob.job(self)


obj = Customer()
obj.info()