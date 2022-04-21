"""
Steve Hyland
File Name: lab13.py
Lab Assignment 13 : Capstone, sorts
I did this alone.
"""
#
def star_find(input_file):
    in_nums = []
    infile = open(input_file, "r")
    in_string = infile.read()
    infile.close()
    in_nums = in_string.split()
# now proces the data looking for strong signals (>= 4000 and <= 5000)
    count = 0
    pulses = []
    sig_compares = 0
    indx = 0
#
    for indx in range(len(in_nums)):
        if int(in_nums[indx]) >= 4000 and int(in_nums[indx]) <= 5000:
            count +=1
            pulses.append(in_nums[indx])
            if count == 5:
                break
        sig_compares += 1
        indx +=1
    if count == 5:
        print('pulses found: ', count)
        print('signals', pulses)
        print('signal compares: ', sig_compares)
    else:
        print('pulses found: ', count)
        print('signals', pulses)



#star_find('signals.txt')
