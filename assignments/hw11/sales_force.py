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
import sales_person
#
#def mysort_func(amt):
    #return work_list[1]
class SalesForce:
#
    def __init__(self):
        self.sales_people = []
#
    def add_data(self, file_name):
        work_list = []
        sales_list = []
        infile = open(file_name, "r")
        #self.sales_people = infile.readlines()
        my_file = infile.readlines()
        infile.close()

        for idx in range(len(my_file)):
            my_file[idx] = my_file[idx].strip('\n')
# now, instantiate one instance for each person
#  I'm using a separate loop for clarity (mine!)
        for record in (my_file):
            new_person = 0
            work_list.clear()
            sales_list.clear()
            work_list = record.split(',')
            work_list[0] = int(work_list[0])
            #work_list[0] = temp_int
            work_list[1] = work_list[1].lstrip()
            print(type(work_list[0]), type(work_list[1]))
            # now add the person
            new_person = sales_person.SalesPerson(work_list[0], work_list[1])
            work_list[2] = work_list[2].lstrip()
            sales_list = work_list[2].split(' ')
            # now add thier sales
            for sale in (sales_list):
                fsale = float(sale)
                fsale = round(fsale,2)
                new_person.enter_sale(fsale)
            # now add the object reference to the sales people list
            self.sales_people.append(new_person)
        #print(self.sales_people)
        # for persona in (self.sales_people):
        #     p_id = persona.get_id()
        #     p_nombre = persona.get_name()
        #     p_sales = persona.get_sales()
        #     print(p_id, p_nombre, p_sales)
#
    def individual_sales(self, emp_id):
        if type(emp_id) != int:
            c_emp_id = int(emp_id)
        else:
            c_emp_id = emp_id

        print('emp id: ', c_emp_id)
        emp_rec =  []
        for person in (self.sales_people):
            #print('person: ', person)
            p_id = person.get_id()
            #print(type(p_id), p_id)
            if p_id == emp_id:
                p_nombre = person.get_name()
                print('Ind Sales: ', p_id, p_nombre)
                return person
        return None
#
    def quota_report(self, quota):
        quota_list = []
        quota_work = []
        work_list = []
        sales_list = []
        #result = False
        for sales_person in (self.sales_people):
            #print('person: ', sales_person)
            quota_work.clear()
            empl_id = sales_person.get_id()
            empl_name = sales_person.get_name()
            quota_work.append(empl_id)
            quota_work.append(empl_name)
            total_sales = sales_person.total_sales()
            #print(empl_id, empl_name, total_sales)
            quota_work.append(total_sales)
            met_quota = sales_person.met_quota(650)
            quota_work.append(met_quota)
            print('quota_work before append: ', quota_work)
            print('quota_list before append', quota_list)
            quota_list.append(quota_work)
            #quota_list.insert(0,quota_work)
            print('quota_work after append: ', quota_work)
            print('quota_list after append', quota_list)
            print()
        # for idx in range(len(quota_list)):
        #     print(quota_list[idx])
        return quota_list
#
    def top_seller(self):
        top_amts = []
        top_persons = []
        work_list = []
        top_sales = 0.00
        temp = []
#
        for person in (self.sales_people):
            work_list.clear()
            temp.clear()
            person_sales = person.total_sales()
            top_amts.append(person_sales)
            work_list.append(person)
            work_list.append(person_sales)
            top_persons.append(work_list)
        print(work_list)
        print('top_amts: ', top_amts)
        top_amts.sort(reverse=True)
        print('top_amt sorted:', top_amts)
        top_sales = top_amts[0]
        print('top_sales: ', top_sales)
        for indx in range(len(top_persons)):
            temp.clear()
            temp = top_persons[indx]
            print('temp: ', temp)
            print('temp len: ', len(temp))
            if temp[1] < top_sales:
                poped = top_persons.pop(indx)
                print('poped', poped)
        print(top_persons)
        return top_persons
#
    def get_sale_frequencies(self):
        work_list = []
        sales_list = []
        sales_dict = {}
        #result = False
        for person in (self.sales_people):
            sales_list.clear()
            sales_list = person.get_sales()
            for sales_amt in sales_list:
                sales_dict[sales_amt] = sales_dict.get(sales_amt,0) + 1
        return sales_dict
#
    def print_salesmen_sales(self):
        for person in (self.sales_people):
            emp_id = person.get_id()
            sales = person.get_sales()
            print(emp_id, sales)

def my_test():
    top_sellers = []
    sales_dict = {}
    sales_guys = SalesForce() # instantiate class
    sales_guys.add_data('sales_data.txt')
    sales_guys.print_salesmen_sales()
    # emp_id = person.get_id
    # who = sales_guys.individual_sales(emp_id)
    # print(who)
    quota_rpt = sales_guys.quota_report(650.00)
    #sales_dict = sales_guys.get_sale_frequencies()
    #print(sales_dict)
    #top_sellers = sales_guys.top_seller()
    #print('top sellers: ', top_sellers)

#
my_test()
