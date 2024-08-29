size = int (input ("Enter a integer : "))
r, c = 0, 0
boundary = size - 1
sizeLeft = size - 1
flag = 1
move = 'r'
m = [[0 for j in range(size)] for i in range(size)]
for i in range(1, size * size + 1):
    m[r][c] = i
    if move == 'r':
        c += 1
    elif move == 'l':
        c -= 1
    elif move == 'u':
        r -= 1
    elif move == 'd':
        r+= 1
    if i == boundary:
        boundary += sizeLeft
        if flag != 2:
            flag = 2
        else:
            flag = 1
            sizeLeft -= 1
        if move == 'r':
            move = 'd'
        elif move == 'd':
             move = 'l'
        elif move == 'l':
            move = 'u'
        elif move == 'u':
            move = 'r'
for r in range(size):
    for c in range(size):
        n = m[r][c]
        print(n, end='  ' if n < 10 else ' ')
    print()