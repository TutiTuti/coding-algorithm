import sys
import pprint
sys.stdin = open("./input/input7.txt", "r")

win = 0
concave = [list(map(int, input().split())) for _ in range(19)]


def x_check(x,y): # 18, 14
    count = 1
    target = concave[x][y]
    next_x = x+1

    while True:
        try:
            if count == 5:
                if next_x != 19:
                    if target != concave[next_x][y]:
                        print(f"{target}\n{x + 1} {y + 1}")
                        return True
                    return False
                print(f"{target}\n{x} {y + 1}")
                return True

            next_value = concave[next_x][y]
            if next_value == target:
                count += 1
                next_x += 1
            else:
                return False
        except:
            return False


def y_check(x,y):
    count = 1
    target = concave[x][y]
    next_y = y + 1

    while True:
        try:

            if count == 5:
                if next_y != 19:
                    if target != concave[x][next_y]:
                        print(f"{target}\n{x + 1} {y + 1}")
                        return True
                    return False
                print(f"{target}\n{x + 1} {y+1}")
                return True

            next_value = concave[x][next_y]

            if next_value == target:
                count += 1
                next_y += 1
            else:
                return False
        except:
            return False


def right_cross_check(x,y):
    count = 1
    target = concave[x][y]
    next_x = x+1
    next_y = y+1

    while True:
        try:


            if count == 5:
                if next_x != 19 and next_y != 19:
                    if target != concave[next_x][next_y]:
                        print(f"{target}\n{x + 1} {y + 1}")
                        return True
                    return False
                print(f"{target}\n{x} {y}")
                return True

            next_value = concave[next_x][next_y]

            if next_value == target:
                count += 1
                next_x += 1
                next_y += 1
            else:
                return False
        except:
            return False


def left_cross_check(x,y):
    count = 1
    target = concave[x][y]
    next_x = x+1
    next_y = y-1
    while True:
        try:


            if count == 5:
                if next_x != 19 and next_y >= 0:
                    if target != concave[next_x][next_y]:
                        print(f"{target}\n{next_x} {next_y+2}")
                        return True
                    return False
                print(f"{target}\n{next_x} {next_y+2}")

                return True

            next_value = concave[next_x][next_y]

            if next_value == target:
                count += 1
                next_x += 1
                next_y -= 1
            else:
                return False
        except:
            return False




result = True
flag = True
x_c = y_c = r_c = l_c =False
for x in range(len(concave)):
    if flag:
        for y in range(len(concave)):
            now_location = concave[x][y]
            if now_location != 0:
                if(x == 0):
                    x_c = x_check(x, y)
                elif concave[x][y] != concave[x-1][y]:
                    x_c = x_check(x, y)

                if (y == 0):
                    y_c = y_check(x, y)
                elif concave[x][y] != concave[x][y-1]:
                    y_c = y_check(x, y)

                if (x==0 or y == 18):
                    l_c = left_cross_check(x, y)
                elif concave[x][y] != concave[x-1][y+1]:
                    l_c = left_cross_check(x, y)

                if (x==0 or y == 0):
                    r_c = right_cross_check(x, y)
                elif concave[x][y] != concave[x-1][y-1]:
                    r_c = right_cross_check(x, y)

                if x_c or y_c or l_c or r_c :
                    # print(x_c,y_c,l_c,r_c)
                    result = False
                    flag = False
                    break

    else:
        break
if result:
    print(0)