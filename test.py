1111111111111
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

queue = ['A']
visited = []

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue.extend(graph[node])
222222222222222
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

stack = ['A']
visited = []

while stack:
    node = stack.pop()
    if node not in visited:
        print(node)
        visited.append(node)
        stack.extend(graph[node])
3333333333333333
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('E', 1)],
    'D': [],
    'E': []
}

queue = [(0, 'A')]   # (cost, node)
visited = []

while queue:
    queue.sort()    # sort by cost
    cost, node = queue.pop(0)

    if node not in visited:
        print(node, cost)
        visited.append(node)

        for neighbor, weight in graph[node]:
            queue.append((cost + weight, neighbor))
444444444444444
import random

board = [' ' for i in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        print("---------")

def check_win(p):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]
    for i in win:
        if board[i[0]] == board[i[1]] == board[i[2]] == p:
            return True
    return False

def player_move():
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == ' ':
        board[pos] = 'X'

def computer_move():
    empty = [i for i in range(9) if board[i] == ' ']
    pos = random.choice(empty)
    board[pos] = 'O'

for turn in range(9):
    print_board()
    
    if turn % 2 == 0:
        player_move()
        if check_win('X'):
            print("Player Wins")
            break
    else:
        computer_move()
        if check_win('O'):
            print("Computer Wins")
            break

print_board()
5555555555555555
def hanoi(n, source, helper, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    
    hanoi(n-1, source, destination, helper)
    print("Move disk", n, "from", source, "to", destination)
    hanoi(n-1, helper, source, destination)

n = 3
hanoi(n, 'A', 'B', 'C')
6666666666666666666
from collections import deque

start = (1,2,3,
         4,0,5,
         7,8,6)

goal = (1,2,3,
        4,5,6,
        7,8,0)

def print_state(state):
    for i in range(0,9,3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_moves(state):
    moves = []
    i = state.index(0)

    swap = {
        0:[1,3], 1:[0,2,4], 2:[1,5],
        3:[0,4,6], 4:[1,3,5,7], 5:[2,4,8],
        6:[3,7], 7:[4,6,8], 8:[5,7]
    }

    for j in swap[i]:
        temp = list(state)
        temp[i], temp[j] = temp[j], temp[i]
        moves.append(tuple(temp))
    
    return moves

queue = deque([(start, [])])
visited = set()

while queue:
    state, path = queue.popleft()

    if state in visited:
        continue

    visited.add(state)

    if state == goal:
        print("Solution Found!\n")
        for step in path + [state]:
            print_state(step)
        break

    for next_state in get_moves(state):
        queue.append((next_state, path + [state]))
7777777777777777
from collections import deque

start = (0, 0)
goal = 2

visited = set()
queue = deque([start])

while queue:
    x, y = queue.popleft()
    
    if (x, y) in visited:
        continue
        
    print(x, y)
    visited.add((x, y))
    
    if x == goal or y == goal:
        print("Goal Reached")
        break

    # possible moves
    queue.append((4, y))   # fill jug1
    queue.append((x, 3))   # fill jug2
    queue.append((0, y))   # empty jug1
    queue.append((x, 0))   # empty jug2
    
    # pour jug1 → jug2
    transfer = min(x, 3 - y)
    queue.append((x - transfer, y + transfer))
    
    # pour jug2 → jug1
    transfer = min(y, 4 - x)
    queue.append((x + transfer, y - transfer))
88888888888888
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(n, row, board):
    if row == n:
        print(board)
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve(n, row + 1, board)

n = 8
board = [-1] * n
solve(n, 0, board)
99999999999999999999
def alphabeta(depth, node, maximizing, values, alpha, beta):
    if depth == 3:
        return values[node]

    if maximizing:
        best = -1000
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            val = alphabeta(depth+1, node*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]

print(alphabeta(0, 0, True, values, -1000, 1000))
