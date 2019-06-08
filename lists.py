def all_gen():
    all = list()
    for i in range(81):
        all.append("E")
    return all
def line_gen(all):
    subl = list()
    l = list()
    for i in range(9):
        for j in range(9):
            subl.append(all[(i*9)+j])
        l.append(subl)
        subl = list()
    return l
def column_gen(line):
    subc = list()
    c = list()
    for i in range(9):
        for j in range(9):
            subc.append(line[j][i])
        c.append(subc)
        subc= list()
    return c
def sq_gen(all):
    subsquare = list()
    square = list()
    count = 0
    for i in range(3):
        for j in range(9):
            for k in range(3):
                subsquare.append(all[(j*9)+(k+(i*3))])
                count+=1
                if count == 9:
                    square.append(subsquare)
                    subsquare = list()
                    count = 0
        subsquare = list()
    square[1], square[3] = square[3], square[1]
    square[2], square[6] = square[6], square[2]
    square[5], square[7] = square[7], square[5]
    return square
