'''
Name: <Steve Hyland>
HW11
sales_force.py

Problem: Fibonacci, Suracuse, etc - Functions, decisions, and graphics

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

'''
#
import sales_person
#
class SalesForce:
    """ class representing a sales force"""
#
    def __init__(self):
        self.sales_people = []
#
    def add_data(self, file_name):
        work_list = []
        sales_list = []
        infile = open(file_name, "r")
        my_file = infile.readlines()
        infile.close()
        for idx in range(len(my_file)):
            my_file[idx] = my_file[idx].strip('\n')
# now, instantiate one instance for each person
#  I'm using a separate loop for clarity (mine!)
        for record in my_file:
            new_person = 0
            work_list.clear()
            sales_list.clear()
            work_list = record.split(',')
            work_list[0] = int(work_list[0])
            work_list[1] = work_list[1].lstrip()
            # now add the person
            new_person = sales_person.SalesPerson(work_list[0], work_list[1])
            work_list[2] = work_list[2].lstrip()
            sales_list = work_list[2].split(' ')
            # now add thier sales
            for sale in sales_list:
                fsale = float(sale)
                fsale = round(fsale,2)
                new_person.enter_sale(fsale)
            # now add the object reference to the sales people list
            self.sales_people.append(new_person)
#
    def individual_sales(self, emp_id):
        for person in self.sales_people:
            p_id = person.get_id()
            if p_id == emp_id:
                return person
        return None
#
    def quota_report(self, quota):
        quota_list = []
        quota_work = []
        for sperson in self.sales_people:
            quota_work = []
            empl_id = sperson.get_id()
            empl_name = sperson.get_name()
            quota_work.append(empl_id)
            quota_work.append(empl_name)
            total_sales = sperson.total_sales()
            quota_work.append(total_sales)
            met_quota = sperson.met_quota(quota)
            quota_work.append(met_quota)
            quota_list.append(quota_work)
        return quota_list
#
    def top_seller(self):
        top_amts = []
        top_persons = []
        top_person_objects = []
#
        for person in self.sales_people:
            work_list = []
            person_sales = person.total_sales()
            top_amts.append(person_sales)
            work_list.append(person_sales)
            work_list.append(person)
            top_persons.append(work_list)
        top_amts.sort(reverse=True)
        top_persons.sort(reverse=True)
        top_sales = top_amts[0]
        for indx in range(len(top_persons)):
            temp = []
            temp = top_persons[indx]
            if temp[0] == top_sales:
                top_person_objects.append(temp[1])
        return top_person_objects
#
    def get_sale_frequencies(self):
        sales_list = []
        sales_dict = {}
        for person in self.sales_people:
            sales_list.clear()
            sales_list = person.get_sales()
            for sales_amt in sales_list:
                sales_dict[sales_amt] = sales_dict.get(sales_amt,0) + 1
        return sales_dict
#
    def print_salesmen_sales(self):
        for person in self.sales_people:
            emp_id = person.get_id()
            sales = person.get_sales()
            print(emp_id, sales)

#def my_test():
    #top_sellers = []
    #sales_dict = {}
    #sales_guys = SalesForce() # instantiate class
    #sales_guys.add_data('sales_data.txt')
    #sales_guys.print_salesmen_sales()
    # emp_id = person.get_id
    # who = sales_guys.individual_sales(emp_id)
    # print(who)
    #quota_rpt = sales_guys.quota_report(650.00)
    #print(quota_rpt)
    #sales_dict = sales_guys.get_sale_frequencies()
    #print(sales_dict)
    #top_sellers = sales_guys.top_seller()
    #print('top sellers: ', top_sellers)

#
#my_test()
