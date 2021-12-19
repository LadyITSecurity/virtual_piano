from tkinter import *
import time
import pygame

# =========================================================================================
notes = {
    'C#': 'C_s.wav', 'D#': 'D_s.wav', 'F#': 'F_s.wav',
    'G#': 'G_s.wav', 'C#1': 'C_s1.wav', 'D#1': 'D_s1.wav',
    'B#': 'Bb.wav', 'C': 'C.wav', 'D': 'D.wav',
    'E': 'E.wav', 'F': 'F.wav', 'G': 'G.wav',
    'A': 'A.wav', 'B': 'B.wav', 'C1': 'C1.wav',
    'D1': 'D1.wav', 'E1': 'E1.wav', 'F1': 'F1.wav',
}


for_Elise =     ['E1', 'D#1', 'E1', 'D#1', 'E1', '', 'B', 'D1', 'C1', 'A', 'C', 'E', 'A', 'B', 'E', 'G#', 'B', 'C1', 'E',
                 'E1', 'D#1', 'E1', 'D#1', 'E1', 'B', 'D1', 'C1', 'A', 'C', 'E', 'A', 'B', 'E', 'C1', 'B', "A"]

jingle_bells1 = ['C', 'A', 'G', 'F', 'C', '', '', 'C', 'C', 'C', 'A', 'G', 'F', 'D', '', '',
                 'D', 'B#', 'A', 'G', 'E', '', '', 'C1', 'C1', 'B#', 'G', 'A', '', '',
                 'C', 'A', 'G', 'F', 'C', '', '', 'C', 'C', 'C', 'A', 'G', 'F', 'D', '', '',
                 'D', 'B#', 'A', 'G', 'C1', 'C1', 'C1', 'C1', 'D1', 'C1', 'B#', 'G', 'F']

we_do_not_care = ['B', '', 'D1', '', 'B', 'B', 'F#', '',
                  'B', '', 'D1', '', 'B', 'B', 'F#', '',
                  'E', '', 'G', '', 'F#', 'F#', 'C#', '', 'F#', 'E', 'D', 'E', 'F#']


pygame.init()
root = Tk()
root.title('Music Box')
root.geometry("1350x700+0+0")
root.configure(background='white')

# заголовок
ABC = Frame(root, bg='powder blue', bd=20, relief=RIDGE)
ABC.grid()
# дата и время
ABC1 = Frame(ABC, bg='powder blue', bd=20, relief=RIDGE)
ABC1.grid()
# проигрывание мелодии
ABC2 = Frame(ABC, bg='powder blue', relief=RIDGE)
ABC2.grid()

# черные клавиши
ABC3 = Frame(ABC, bg='powder blue', relief=RIDGE)
ABC3.grid()
# белые клавиши
ABC4 = Frame(ABC, bg='powder blue', relief=RIDGE)
ABC4.grid()

str1 = StringVar()
str1.set("Just Like Music")
Date1 = StringVar()
Time1 = StringVar()

Date1.set(time.strftime('%d/%m/%Y'))
Time1.set(time.strftime('%H:/%M:/%S'))

start_time = time.time()

import os

def value_notes(note):
    if note == '':
        time.sleep(0.2)
        return
    str1.set(note)
    tmp_directory = notes[note]
    directory = 'C:\\notes\\' + tmp_directory
    print(tmp_directory)
    sound = pygame.mixer.Sound(directory)
    sound.play()


def play_melody(choice):
    for i in choice:
        time.sleep(0.35)
        value_notes(i)


# ======================================Label with Title===================================================

Label(ABC1, text="Piano Musical Keys", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg='powder blue',
      fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11)

# =========================================================================================
txtDate = Entry(ABC1, textvariable=Date1, font=('arial', 18, 'bold'), bd=4, bg='powder blue',
                fg='black', width=28, justify=CENTER).grid(row=1, column=0, pady=1)

txtDisplay = Entry(ABC1, textvariable=str1, font=('arial', 18, 'bold'), bd=4, bg='powder blue',
                   fg='black', width=28, justify=CENTER).grid(row=1, column=1, pady=1)

txtTime = Entry(ABC1, textvariable=Time1, font=('arial', 18, 'bold'), bd=4, bg='powder blue',
                fg='black', width=28, justify=CENTER).grid(row=1, column=2, pady=1)

# =========================================================================================

PlayMelody1 = Button(ABC2, height=2, width=16, justify=CENTER, text="Für Elise", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(for_Elise))
PlayMelody1.grid(row=0, column=0, padx=0, pady=0)

PlayMelody2 = Button(ABC2, height=2, width=16, justify=CENTER, text="jingle_bells", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(jingle_bells1))
PlayMelody2.grid(row=0, column=1, padx=0, pady=0)

