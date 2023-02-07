def checkered ():
    column = int(input("Enter the vertical number"))
    row = int(input("Enter the Horizontal number"))
    matrix = []
    for x in range(column):
        a = []
        b = []
        for y in range(row):
            a.append("*")
            a.append("#")
            b.append("*")
            b.append("#")

            matrix.append(a)
            matrix.append(b)

    for x in range(column):
        for y in range(row):

            print(matrix[x][y], end = "")

        print()

checkered()