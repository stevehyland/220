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
import math
class SalesForce:
#
    def __init__(self):
        self.sales_people = []
#
    def add_data(self, file_name):
        infile = open(file_name, "r")
        self.sales_people =infile.readlines()
#
        for idx in range(len(self.sales_people)):
            self.sales_people[idx] = self.sales_people[idx].strip('\n')
        # for xyz in self.sales_people:
        #     print('Sales People ', xyz)
        infile.close()
#
    def quota_report(self, quota):
        quota_list = []
        quota_work = []
        work_list = []
        sales_list = []
        result = False
        for idx in range(len(self.sales_people)):
            print('number of records: ', len(self.sales_people), 'processing: ', (idx + 1))
            sales = 0.0
            work_list.clear()
            quota_work.clear()
            sales_list.clear()
            work_list = self.sales_people[idx].split(',')
            #print('work list entries: ', len(work_list))
            quota_work.append(work_list[0]) # emp Id
            quota_work.append(work_list[1]) # emp name
            #print(quota_work)
            work_list[2] = work_list[2].lstrip()
            sales_list = work_list[2].split(' ')
            #print(len(sales_list))
            for idn in range(len(sales_list)):
                fsales = float(sales_list[idn])
                sales = sales + fsales
            #print(sales)
            if sales >= quota:
                result = True
            else:
                result = False
#
            quota_work.append(sales)
            quota_work.append(result)
            print('quota_work before append:', quota_work)
            quota_list.append(quota_work)
            #quota_list.extend(quota_work)
            #quota_list.insert(0, quota_work)
            print('quota_list after append: ', quota_list)
        for entry in quota_list:
            print('end of loop: ', entry)
        return quota_list
#
    def top_seller(self):
        top_sales = 0.0
        top_persons = []
        for idx in range(len(self.sales_people)):
            person = self.sales_people[idx].split(',')
            ind_sales = self.individual_sales(person[0])
            if ind_sales != None:
                quota_data = self.quota_report(0.00)
        return
#
    def individual_sales(self, emp_id):
        emp_rec =  []
        for idx in range(len(self.sales_people)):
            emp_rec = self.sales_people[idx].split(',')
            if emp_rec[0] == emp_id:
                return self.sales_people[idx]
        return None
#
    def get_sale_frequencies(self):
        work_list = []
        sales_list = []
        sales_dict = {}
        #result = False
        for idx in range(len(self.sales_people)):
            sales_list.clear()
            work_list = self.sales_people[idx].split(',')
            work_list[2] = work_list[2].lstrip()
            sales_list = work_list[2].split(' ')
            for sales_amt in sales_list:
                sales_dict[sales_amt] = sales_dict.get(sales_amt,0) + 1
        return sales_dict
def my_test():
    top_sellers = []
    my_dict = {}
    sales_guys = SalesForce() # instantiate class
    sales_guys.add_data('sales_data.txt')
    # emp = sales_guys.individual_sales('123')
    # print(emp)
    # emp = sales_guys.individual_sales('567')
    # print(emp)
    # emp = sales_guys.individual_sales('890')
    # # print(emp)
    sales_quota_rpt = sales_guys.quota_report(float(650.00))
    for line in (sales_quota_rpt):
        print(line)
    # print(len(sales_quota_rpt))
    # top_sellers = sales_guys.top_seller()
    # for idx in range(len(top_sellers)):
    #     print(top_sellers[idx])
    # sales_person = sales_guys.individual_sales('345')
    # if sales_person != None:
    #     print('sales person: ', sales_person)
    # else: print('sales_person does not exist.')
    # sales_person = sales_guys.individual_sales('789')
    # if sales_person != None:
    #     print('sales person: ', sales_person)
    # else: print('sales_person does not exist.')
    # my_dict = sales_guys.get_sale_frequencies()
    # print(my_dict)
    # for sales in my_dict:
    #     print(sales, my_dict[sales])
#
my_test()