PlayMelody3 = Button(ABC2, height=2, width=16, justify=CENTER, text="а нам все равно", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(we_do_not_care))
PlayMelody3.grid(row=0, column=2, padx=0, pady=0)

# =========================================================================================

# верхний ряд (черные)
# до#, ре# (ре бемоль, ми бемоль)
btnCs = Button(ABC3, height=6, width=6, text="С#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes('C#'))
btnCs.grid(row=0, column=0, padx=5, pady=5)
btnDs = Button(ABC3, height=6, width=6, text="D#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("D#"))
btnDs.grid(row=0, column=2, padx=5, pady=5)

btnSpace1 = Button(ABC3, state=DISABLED, height=6, width=15, bg='powder blue', relief=FLAT)
btnSpace1.grid(row=0, column=3, padx=0, pady=0)

# фа#, соль#, ля# (соль бемоль, ля бемоль, си бемоль)
btnFs = Button(ABC3, height=6, width=6, text="F#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("F#"))
btnFs.grid(row=0, column=4, padx=5, pady=5)
btnGs = Button(ABC3, height=6, width=6, text="G#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("G#"))
btnGs.grid(row=0, column=6, padx=5, pady=5)
btnBs = Button(ABC3, height=6, width=6, text="B#", bg="black", fg="white", font=('arial', 18, 'bold'),
               command=lambda: value_notes("B#"))
btnBs.grid(row=0, column=8, padx=5, pady=5)

btnSpace2 = Button(ABC3, state=DISABLED, height=6, width=15, bg='powder blue', relief=FLAT)
btnSpace2.grid(row=0, column=9, padx=0, pady=0)

# до#, ре# (ре бемоль, ми бемоль)
btnCs1 = Button(ABC3, height=6, width=6, text="С#1", bg="black", fg="white", font=('arial', 18, 'bold'),
                command=lambda: value_notes("C#1"))
btnCs1.grid(row=0, column=10, padx=5, pady=5)
btnDs1 = Button(ABC3, height=6, width=6, text="D#1", bg="black", fg="white", font=('arial', 18, 'bold'),
                command=lambda: value_notes("D#1"))
btnDs1.grid(row=0, column=12, padx=5, pady=5)

btnSpace3 = Button(ABC3, state=DISABLED, height=6, width=15, bg='powder blue', relief=FLAT)
btnSpace3.grid(row=0, column=13, padx=0, pady=0)

# =========================================================================================
# нижний ряд (белые)

btnC = Button(ABC4, height=6, width=6, text="C", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("C"))
btnC.grid(row=0, column=0, padx=5, pady=5)
btnD = Button(ABC4, height=6, width=6, text="D", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("D"))
btnD.grid(row=0, column=1, padx=5, pady=5)
btnE = Button(ABC4, height=6, width=6, text="E", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("E"))
btnE.grid(row=0, column=2, padx=5, pady=5)
btnF = Button(ABC4, height=6, width=6, text="F", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("F"))
btnF.grid(row=0, column=3, padx=5, pady=5)

btnG = Button(ABC4, height=6, width=6, text="G", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("G"))
btnG.grid(row=0, column=4, padx=5, pady=5)
btnA = Button(ABC4, height=6, width=6, text="A", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("A"))
btnA.grid(row=0, column=5, padx=5, pady=5)
btnB = Button(ABC4, height=6, width=6, text="B", bg="white", fg="black", font=('arial', 18, 'bold'),
              command=lambda: value_notes("B"))
btnB.grid(row=0, column=6, padx=5, pady=5)
btnC1 = Button(ABC4, height=6, width=6, text="C1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("C1"))
btnC1.grid(row=0, column=7, padx=5, pady=5)

btnD1 = Button(ABC4, height=6, width=6, text="D1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("D1"))
btnD1.grid(row=0, column=8, padx=5, pady=5)
btnE1 = Button(ABC4, height=6, width=6, text="E1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("E1"))
btnE1.grid(row=0, column=9, padx=5, pady=5)
btnF1 = Button(ABC4, height=6, width=6, text="F1", bg="white", fg="black", font=('arial', 18, 'bold'),
               command=lambda: value_notes("F1"))
btnF1.grid(row=0, column=10, padx=5, pady=5)

root.mainloop()


time.sleep(10)
pygame.quit()
pygame.init()
root = Tk()
root.title('Music Box')
root.geometry("1350x700+0+0")
root.configure(background='white')

# заголовок
ABC = Frame(root, bg='powder blue', bd=20, relief=RIDGE)
ABC.grid()
# =========================================================================================
Label(ABC1, text="Piano Musical Keys\nThe time is over!", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg='powder blue',
      fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11)

root.mainloop()
# =========================================================================================
# =========================================================================================
