from pathlib import Path

path = Path("input.txt")

N_LINES = 5


def read_input(path):
    with open(path, 'r') as f:
        boards = []
        numbers = list(map(int, f.readline().split(",")))
        curr = []
        for line in f:
            if line == "\n" and len(curr) == 0:
                pass
            elif line == "\n":
                boards.append(curr)
                curr = []
            else:
                curr.append([*map(int, line.strip().split())])
    return numbers, boards


def col_sum(arr, col):
    total = 0
    for i in range(len(arr[0])):
        total += arr[i][col]
    return total


def row_sum(arr, row):
    return sum(arr[row])


def isin(arr, val):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == val:
                return i, j
    return False


def board_sum(arr, to_exclude=-1):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != to_exclude:
                total += arr[i][j]
    return total


# Part 1

numbers, boards = read_input(path)


def bingo(numbers, boards):
    for number in numbers:
        for board in boards:
            if pos := isin(board, number):
                board[pos[0]][pos[1]] = -1
            for i in range(N_LINES):
                if row_sum(board, i) == -N_LINES or \
                   col_sum(board, i) == -N_LINES:
                    return number, board_sum(board)
    return 0, 0


num, b_sum = bingo(numbers, boards)
print(num, b_sum, num * b_sum)

# Part 2


def bingo2(numbers, boards):
    num_last = 0
    board_last = 0
    flips = [0] * len(boards)
    for number in numbers:
        for idx, board in enumerate(boards):
            if flips[idx] != 1:
                if pos := isin(board, number):
                    board[pos[0]][pos[1]] = -1
                for i in range(N_LINES):
                    if row_sum(board, i) == -N_LINES or \
                       col_sum(board, i) == -N_LINES:
                        flips[idx] = 1
                        num_last = number
                        board_last = board

    return num_last, board_sum(board_last)


num2, b_sum2 = bingo2(numbers, boards)
print(num2, b_sum2, num2 * b_sum2)
