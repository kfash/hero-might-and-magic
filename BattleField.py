import random as rand

class Field:

    def __init__(self):
        self.cell_list = [[0 for i in range(12)] for i in range(12)]
        self.cell = None
        self.biom_list_generation()
        for i in range(12):
            for j in range(12):
                self.cell_list[i][j] = Cell(i, j, self.biom_generation(i, j))

    def biom_list_generation(self):

        global bioms

        bioms = []
        with open('bioms.txt') as input_file:
            for line in input_file:
                bioms += [line.split()]

    def biom_generation(self, x, y):
        global bioms

        biom = ''

        if x == y == 0:
            biom = rand.choice(bioms[1])

        elif (x < 2) or (x > 9):

            if y == 0:
                if (self.cell_list[x - 1][y].biom == 'SpringGreen2') or (self.cell_list[x - 1][y].biom == 'SlateBlue2'):
                    biom = rand.choice(bioms[2])
                if self.cell_list[x - 1][y].biom == 'DarkGoldenrod3':
                    biom = rand.choice(bioms[3])
                if (self.cell_list[x - 1][y].biom == 'gray40') or (self.cell_list[x - 1][y].biom == 'red2'):
                    biom = rand.choice(bioms[4])
                if self.cell_list[x - 1][y].biom == 'azure':
                    biom = rand.choice(bioms[5])

            elif x == 0:
                if (self.cell_list[x][y - 1].biom == 'SpringGreen2'):
                    biom = rand.choice(bioms[2])
                if self.cell_list[x][y - 1].biom == 'DarkGoldenrod3':
                    biom = rand.choice(bioms[3])
                if (self.cell_list[x][y - 1].biom == 'gray40'):
                    biom = rand.choice(bioms[4])
                if self.cell_list[x][y - 1].biom == 'azure':
                    biom = rand.choice(bioms[5])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'SpringGreen2') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'SpringGreen2') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'SpringGreen2'):
                biom = rand.choice(bioms[2])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'DarkGoldenrod3') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'DarkGoldenrod3') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'DarkGoldenrod3'):
                biom = rand.choice(bioms[3])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'gray40') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'gray40') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'gray40'):
                biom = rand.choice(bioms[4])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'azure') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'azure') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'azure'):
                biom = rand.choice(bioms[5])

        else:
            if y == 0:
                if self.cell_list[x - 1][y].biom == 'SpringGreen2':
                    biom = rand.choice(bioms[6])
                if self.cell_list[x - 1][y].biom == 'DarkGoldenrod3':
                    biom = rand.choice(bioms[7])
                if self.cell_list[x - 1][y].biom == 'gray40':
                    biom = rand.choice(bioms[8])
                if self.cell_list[x - 1][y].biom == 'azure':
                    biom = rand.choice(bioms[9])
                if (self.cell_list[x - 1][y].biom == 'SlateBlue2'):
                    biom = rand.choice(bioms[10])
                if self.cell_list[x - 1][y].biom == 'red2':
                    biom = rand.choice(bioms[11])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'SpringGreen2') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'SpringGreen2') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'SpringGreen2'):
                biom = rand.choice(bioms[6])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'DarkGoldenrod3') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'DarkGoldenrod3') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'DarkGoldenrod3'):
                biom = rand.choice(bioms[7])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'gray40') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'gray40') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'gray40'):
                biom = rand.choice(bioms[8])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'azure') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'azure') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'azure'):
                biom = rand.choice(bioms[9])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'SlateBlue2') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'SlateBlue2') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'SlateBlue2'):
                biom = rand.choice(bioms[10])

            elif (self.cell_list[x - 1][y - 1].biom == self.cell_list[x][y - 1].biom == 'red2') or\
                    (self.cell_list[x - 1][y - 1].biom == self.cell_list[x - 1][y].biom == 'red2') or\
                    (self.cell_list[x - 1][y].biom == self.cell_list[x][y-1].biom == 'red2'):
                biom = rand.choice(bioms[11])

            if biom == '':
                biom = rand.choice(bioms[1])

        return biom

    def biom_reset(self):
        for i in range(12):
            for j in range(12):
                self.cell_list[i][j].biom = ''


class Cell:

    def __init__(self, x, y, color):
        self.coordx = x
        self.coordy = y
        self.passability = True
        self.shootability = True
        self.biom = color
        self.id = None
        self.unit = None

