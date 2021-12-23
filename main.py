from tkinter import *
import time
import pygame


# =========================================================================================
class Settings:
    _way = 'C:\\notes\\'
    _way_piano = 'C:\\notes\\'
    _way_another = 'C:\\notes\\Steel_Drum\\'
    _piano_flag = True


    def get_piano_flag(self) -> bool:
        return  self._piano_flag

    def change_instrument(self) -> None:
        if self._piano_flag:
            self._piano_flag = False
        else:
            self._piano_flag = True
        return

    def get_instrument(self) -> str:
        if self._piano_flag:
            return self._way_piano
        else:
            return self._way_another


notes = {
    'C#': 'C_s.wav', 'D#': 'D_s.wav', 'F#': 'F_s.wav',
    'G#': 'G_s.wav', 'C#1': 'C_s1.wav', 'D#1': 'D_s1.wav',
    'B#': 'Bb.wav', 'C': 'C.wav', 'D': 'D.wav',
    'E': 'E.wav', 'F': 'F.wav', 'G': 'G.wav',
    'A': 'A.wav', 'B': 'B.wav', 'C1': 'C1.wav',
    'D1': 'D1.wav', 'E1': 'E1.wav', 'F1': 'F1.wav',
}

for_Elise = ['E1', 'D#1', 'E1', 'D#1', 'E1', '', 'B', 'D1', 'C1', 'A', 'C', 'E', 'A', 'B', 'E', 'G#', 'B', 'C1', 'E',
             'E1', 'D#1', 'E1', 'D#1', 'E1', 'B', 'D1', 'C1', 'A', 'C', 'E', 'A', 'B', 'E', 'C1', 'B', "A"]

jingle_bells1 = ['C', 'A', 'G', 'F', 'C', '', '', 'C', 'C', 'C', 'A', 'G', 'F', 'D', '', '',
                 'D', 'B#', 'A', 'G', 'E', '', '', 'C1', 'C1', 'B#', 'G', 'A', '', '',
                 'C', 'A', 'G', 'F', 'C', '', '', 'C', 'C', 'C', 'A', 'G', 'F', 'D', '', '',
                 'D', 'B#', 'A', 'G', 'C1', 'C1', 'C1', 'C1', 'D1', 'C1', 'B#', 'G', 'F']

we_do_not_care = ['B', '', 'D1', '', 'B', 'B', 'F#', '',
                  'B', '', 'D1', '', 'B', 'B', 'F#', '',
                  'E', '', 'G', '', 'F#', 'F#', 'C#', '', 'F#', 'E', 'D', 'E', 'F#']

coca_cola = ['A', 'A', 'A', 'A', 'B#', '', '', 'B#', 'A', 'G', '', 'F', 'A', '', 'F',
             'A', 'A', 'C1', 'B#', '', 'A', '', 'G', '', 'G', 'C1', 'A', 'F', '',
             'F', 'G', 'G', 'C1', 'A', 'F']

jingle_bells2 = ['A', 'A', 'A', '', 'A', 'A', 'A', '', 'A', 'C1', 'F', 'G', 'A', '', '',
                 'B#', 'B#', 'B#', 'B#', 'B#', 'A', 'A', 'A', 'A', 'G', 'G', 'A', 'G', '', 'C1',
                 'A', 'A', 'A', '', 'A', 'A', 'A', '', 'A', 'C1', 'F', 'G', 'A', '', '',
                 'B#', 'B#', 'B#', 'B#', 'B#', 'A', 'A', 'A', 'C1', 'C1', 'B#', 'G', 'F', '']

raffaello = ['E', '', 'F#', 'G#', 'E', 'D#', '', 'E', 'F#', 'G#', 'G#', '', 'A', 'B', 'C#1', 'F#', '', '',
             'G', '', 'G#', 'A', 'B', 'E1', '', 'D#1', 'C#1', 'G#', 'B', '', '', 'B#', 'A', '', '',
             'E', '', 'F#', 'G#', 'E', 'D#', '', 'E', 'F#', 'G#', 'G#', '', 'A', 'B', 'C#1', 'F#', '', '',
             'E1', '', '', 'D#1', '', 'E1', 'C#1', 'A', 'F#', 'G#', 'A', 'C#', '', 'A', 'F#', 'D#', '', 'E']


