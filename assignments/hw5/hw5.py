"""
Name: <your name goes here – first and last>
<hw5>.py

Problem: <String and list processing, conversions to/from, slicing, indexing, etc>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

#
def name_reverse():
    anyname = input("enter a name (first last): ")
    namelist = anyname.split()
    namelist[1] = namelist[1]+","
    print(namelist[1],namelist[0])


def company_name():
    coname_str = input("enter a domain name: ")
    coname_list = coname_str.split(".")
    print(coname_list[1])

#
def initials():

    num_students = eval(input("how many students are in the class?: "))
    student = "what is the name of student x?: "
#
    for idn in range(num_students):
        init_string = ""
        names = []
        string_list = list(student)
        string_list[28] = str(idn + 1)
        senstr = "".join(string_list)
        strg_in = input(senstr)
        names = strg_in.split()
        first_init = "".join(names[0])
        last_init = "".join(names[1])
        init_string = init_string + first_init[0] + last_init[0]
        print(init_string)
#
def names():
    #
    name_str = input(("enter a list of names: "))
    names_in = name_str.split(", ")
    num_names = len(names_in)
    initials_list = ""
    #
    for idn in range(num_names):
        names2 = []
        #print(names[idn])
        names2 = names_in[idn].split()
        first_init = "".join(names2[0])
        last_init = "".join(names2[1])
        initials_list = initials_list + first_init[0] + last_init[0] + " "
    print(initials_list)
#
def thirds():
    #
    num_sen = eval(input("enter the number of sentences: "))
    list1 = []
    sentence = "enter sentence x: "
    #
    for idn in range(num_sen):
        string_list = list(sentence)
        string_list[15] = str(idn+1)
        senstr = "".join(string_list)
        strg_in = input(senstr)
        list1.append(strg_in)
    #
    for isen in range(0,num_sen):
        sentence = list1[isen]
        strlen = len(sentence)
        for idx in range(0,strlen,3):
            print(sentence[idx],end="")
        print('')
#
#
def word_average():
    string_in = input("enter a sentence: ")
    words = string_in.split()
    num_words = len(words)
    tot_letters = 0
    for iwords in range(num_words):
        tot_letters = tot_letters + len(words[iwords])
    avg = tot_letters/(num_words)
    print(avg)
#
def pig_latin():
    sentence = input("input a sentence to convert to pig latin: ")
    list1 = sentence.split()
    num_words = len(list1)
    for iwords in range(num_words):
        len_word = len(list1[iwords])
        work_str = list1[iwords]
        new_str = work_str[1:len_word] + work_str[0] + "ay"
        list1[iwords] = new_str
    pig_out = " ".join(list1)
    low_pig = pig_out.lower()
    print(low_pig)
#
if __name__ == '__main__':
    pass
#name_reverse()
#company_name()
#initials()
#names()
#thirds()
#word_average()
#pig_latin()
#
