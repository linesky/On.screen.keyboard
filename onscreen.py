import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


keyss=[]
bottomframe=None
class BareboneBuilder:
    def __init__(self, root):
        global keyss
        i:int=0
        self.root = root
        self.root.title("view")
        frame = Frame(self.root)
        frame.pack()
        # Janela amarela
        self.root.configure(bg='red')
        self.topframe = Frame(frame,bg='red')
        self.topframe.pack( side = TOP )

        self.bottomframe = Frame(frame,bg='red')
        self.bottomframe.pack( side = BOTTOM )
        self.text_area = tk.Text(self.root, height=25, width=80,bg='red')
        self.text_area.pack(pady=5)

        # Botões
        for n in range(100):
            keyss=keyss+[""]
        keyss[0]=tk.Button(self.bottomframe, text='\\',command=lambda:self.ckeyss('\\') ,borderwidth=1,bg='red').grid(row=0, column=0)

        keyss[1]=tk.Button(self.bottomframe, text='1',command=lambda:self.ckeyss('1') ,borderwidth=1,bg='red').grid(row=0, column=1)

        keyss[2]=tk.Button(self.bottomframe, text='2',command=lambda:self.ckeyss('2') ,borderwidth=1,bg='red').grid(row=0, column=2)

        keyss[3]=tk.Button(self.bottomframe, text='3',command=lambda:self.ckeyss('3') ,borderwidth=1,bg='red').grid(row=0, column=3)

        keyss[4]=tk.Button(self.bottomframe, text='4',command=lambda:self.ckeyss('4') ,borderwidth=1,bg='red').grid(row=0, column=4)

        keyss[5]=tk.Button(self.bottomframe, text='5',command=lambda:self.ckeyss('5') ,borderwidth=1,bg='red').grid(row=0, column=5)

        keyss[6]=tk.Button(self.bottomframe, text='6',command=lambda:self.ckeyss('6') ,borderwidth=1,bg='red').grid(row=0, column=6)

        keyss[7]=tk.Button(self.bottomframe, text='7',command=lambda:self.ckeyss('7') ,borderwidth=1,bg='red').grid(row=0, column=7)

        keyss[8]=tk.Button(self.bottomframe, text='8',command=lambda:self.ckeyss('8') ,borderwidth=1,bg='red').grid(row=0, column=8)

        keyss[9]=tk.Button(self.bottomframe, text='9',command=lambda:self.ckeyss('9') ,borderwidth=1,bg='red').grid(row=0, column=9)

        keyss[10]=tk.Button(self.bottomframe, text='0',command=lambda:self.ckeyss('0') ,borderwidth=1,bg='red').grid(row=0, column=10)

        keyss[11]=tk.Button(self.bottomframe, text='«',command=lambda:self.ckeyss('«') ,borderwidth=1,bg='red').grid(row=0, column=11)

        keyss[12]=tk.Button(self.bottomframe, text='|',command=lambda:self.ckeyss('|') ,borderwidth=1,bg='red').grid(row=1, column=0)

        keyss[13]=tk.Button(self.bottomframe, text='!',command=lambda:self.ckeyss('!') ,borderwidth=1,bg='red').grid(row=1, column=1)

        keyss[14]=tk.Button(self.bottomframe, text='#',command=lambda:self.ckeyss('#') ,borderwidth=1,bg='red').grid(row=1, column=2)

        keyss[15]=tk.Button(self.bottomframe, text='$',command=lambda:self.ckeyss('$') ,borderwidth=1,bg='red').grid(row=1, column=3)

        keyss[16]=tk.Button(self.bottomframe, text='%',command=lambda:self.ckeyss('%') ,borderwidth=1,bg='red').grid(row=1, column=4)

        keyss[17]=tk.Button(self.bottomframe, text='&',command=lambda:self.ckeyss('&') ,borderwidth=1,bg='red').grid(row=1, column=5)

        keyss[18]=tk.Button(self.bottomframe, text='/',command=lambda:self.ckeyss('/') ,borderwidth=1,bg='red').grid(row=1, column=6)

        keyss[19]=tk.Button(self.bottomframe, text='(',command=lambda:self.ckeyss('(') ,borderwidth=1,bg='red').grid(row=1, column=7)

        keyss[20]=tk.Button(self.bottomframe, text=')',command=lambda:self.ckeyss(')') ,borderwidth=1,bg='red').grid(row=1, column=8)

        keyss[21]=tk.Button(self.bottomframe, text='=',command=lambda:self.ckeyss('=') ,borderwidth=1,bg='red').grid(row=1, column=9)

        keyss[22]=tk.Button(self.bottomframe, text='?',command=lambda:self.ckeyss('?') ,borderwidth=1,bg='red').grid(row=1, column=10)

        keyss[23]=tk.Button(self.bottomframe, text='»',command=lambda:self.ckeyss('»') ,borderwidth=1,bg='red').grid(row=1, column=11)

        keyss[24]=tk.Button(self.bottomframe, text='    ',command=lambda:self.ckeyss('  ') ,borderwidth=1,bg='red').grid(row=2, column=0)

        keyss[25]=tk.Button(self.bottomframe, text='q',command=lambda:self.ckeyss('q') ,borderwidth=1,bg='red').grid(row=2, column=1)

        keyss[26]=tk.Button(self.bottomframe, text='w',command=lambda:self.ckeyss('w') ,borderwidth=1,bg='red').grid(row=2, column=2)

        keyss[27]=tk.Button(self.bottomframe, text='e',command=lambda:self.ckeyss('e') ,borderwidth=1,bg='red').grid(row=2, column=3)

        keyss[28]=tk.Button(self.bottomframe, text='r',command=lambda:self.ckeyss('r') ,borderwidth=1,bg='red').grid(row=2, column=4)

        keyss[29]=tk.Button(self.bottomframe, text='t',command=lambda:self.ckeyss('t') ,borderwidth=1,bg='red').grid(row=2, column=5)

        keyss[30]=tk.Button(self.bottomframe, text='y',command=lambda:self.ckeyss('y') ,borderwidth=1,bg='red').grid(row=2, column=6)

        keyss[31]=tk.Button(self.bottomframe, text='u',command=lambda:self.ckeyss('u') ,borderwidth=1,bg='red').grid(row=2, column=7)

        keyss[32]=tk.Button(self.bottomframe, text='i',command=lambda:self.ckeyss('i') ,borderwidth=1,bg='red').grid(row=2, column=8)

        keyss[33]=tk.Button(self.bottomframe, text='o',command=lambda:self.ckeyss('o') ,borderwidth=1,bg='red').grid(row=2, column=9)

        keyss[34]=tk.Button(self.bottomframe, text='p',command=lambda:self.ckeyss('p') ,borderwidth=1,bg='red').grid(row=2, column=10)

        keyss[35]=tk.Button(self.bottomframe, text='+',command=lambda:self.ckeyss('+') ,borderwidth=1,bg='red').grid(row=2, column=11)

        keyss[36]=tk.Button(self.bottomframe, text='´',command=lambda:self.ckeyss('´') ,borderwidth=1,bg='red').grid(row=3, column=0)

        keyss[37]=tk.Button(self.bottomframe, text='~',command=lambda:self.ckeyss('~') ,borderwidth=1,bg='red').grid(row=3, column=1)

        keyss[38]=tk.Button(self.bottomframe, text='Q',command=lambda:self.ckeyss('Q') ,borderwidth=1,bg='red').grid(row=3, column=2)

        keyss[39]=tk.Button(self.bottomframe, text='W',command=lambda:self.ckeyss('W') ,borderwidth=1,bg='red').grid(row=3, column=3)

        keyss[40]=tk.Button(self.bottomframe, text='E',command=lambda:self.ckeyss('E') ,borderwidth=1,bg='red').grid(row=3, column=4)

        keyss[41]=tk.Button(self.bottomframe, text='R',command=lambda:self.ckeyss('R') ,borderwidth=1,bg='red').grid(row=3, column=5)

        keyss[42]=tk.Button(self.bottomframe, text='T',command=lambda:self.ckeyss('T') ,borderwidth=1,bg='red').grid(row=3, column=6)

        keyss[43]=tk.Button(self.bottomframe, text='Y',command=lambda:self.ckeyss('Y') ,borderwidth=1,bg='red').grid(row=3, column=7)

        keyss[44]=tk.Button(self.bottomframe, text='U',command=lambda:self.ckeyss('U') ,borderwidth=1,bg='red').grid(row=3, column=8)

        keyss[45]=tk.Button(self.bottomframe, text='I',command=lambda:self.ckeyss('I') ,borderwidth=1,bg='red').grid(row=3, column=9)

        keyss[46]=tk.Button(self.bottomframe, text='O',command=lambda:self.ckeyss('O') ,borderwidth=1,bg='red').grid(row=3, column=10)

        keyss[47]=tk.Button(self.bottomframe, text='P',command=lambda:self.ckeyss('P') ,borderwidth=1,bg='red').grid(row=3, column=11)

        keyss[48]=tk.Button(self.bottomframe, text='*',command=lambda:self.ckeyss('*') ,borderwidth=1,bg='red').grid(row=4, column=0)

        keyss[49]=tk.Button(self.bottomframe, text='`',command=lambda:self.ckeyss('`') ,borderwidth=1,bg='red').grid(row=4, column=1)

        keyss[50]=tk.Button(self.bottomframe, text='^',command=lambda:self.ckeyss('^') ,borderwidth=1,bg='red').grid(row=4, column=2)

        keyss[51]=tk.Button(self.bottomframe, text='a',command=lambda:self.ckeyss('a') ,borderwidth=1,bg='red').grid(row=4, column=3)

        keyss[52]=tk.Button(self.bottomframe, text='s',command=lambda:self.ckeyss('s') ,borderwidth=1,bg='red').grid(row=4, column=4)

        keyss[53]=tk.Button(self.bottomframe, text='d',command=lambda:self.ckeyss('d') ,borderwidth=1,bg='red').grid(row=4, column=5)

        keyss[54]=tk.Button(self.bottomframe, text='f',command=lambda:self.ckeyss('f') ,borderwidth=1,bg='red').grid(row=4, column=6)

        keyss[55]=tk.Button(self.bottomframe, text='g',command=lambda:self.ckeyss('g') ,borderwidth=1,bg='red').grid(row=4, column=7)

        keyss[56]=tk.Button(self.bottomframe, text='h',command=lambda:self.ckeyss('h') ,borderwidth=1,bg='red').grid(row=4, column=8)

        keyss[57]=tk.Button(self.bottomframe, text='j',command=lambda:self.ckeyss('j') ,borderwidth=1,bg='red').grid(row=4, column=9)

        keyss[58]=tk.Button(self.bottomframe, text='k',command=lambda:self.ckeyss('k') ,borderwidth=1,bg='red').grid(row=4, column=10)

        keyss[59]=tk.Button(self.bottomframe, text='l',command=lambda:self.ckeyss('l') ,borderwidth=1,bg='red').grid(row=4, column=11)

        keyss[60]=tk.Button(self.bottomframe, text='A',command=lambda:self.ckeyss('A') ,borderwidth=1,bg='red').grid(row=5, column=0)

        keyss[61]=tk.Button(self.bottomframe, text='S',command=lambda:self.ckeyss('S') ,borderwidth=1,bg='red').grid(row=5, column=1)

        keyss[62]=tk.Button(self.bottomframe, text='D',command=lambda:self.ckeyss('D') ,borderwidth=1,bg='red').grid(row=5, column=2)

        keyss[63]=tk.Button(self.bottomframe, text='F',command=lambda:self.ckeyss('F') ,borderwidth=1,bg='red').grid(row=5, column=3)

        keyss[64]=tk.Button(self.bottomframe, text='G',command=lambda:self.ckeyss('G') ,borderwidth=1,bg='red').grid(row=5, column=4)

        keyss[65]=tk.Button(self.bottomframe, text='H',command=lambda:self.ckeyss('H') ,borderwidth=1,bg='red').grid(row=5, column=5)

        keyss[66]=tk.Button(self.bottomframe, text='J',command=lambda:self.ckeyss('J') ,borderwidth=1,bg='red').grid(row=5, column=6)

        keyss[67]=tk.Button(self.bottomframe, text='K',command=lambda:self.ckeyss('K') ,borderwidth=1,bg='red').grid(row=5, column=7)

        keyss[68]=tk.Button(self.bottomframe, text='L',command=lambda:self.ckeyss('L') ,borderwidth=1,bg='red').grid(row=5, column=8)

        keyss[69]=tk.Button(self.bottomframe, text='z',command=lambda:self.ckeyss('z') ,borderwidth=1,bg='red').grid(row=5, column=9)

        keyss[70]=tk.Button(self.bottomframe, text='x',command=lambda:self.ckeyss('x') ,borderwidth=1,bg='red').grid(row=5, column=10)

        keyss[71]=tk.Button(self.bottomframe, text='c',command=lambda:self.ckeyss('c') ,borderwidth=1,bg='red').grid(row=5, column=11)

        keyss[72]=tk.Button(self.bottomframe, text='v',command=lambda:self.ckeyss('v') ,borderwidth=1,bg='red').grid(row=6, column=0)

        keyss[73]=tk.Button(self.bottomframe, text='b',command=lambda:self.ckeyss('b') ,borderwidth=1,bg='red').grid(row=6, column=1)

        keyss[74]=tk.Button(self.bottomframe, text='n',command=lambda:self.ckeyss('n') ,borderwidth=1,bg='red').grid(row=6, column=2)

        keyss[75]=tk.Button(self.bottomframe, text='m',command=lambda:self.ckeyss('m') ,borderwidth=1,bg='red').grid(row=6, column=3)

        keyss[76]=tk.Button(self.bottomframe, text=',',command=lambda:self.ckeyss(',') ,borderwidth=1,bg='red').grid(row=6, column=4)

        keyss[77]=tk.Button(self.bottomframe, text='.',command=lambda:self.ckeyss('.') ,borderwidth=1,bg='red').grid(row=6, column=5)

        keyss[78]=tk.Button(self.bottomframe, text='-',command=lambda:self.ckeyss('-') ,borderwidth=1,bg='red').grid(row=6, column=6)

        keyss[79]=tk.Button(self.bottomframe, text='Z',command=lambda:self.ckeyss('Z') ,borderwidth=1,bg='red').grid(row=6, column=7)

        keyss[80]=tk.Button(self.bottomframe, text='X',command=lambda:self.ckeyss('X') ,borderwidth=1,bg='red').grid(row=6, column=8)

        keyss[81]=tk.Button(self.bottomframe, text='C',command=lambda:self.ckeyss('C') ,borderwidth=1,bg='red').grid(row=6, column=9)

        keyss[82]=tk.Button(self.bottomframe, text='V',command=lambda:self.ckeyss('V') ,borderwidth=1,bg='red').grid(row=6, column=10)

        keyss[83]=tk.Button(self.bottomframe, text='B',command=lambda:self.ckeyss('B') ,borderwidth=1,bg='red').grid(row=6, column=11)






    def ckeyss(self,s:str):
        self.text_area.insert(tk.END,s )


    

if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