def value_notes(note):
    if note == '':
        time.sleep(0.1)
        return
    str1.set(note)
    tmp_directory = notes[note]
    '''
    way1 = 'C:\\notes\\'
    way2 = 'C:\\notes\\Steel_Drum\\'
    if instrument:
        directory = way + tmp_directory
    else:
        directory = way + tmp_directory
        '''
    path = settings.get_instrument()
    directory = path + tmp_directory
    print(tmp_directory)
    sound = pygame.mixer.Sound(directory)
    sound.play()
    time.sleep(0.1)
    # pygame.mixer.music.stop()


def play_melody(choice):
    for i in choice:
        time.sleep(0.35)
        value_notes(i)


pygame.init()
root = Tk()
root.title('Music Box')
root.geometry("1350x700+0+0")
root.configure(background='white')

_start_time = time.time()

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

settings = Settings()
# ======================================Label with Title===================================================

Label(ABC1, text="Piano Musical Keys", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4, bg='powder blue',
      fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11)

# =========================================================================================
txtDate = Entry(ABC1, textvariable=Date1, font=('arial', 18, 'bold'), bd=4, bg='powder blue',
                fg='black', width=20, justify=CENTER).grid(row=1, column=0, pady=1)

txtDisplay = Entry(ABC1, textvariable=str1, font=('arial', 18, 'bold'), bd=4, bg='powder blue',
                   fg='black', width=20, justify=CENTER).grid(row=1, column=1, pady=1)

txtTime = Entry(ABC1, textvariable=Time1, font=('arial', 18, 'bold'), bd=4, bg='powder blue',
                fg='black', width=20, justify=CENTER).grid(row=1, column=2, pady=1)
'''
var = StringVar()
var.set('C:\\notes\\Steel_Drum\\')
piano = Radiobutton(ABC1, text="piano", variable=var, value='C:\\notes\\Steel_Drum\\')
another = Radiobutton(ABC1, text="another", variable=var, value='C:\\notes\\')
another.grid(row=1, column=3, padx=0, pady=1)
piano.grid(row=1, column=4, padx=0, pady=1)
'''
change_instrument = Button(ABC1, height=1, width=20, justify=CENTER, text="change instrument", bg="powder blue",
                           fg="black", font=('arial', 14, 'bold'), command=lambda: settings.change_instrument())
change_instrument.grid(row=1, column=5, padx=0, pady=1)

# =========================================================================================

PlayMelody1 = Button(ABC2, height=1, width=16, justify=CENTER, text="Für Elise", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(for_Elise))
PlayMelody1.grid(row=0, column=0, padx=0, pady=0)

PlayMelody2 = Button(ABC2, height=1, width=16, justify=CENTER, text="jingle_bells", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(jingle_bells2))
PlayMelody2.grid(row=0, column=1, padx=0, pady=0)

PlayMelody3 = Button(ABC2, height=1, width=16, justify=CENTER, text="а нам все равно", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(we_do_not_care))
PlayMelody3.grid(row=0, column=2, padx=0, pady=0)

PlayMelody4 = Button(ABC2, height=1, width=16, justify=CENTER, text="coca cola", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(coca_cola))
PlayMelody4.grid(row=0, column=3, padx=0, pady=0)

PlayMelody5 = Button(ABC2, height=1, width=16, justify=CENTER, text="Raffaello", bg="pink",
                     fg="black", font=('arial', 14, 'bold'), command=lambda: play_melody(raffaello))
PlayMelody5.grid(row=0, column=4, padx=0, pady=0)

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
btnBs = Button(ABC3, height=6, width=6, text="A#", bg="black", fg="white", font=('arial', 18, 'bold'),
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

if time.time() - _start_time > 10:
    pygame.quit()
    exit()
    pygame.init()
    root = Tk()
    root.title('Music Box')
    root.geometry("1350x700+0+0")
    root.configure(background='white')

    # заголовок
    ABC = Frame(root, bg='powder blue', bd=20, relief=RIDGE)
    ABC.grid()
    # =========================================================================================
    Label(ABC1, text="Piano Musical Keys\nThe time is over!", font=('arial', 25, 'bold'), padx=8, pady=8, bd=4,
          bg='powder blue',
          fg='white', justify=CENTER).grid(row=0, column=0, columnspan=11)

    root.mainloop()
# =========================================================================================
# =========================================================================================
