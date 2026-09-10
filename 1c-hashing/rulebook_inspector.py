import math

given =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
sudoku_rows = {
    0: {5: 0}
}
sudoku_cols = {}
sudoku_boxes = {}
valid = True
for i in range(9):
    sudoku_rows[i], sudoku_cols[i], sudoku_boxes[i] = {}, {}, {}
for i in range(9):
    for j in range(9):
        if given[i][j] != '.':
            box_number = 3 * math.floor(i/3) + math.floor(j/3)
            box_index = 3 * (i%3) + (j%3)
            c1 = given[i][j] in sudoku_rows[i]
            c2 = given[i][j] in sudoku_cols[j]
            c3 = given[i][j] in sudoku_boxes[box_number]
            if c1 or c2 or c3:
                valid = False
                break
            sudoku_rows[i][int(given[i][j])] = j
            sudoku_cols[j][given[i][j]] = i
            sudoku_boxes[box_number][given[i][j]] = box_index
    if not valid:
        break
print(valid)
