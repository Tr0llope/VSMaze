from tkinter import *

def focus(event):
    frame.focus_set()

def playAgainCommand():
    frame.pack()
    endMessage.pack_forget()
    closeButton.pack_forget()
    playAgain.pack_forget()
    for x in range(2):
        list_carre_h_all[list_characters[x].grid_id] = []
        list_carre_v_all[list_characters[x].grid_id] = []
        list_state_h_all[list_characters[x].grid_id] = []
        list_state_v_all[list_characters[x].grid_id] = []
        list_characters[x].level = 0
        create_grid(0, 0, list_characters[x].grid_id*12, list_characters[x].grid_id, list_characters[x].level)
        list_characters[x].pos_x = (list_characters[x].origin%10 + list_characters[x].grid_id*12)*50 + 20
        list_characters[x].pos_y = list_characters[x].origin//10*50 + 20
        list_characters[x].case = 0
        list_characters[x].refresh()



class mur:
    def __init__(self, grid_id, state, orientation, num_grid):
        self.orientation = orientation
        self.solid = state
        self.num_grid = num_grid
        if self.orientation == 'v':
            self.a = ((grid_id%10 + self.num_grid)*50)
            self.b = ((grid_id//10)*50)+5
            self.c = self.a + 5
            self.d = self.b + 45
            self.id = frame.create_rectangle(self.a, self.b, self.c, self.d, width = 0)
        elif self.orientation == 'h':
            self.a = ((grid_id%10 + self.num_grid)*50)+5
            self.b = ((grid_id//10)*50)
            self.c = self.a + 45
            self.d = self.b + 5
            self.id = frame.create_rectangle(self.a, self.b, self.c, self.d, width = 0)

    def refresh(self):
        if self.solid == 1:
            frame.itemconfig(self.id, fill = 'black')
        elif self.solid == 0:
            frame.itemconfig(self.id, fill = 'white')




class character:
    def __init__(self, color, origin, decalage, grid_id, name):
        self.name = name
        self.origin = origin
        self.level = 0
        self.grid_id = grid_id
        self.pos_x = (origin%10 + decalage)*50 + 20
        self.pos_y = origin//10*50 + 20
        self.case = 0
        self.color = color
        self.id = frame.create_rectangle(self.pos_x, self.pos_y, self.pos_x + 15, self.pos_y + 15, width = 0, fill = self.color)
    def up(self, event):
        self.deplace('up')
    def down(self, event):
        self.deplace('down')
    def left(self, event):
        self.deplace('left')
    def right(self, event):
        self.deplace('right')
    def deplace(self, direction):
        if direction == 'up' and list_carre_h_all[self.grid_id][self.case].solid != 1:
            self.pos_y -= 50
            self.case -= 10
            self.refresh()
        elif direction == 'down' and list_carre_h_all[self.grid_id][self.case+10].solid != 1:
            self.pos_y += 50
            self.case += 10
            self.refresh()
        elif direction == 'right' and list_carre_v_all[self.grid_id][self.case+1].solid != 1:
            self.pos_x += 50
            self.case += 1
            self.refresh()
        elif direction == 'left' and list_carre_v_all[self.grid_id][self.case].solid != 1:
            self.pos_x -= 50
            self.case -= 1
            self.refresh()
    def ifWinTrue(self):
        if self.case == 88:
            if self.level < 4:
                list_carre_h_all[self.grid_id] = []
                list_carre_v_all[self.grid_id] = []
                list_state_h_all[self.grid_id] = []
                list_state_v_all[self.grid_id] = []
                self.level+= 1
                create_grid(0, 0, self.grid_id*12, self.grid_id, self.level)
                self.pos_x = (self.origin%10 + self.grid_id*12)*50 + 20
                self.pos_y = self.origin//10*50 + 20
                self.case = 0
                self.refresh()
            else:
                name = self.name
                print(name)
                frame.pack_forget()
                endMessage.pack()
                closeButton.pack()
                playAgain.pack()
        else:
            pass
    def refresh(self):
        self.ifWinTrue()
        frame.coords(self.id, self.pos_x, self.pos_y, self.pos_x + 15, self.pos_y + 15)
    






root = Tk()
root.title('VS Maze')
frame = Canvas(root, width = 1100, height = 600, bg = 'white')
frame.pack()
endMessage = Label(root, text = 'Game Over !!!')
closeButton = Button(root, text = 'Close', command = root.destroy)
playAgain = Button(root, text  = 'play again', command = playAgainCommand)
list_carre_h = []
list_carre_v = []
list_state_h = []
list_state_v = []

list_carre_h_2 = []
list_carre_v_2 = []
list_state_h_2 = []
list_state_v_2 = []

list_carre_h_all = [list_carre_h, list_carre_h_2]
list_carre_v_all = [list_carre_v, list_carre_v_2]
list_state_h_all = [list_state_h, list_state_h_2]
list_state_v_all = [list_state_v, list_state_v_2]

list_levels = ['grid1.txt', 'grid2.txt', 'grid3.txt', 'grid4.txt', 'grid5.txt']


def create_grid(x, y, decalage, list_id, grid_id):
    file = open(list_levels[grid_id], 'r')

    for x in range(100):
        list_state_h_all[list_id].append(int(file.read(1)))
        blank = file.read(1)
    line_return = file.read(1)

    for x in range(100):
        list_state_v_all[list_id].append(int(file.read(1)))
        blank = file.read(1)

    file.close()

    for x in range(100):
        list_carre_h_all[list_id].append(mur(x, list_state_h_all[list_id][x], 'h', decalage))
        list_carre_h_all[list_id][x].refresh()
    for x in range(100):
        list_carre_v_all[list_id].append(mur(x, list_state_v_all[list_id][x], 'v', decalage))
        list_carre_v_all[list_id][x].refresh()
    
    def case_fin(case_num):
        a = ((case_num)%10)*50 + 5 + (list_id*12)*50
        b = ((case_num)//10)*50 + 5
        c = a + 45
        d = b + 45
        fin = frame.create_rectangle(a, b, c, d, fill = 'green', width = 0)
    case_fin(88)

    def piliers(decalage):
        liste_pilier = []
        for k in range (100):
            colonne=k%10
            ligne=k//10
            a=(0 + (colonne+decalage)*50)
            b=(0 + (ligne)*50)
            c=(a+5)
            d=(b+5)
            liste_pilier.append(frame.create_rectangle(a,b,c,d, fill="black", width = 0))
    piliers(decalage)

create_grid(0, 0, 0, 0, 0)
create_grid(0, 0, 12, 1, 0)


perso = character('red', 0, 12, 1, 'red')
perso2 = character('blue', 0, 0, 0, 'blue')
list_characters = [perso, perso2]


frame.bind('<Button-1>', focus)
frame.bind('<Up>', perso.up)
frame.bind('<Down>', perso.down)
frame.bind('<Left>', perso.left)
frame.bind('<Right>', perso.right)
frame.bind('<z>', perso2.up)
frame.bind('<s>', perso2.down)
frame.bind('<q>', perso2.left)
frame.bind('<d>', perso2.right)


root.mainloop()
