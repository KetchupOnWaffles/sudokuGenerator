out = open("out.txt", 'w+')
def show(line):
    li = ""
    for i in line:
        for j in i:
            li += str(j) + " "
        li += "\n"
    out.write(li)
    out.write("\n")
    showline = "  _ _ _   _ _ _   _ _ _\n"
    showline += "  _ _ _   _ _ _   _ _ _\n"
    showline += "| "
    counter = 0
    counter2 =0
    for i in line:
        for j in i:
            showline+= str(j)
            showline+= " "
            if counter == 2:
                showline += "| "
                counter = 0
            else:
                counter+=1
        showline+="\n"
        if counter2 == 2:
            showline += "  _ _ _   _ _ _   _ _ _\n"
            counter2 = 0
        else:
            counter2 +=1
        showline += "| "
    showline+="\n"
    showline += "  _ _ _   _ _ _   _ _ _\n"
    showline += "  _ _ _   _ _ _   _ _ _\n"

    print(showline)
