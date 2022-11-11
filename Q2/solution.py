#q2
def areAllValid():
    lines = []
    with open('test.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line[0:len(line)-1])
    # print(lines)

    allValid = True
    errorCodes = []

    for record in range(int(lines[0])):

        current_line_info = lines[record+1].split(" ")

        if current_line_info[1] == 'false':
            allValid = False

        if len(current_line_info) == 3:
            errorCodes.append(current_line_info[2])

        current_line_info.clear()

    if allValid == True:
        print("Yes")
    else:
        print("No")

        for i in range(len(errorCodes)):
            print(errorCodes[i], end=" ")
        print()


if __name__ == '__main__':
    areAllValid()

