from lists import all_gen, line_gen, column_gen, sq_gen
from verif import *
from show import show
all = all_gen()
line = line_gen(all)
column = column_gen(line)
square = sq_gen(all)


def backtrack(all):
    count = 0
    index = 0
    n=1
    while True:
        if n == 10:
            all[index] = "E"
            index= index-1
            n = all[index]+1
        if n != 10:
            all[index] = n
        line = line_gen(all)
        column = column_gen(line)
        square = sq_gen(all)
        verif_all = verif_line(line) or verif_column(column) or verif_square(square)
        if verif_all == True:
            n+=1
            if n == 10:
                all[index] = "E"
                index = index - 1
                #print ((all[empty[index-1]], empty[index-1], index-1))
                n = all[index]+1
        else:
            if index !=80:
                index +=1
                n = 1
        if index == 80 and verif_all == False:
            if "E" in all:
                pass
            else:
                show(line)
                all[80] = "E"
                index = 79
                n = all[index]+1
                count +=1
                print(count)
                if count == 6670903752021072936960:
                    break

backtrack(all)
