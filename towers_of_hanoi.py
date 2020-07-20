#The following script demonstrates the concepts of recursion.

towers = [[6,4,2,1], [0,0,0,0], [0,0,0,0]]


def display_towers():
    print("\n")
    print("{0}|{0}            {1}|{1}            {2}|{2}            ".format(17*' ',17*' ',17*' '))
    print("{0}{1}|{1}{0}            {2}{3}|{3}{2}            {4}{5}|{5}{4}".format((17-towers[0][3])*' ', towers[0][3]*'=', (17-towers[1][3])*' ', towers[1][3]*'=', (17-towers[2][3])*' ', towers[2][3]*'='))
    print("{0}{1}|{1}{0}            {2}{3}|{3}{2}            {4}{5}|{5}{4}".format((17-towers[0][2])*' ', towers[0][2]*'=', (17-towers[1][2])*' ', towers[1][2]*'=', (17-towers[2][2])*' ', towers[2][2]*'='))
    print("{0}{1}|{1}{0}            {2}{3}|{3}{2}            {4}{5}|{5}{4}".format((17-towers[0][1])*' ', towers[0][1]*'=', (17-towers[1][1])*' ', towers[1][1]*'=', (17-towers[2][1])*' ', towers[2][1]*'='))
    print("{0}{1}|{1}{0}            {2}{3}|{3}{2}            {4}{5}|{5}{4}".format((17-towers[0][0])*' ', towers[0][0]*'=', (17-towers[1][0])*' ', towers[1][0]*'=', (17-towers[2][0])*' ', towers[2][0]*'='))
    print("\n")


def find_open_slot(tower_index):

    tower = towers[tower_index]
    index = 0

    if (tower[-1] != 0):
        raise BufferError('Destination tower is full and cannot hold anymore discs.')
    else:
        disc = tower[index]

        while (disc != 0):

            index += 1
            disc = tower[index]

    return index

def place_disc(tower_index, num):
    index = find_open_slot(tower_index)
    towers[tower_index][index] = num

def pop_tower_disc(tower_num):

    disc  = 0
    tower = towers[tower_num]
    index = len(tower)

    while (disc == 0):
        index -= 1
        disc = tower[index]

    tower[index] = 0
    
    return disc

def move_disc(tower_source, tower_dest):

    disc = pop_tower_disc(tower_source)
    index = find_open_slot(tower_dest)
    towers[tower_dest][index] = disc

def move_tower(N, source, destination, workspace):
    if (N == 1):
        move_disc(source,destination)
    else:
        move_tower(N-1, source, workspace, destination)
        move_disc(source, destination)
        move_tower(N-1, workspace, destination, source)

def play():
    while(True):
        display_towers()
        str_in = input("Where would you like to move the disc? e.g. [0,1]: ")
        move_disc(int(str_in[1]), int(str_in[3]))
        display_towers

def __main__():
    choice = input("Would you like to play or let the computer do it?: ")
    if (choice == 0):
        play()
    else:
        display_towers()
        inp = input("Press enter to solve.")
        move_tower(4, 0, 1, 2)
        display_towers()



__main__()