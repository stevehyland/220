"""
Steve Hyland
File Name: lab7.py
Lab Assignment 7: File processing - input and output.  If statements.
I did this alone.
"""
def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r" )
    outfile = open(out_file_name, "w")
# read file into a list
    all_grades = infile.readlines()
# process the records one at a time
    class_avg = 0
    good_students = 0
    for idx in range(len(all_grades)):
        student = ""
        student = all_grades[idx].split(":")
        student_grades = student[1].split(" ")
        weight_tot = 0
        grade_tot = 0
        for idn in range(1,len(student_grades),2):
            test_weight = int(student_grades[idn])
            test_score = int(student_grades[idn+1])
            weight_tot = weight_tot + test_weight
            grade_tot = grade_tot + test_weight * test_score
        weighted_grade = grade_tot / 100
        if weight_tot > 100:
            outstring = student[0] + "'s average: Error: The weights are more than 100."
            print(outstring, file = outfile)
        elif weight_tot < 100:
            outstring = student[0] + "'s average: Error: The weights are less than 100."
            print(outstring, file = outfile)
        else:
            class_avg = class_avg + weighted_grade
            good_students = good_students + 1
            outstring = student[0] + "'s average: "
            print(outstring, weighted_grade, file = outfile)
    class_avg = class_avg / good_students
    print("Class average: ", '{0:.1f}'.format(class_avg), file=outfile)
#
    infile.close()
    outfile.close()
#
#weighted_average("grades.txt", "report1.txt")
