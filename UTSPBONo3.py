from abc import ABC, abstractmethod

# Membuat interface 'Payable'
class Payable(ABC):
    @abstractmethod
    def getPaymentAmount(self):
        pass

# Subclass 'Employee' yang mengimplementasikan 'Payable'
class Employee(Payable):
    def __init__(self, first_name, last_name, social_security_number):
        self.first_name = first_name
        self.last_name = last_name
        self.social_security_number = social_security_number

    def getPaymentAmount(self):
        pass  # Nantinya diimplementasikan oleh subclass

# Subclass 'Invoice' yang mengimplementasikan 'Payable'
class Invoice(Payable):
    def __init__(self, part_number, part_description, price_per_item):
        self.part_number = part_number
        self.part_description = part_description
        self.price_per_item = price_per_item
        

    def getPaymentAmount(self):
        return self.price_per_item

# Subclass 'CommissionEmployee' yang merupakan subclass dari 'Employee'
class CommissionEmployee(Employee):
    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate):
        super().__init__(first_name, last_name, social_security_number)
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    def getPaymentAmount(self):
        return self.gross_sales * (self.commission_rate / 100)

# Subclass 'HourlyEmployee' yang merupakan subclass dari 'Employee'
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, social_security_number, wage, hours):
        super().__init__(first_name, last_name, social_security_number)
        self.wage = wage
        self.hours = hours

    def getPaymentAmount(self):
        return self.wage * self.hours

# Subclass 'SalariedEmployee' yang merupakan subclass dari 'Employee'
class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, social_security_number, weekly_salary):
        super().__init__(first_name, last_name, social_security_number)
        self.weekly_salary = weekly_salary

    def getPaymentAmount(self):
        return self.weekly_salary

# Subclass 'BasePlusCommissionEmployee' yang merupakan subclass dari 'CommissionEmployee'
class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, social_security_number, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, social_security_number, gross_sales, commission_rate)
        self.base_salary = base_salary

    def getPaymentAmount(self):
        return super().getPaymentAmount() + self.base_salary

# Contoh penggunaan:
if __name__ == "__main__":
    commission_employee = CommissionEmployee("Yosan", "Yogi", "123-45-6789", 10000, 10)
    hourly_employee = HourlyEmployee("Farrel", "Navyansyah", "987-65-4321", 20, 40)
    salaried_employee = SalariedEmployee("Dipsi", "Lala", "555-12-3456", 800)
    base_plus_commission_employee = BasePlusCommissionEmployee("Ada", "Wong", "777-88-9999", 5000, 5, 1000)
    invoice = Invoice("12345", "Widget", 10.0)

    employees = [commission_employee, hourly_employee, salaried_employee, base_plus_commission_employee]

    for employee in employees:
        print(f"{employee.first_name} {employee.last_name} Payment: ${employee.getPaymentAmount():.2f}")

    print(f"Invoice Payment: ${invoice.getPaymentAmount():.2f}")