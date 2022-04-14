'''
Name: <Steve Hyland>
HW11
sales_person.py

Problem: Fibonacci, Suracuse, etc - Functions, decisions, and graphics

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
#
'''
#
#imported by sales_force
#
class SalesPerson:
    """ class representing a sales person"""
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []
#
    def get_id(self):
        return self.employee_id
#
    def get_name(self):
        return self.name
#
    def set_name(self, name):
        self.name = name
#
    def enter_sale(self, sale):
        self.sales.append(sale)
#
    def total_sales(self):
        sales_total = 0.0
        for indx in range(len(self.sales)):
            sales_total = sales_total + float(self.sales[indx])
        return sales_total
#
    def get_sales(self):
        return self.sales
#
    def met_quota(self, quota):
        tot_sales = self.total_sales()
        fquota = float(quota)
        if tot_sales >= fquota:
            return True
        return False
#
    def compare_to(self, other):
        tot_sales = self.total_sales()
        other_tot = other.total_sales()
        if other_tot > tot_sales:
            return -1
        if other_tot < tot_sales:
            return 1
        return 0
#
    def __str__(self):
        tot_sales = self.total_sales()
        employee_id_chr = str(self.employee_id)
        str_out = employee_id_chr + '-' + self.name + ':' + str(tot_sales)
        return str_out
#
# def my_test():
#     other = SalesPerson(1235,'Trader Joe')
#     sperson = other.get_name()
#     print(sperson)
#     sperson_id = other.get_id()
#     #print(sperson_id)
#     other.enter_sale(150.00)
#     other.enter_sale(200.00)
#     other.enter_sale(125.00)
#     my_sales = SalesPerson(1234,'Steve Hyland')
#     sperson = my_sales.get_name()
#     print(sperson)
#     sperson_id = my_sales.get_id()
#     print(sperson_id)
#     my_sales.enter_sale(150.00)
#     my_sales.enter_sale(200.00)
#     my_sales.enter_sale(123.45)
#     tot_sales = my_sales.total_sales()
#     print(tot_sales)
#     all_sales = my_sales.get_sales()
#     for sale in all_sales:
#         print(sale)
#     good_job = my_sales.met_quota(400.00)
#     print(good_job)
#     did_he = my_sales.compare_to(other)
#     print(did_he)
#     currency = "${:,.2f}".format(tot_sales)
#     print(currency)
#     my_string = my_sales.__str__()
#     print(my_string, currency)
#
#my_test()
