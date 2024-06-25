# -*- encoding: utf-8 -*-
# ----------------------------------------------------------------------------
# The People Versus
# Copyright © 2021 Sergey Chernov aka Gamer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import time
from PIL import Image, ImageTk, ImageDraw, ImageFont
from random import randint
from random import choice
from random import randrange
from enum import Enum
import codecs
root = tk.Tk()
root.geometry("640x480")
root.title("Народ против")
root.resizable(width=False, height=False)
otvet_na_zamenu = False
log = codecs.open('log.txt', 'a', "utf_8_sig")
s = None
morna = False
odgovor = ""
zamen_numbaz = []
var_ready=[]
bazaq, baza_zamen = [], []
bazaq_round, baza_zamen_round = [], []
bazaq_numbaz = []
no_more_left_q, no_more_left_z = False, False
bong_buttons = []
bong_howmuchsaved = 0
infa = ""
ROUND_NUMBER = 1 #1
parodytas_klausimas = tk.Label(root, justify = tkinter.CENTER, bg="#007fff", fg="#ffffff",  wraplength = 380)
#parodytas_klausimas.place(x=10, y=220, width=450, height=70)
timer = tk.Label(root, justify = tkinter.CENTER, bg="#007fff", fg="#ffffff", wraplength = 40)
TIME_LAP = 240 #240
FLIPS = 3
a_o_n_activated = False
SKIP_LEFT = 5-ROUND_NUMBER
TIME_LEFT=240 #240
QUESTIONS_PASSED = 0
tick = False
vienas = Image.open("images/question.png")
du = Image.open("images/empty.png")
trys = Image.open("images/grey.png")
keturi = Image.open("images/wrong.png")
penki = Image.open("images/correct.png")
vienas.thumbnail((36, 36), Image.ANTIALIAS)
du.thumbnail((36, 36), Image.ANTIALIAS)
trys.thumbnail((36, 36), Image.ANTIALIAS)
keturi.thumbnail((36, 36), Image.ANTIALIAS)
penki.thumbnail((36, 36), Image.ANTIALIAS)
uno, dos, tres, cuatro, cinco = ImageTk.PhotoImage(vienas), ImageTk.PhotoImage(du), ImageTk.PhotoImage(trys), ImageTk.PhotoImage(keturi), ImageTk.PhotoImage(penki)
klausimai = ([uno]*ROUND_NUMBER) + [dos]*(5-ROUND_NUMBER)
pytania = []
alt_var_enabled = False
a_o_n = False
for i in range(5):
    mj = tk.Label(image=klausimai[i])
    pytania.append(mj)
    #pytania[i].place(x=10+36*i, y=300)

arrow = Image.open("images/flip.png")
cross = Image.open("images/flip_used.png")
arrow.thumbnail((36, 36), Image.ANTIALIAS)
cross.thumbnail((36, 36), Image.ANTIALIAS)
ahat, shtayim = ImageTk.PhotoImage(arrow), ImageTk.PhotoImage(cross)
#flipz = [ahat, ahat, ahat]
zamienic = []
for i in range(3):
    mj = tk.Label(image=ahat)
    zamienic.append(mj)
    #zamienic[i].place(x=350+36*i, y=300)
BASIC_MONEY = [0, 1000, 2500, 5000, 15000, 50000]
MONEY = [0, 1000, 2500, 5000, 15000, 50000]
BANK = 0
LAPS_PASSED = 0
ROUNDS_IN_LAP_PASSED = 0 #0
rinkimas = []
baza_zamen = []
b = {}
flips_themes = codecs.open('flip.txt', 'r', "utf_8_sig")
for line in flips_themes:
    b = {}
    b["T"] = line.rstrip('\n')
    foo = flips_themes.readline()
    foo = foo.rstrip('\n')
    b["P"] = 'zamen/'+foo
    rinkimas.append(b)
flips_themes.close()
for_cb = []
for a in range(len(rinkimas)):
    for_cb.append(rinkimas[a]["T"])
bazaq = []
stagegong = None
happy_variant = None
bong_stopped = None
flip_topic_choose = ttk.LabelFrame(root, text = 'Тема для замены', width=338, height=45)
flip_topic_choose.place(relx=0.40, rely=0.75)
options = ttk.LabelFrame(root, text = 'Модификации игры', width=280, height=140)
options.place(relx=0.25, rely=0.15)
xxx = ttk.Combobox(flip_topic_choose, values = for_cb, width=27)
xxx.state = 'readonly'
xxx.place(relx = 0, rely=0)
xxx.current(0)
bong_summa_index = -1
alt_yes = tk.IntVar()
allornothing = tk.IntVar()
def doSomething():
    if tk.messagebox.askyesno("Exit", "Do you want to quit the application?"):
        log.close()
        root.destroy()

class bongstage(Enum):
    before = 0
    inprogress = 1
    stopped = 2
    finish = 3
    after = 4


def setgong(variant_, aim):
    global var_ready, variant_bg, happy_variant, all_m
    b = randint (5, 15)
    cpp = []
    for d in range(b):
        while True:
            e = randint(1, aim - 1)
            if not (e in cpp):
                break
        cpp.append(e)
    #c.append (aim)
    cpp.sort()
    #c.pop(0)
    if (variant_!=happy_variant):
        var = cpp[:randint(3, b-2)]
    else:
        var = cpp.copy()
    var_ready = var.copy()
    #print(var_ready)
    variant_bg = variant_
    all_m = aim

def bong_game():
    global stagegong, bong_summa_index, active, bong_buttons, bong_summa, bong_stop, bong_stopped, ROUND_NUMBER, happy_variant, LAPS_PASSED, BANK
    # if a_o_n_activated is True:
    #     BANK = 0
    pas.place_forget()
    zamena.place_forget()
    flip_topic_choose.place_forget()
    timer.place_forget()
    parodytas_klausimas.place_forget()
    for i in range(len(zamienic)):
        zamienic[i].place_forget()
    for i in range(len(pytania)):
        pytania[i].place_forget()
    if (ROUND_NUMBER==1):
        tk.messagebox.showinfo('0', 'Гонг-игры не будет, так как делить нечего')
        if (alt_var_enabled is False):
            tk.messagebox.showinfo("Конец игры", "Выигрыш: "+str(MONEY[5]*LAPS_PASSED))
            log.write("Выигрыш: "+str(MONEY[5]*LAPS_PASSED)+'\n')
        else:
            tk.messagebox.showinfo("Конец игры", "Выигрыш: "+str(BANK))
            log.write("Выигрыш: "+str(BANK)+'\n')
    else:
        bong_stopped = False
        stagegong = bongstage.before
        bong_summa_index = -1
        happy_variant = randint(0, 2)
        #print(str(happy_variant+1)+" - вариант без гонга")
        for a in range(3):
            l = tk.Button(text=str(a + 1), width=5, height=1, command=lambda rtt=a: start_bong_game(rtt))
            bong_buttons.append(l)
            bong_buttons[a].place(relx=.10 + .15 * a, rely=0.08)
        bong_summa = tk.Label(root, width=14, height=1, text="0")
        bong_summa.place(relx=0.25, rely=0.18)
        bong_stop = tk.Button(text="Стоп", width=9, height=1, command=stopgame, state="disabled")
        bong_stop.place(relx=0.25, rely=0.24)

def blah():
    global variant_bg, happy_variant, stagegong, active, bong_stopped, all_m, bong_howmuchsaved
    stagegong = bongstage.finish
    if variant_bg == happy_variant:
        bong_summa["text"] = str(all_m)
        bong_stop["state"] = "disabled"
        if (bong_stopped)==False:
            if (a_o_n_activated) is False:
                bong_howmuchsaved = MONEY[ROUND_NUMBER-1]
            else:
                bong_howmuchsaved = MONEY[ROUND_NUMBER-1]+BANK
            tk.messagebox.showinfo('Вам повезло', 'Вы отыграли все ' + str(bong_howmuchsaved))
    else:
        bong_summa["text"] = "ГОНГ"
        bong_stop["state"] = "disabled"
        if (bong_stopped)==False:
            bong_howmuchsaved = 0
            tk.messagebox.showinfo('Гонг', 'Вы не отыграли ничего')
    if (bong_stopped is False):
        log.write('Выигрыш в гонг-игре: ' + str(bong_howmuchsaved) + '\n')
    if (alt_var_enabled is False):
        tk.messagebox.showinfo("Конец игры", "Выигрыш: " + str(MONEY[5] * LAPS_PASSED + bong_howmuchsaved))
        log.write("Выигрыш: " + str(MONEY[5] * LAPS_PASSED + bong_howmuchsaved) + '\n')
    elif (a_o_n_activated is True):
        tk.messagebox.showinfo("Конец игры", "Выигрыш: " + str(bong_howmuchsaved))
        log.write("Выигрыш: " + str(bong_howmuchsaved) + '\n')


def increase():
    global stagegong, bong_summa_index, bong_buttons, bong_summa, bong_stop
    stagegong = bongstage.inprogress
    root.after_cancel(root.bongtimer)
    bong_summa_index += 1
    if (bong_summa_index == 0):
        bong_stop["state"] = "active"
        bong_summa["text"] = str(var_ready[bong_summa_index])
        stagegong = bongstage.inprogress
        root.bongtimer = root.after(randint(1600, 3200), increase)
    elif bong_summa_index <= len(var_ready)-1:
        bong_summa["text"] = str(var_ready[bong_summa_index])
        root.bongtimer = root.after(randint(1600, 3200), increase)
        # if (bong_summa_index < len(x2)-1):
        #     root.timer = root.after(randint(800, 1900), increase)
    elif (bong_summa_index >= len(var_ready)):
        blah()

def start_bong_game(uyt):
    for a in range(len(bong_buttons)):
        bong_buttons[a]["state"] = "disabled"
    root.bongtimer = root.after(randint(1600, 3200), increase)
    if a_o_n_activated is False:
        setgong(uyt, MONEY[ROUND_NUMBER-1])
    else:
        setgong(uyt, MONEY[ROUND_NUMBER-1]+BANK)

def skipflip(a):
    if (a>0):
        return "normal"
    else:
        return "disabled"

def q_choose(io):
    global s, bazaq_round, baza_zamen_round, morna
    if (io is True): #True-обычный вопрос, False - замена
        s = randint(0, len(bazaq_round)-1)
        parodytas_klausimas["text"] = bazaq_round[s]["Q"]
        #print(str(6-len(bazaq_round)))
        log.write("Вопрос "+str(6-len(bazaq_round))+". "+bazaq_round[s]["Q"]+'\n')
    else:
        s = randint(0, len(baza_zamen_round)-1)
        parodytas_klausimas["text"] = baza_zamen_round[s]["Q"]
        log.write("Замена вопроса. " + baza_zamen_round[s]["Q"] + '\n')
    morna = True


def q_after(r):
    global s
    if r is False: #ответил на обычный вопрос
        parodytas_klausimas["text"] = bazaq_round[s]["A"][0]
        #log.write("Правильный ответ: " + bazaq_round[s]["A"][0] + '\n')
        bazaq_numbaz.pop(s)
        bazaq_round.pop(s)
    else:
        parodytas_klausimas["text"] = baza_zamen_round[s]["A"][0]
        #log.write("Правильный ответ: " + baza_zamen_round[s]["A"][0] + '\n')
        baza_zamen_round.pop(s)
        zamen_numbaz.pop(s)


def load_zamen():
    global baza_zamen, baza_zamen_round, zamen_numbaz, no_more_left_z
    zamen_numbaz = []
    baza_zamen_round = []
    if (len(baza_zamen)<3):
        tk.messagebox.showinfo("Игра окончена", "В базе не осталось достаточного количества замен")
        no_more_left_z = True
        # root.after_cancel(root.startgame)
        # verno.place_forget()
        # neverno.place_forget()
        # pas.place_forget()
        # zamena.place_forget()
    else:
        for i in range(3):
            while True:
                a = randint(0, len(baza_zamen)-1)
                if (baza_zamen[a] not in baza_zamen_round):
                    baza_zamen_round.append(baza_zamen[a])
                    zamen_numbaz.append(a)
                    #print(baza_zamen_round[i]["Q"]) #debug
                    break
        baza_zamen[:] = [x for i, x in enumerate(baza_zamen) if i not in zamen_numbaz]
        #print(len(baza_zamen))
        #for tt in range(len(baza_zamen)):
            #print(baza_zamen[tt]["Q"])

def log_pravotv(d):
    global s
    if not (d): #обычный вопрос
        log.write("Правильный ответ: " + bazaq_round[s]["A"][0] + '\n')
    else:
        log.write("Правильный ответ: " + baza_zamen_round[s]["A"][0] + '\n')

def took_money(n, m):
    if (alt_var_enabled is False):
        tk.messagebox.showinfo("Вы забрали деньги", "Ваш выигрыш - "+str(MONEY[5]*n+MONEY[m-1]))
        log.write("Игрок забирает деньги"+'\n'+ "Выигрыш - "+str(MONEY[5]*n+MONEY[m-1]))
    else:
        tk.messagebox.showinfo("Вы забрали деньги", "Ваш выигрыш - "+str(BANK+MONEY[m-1]))
        log.write("Игрок забирает деньги"+'\n'+ "Выигрыш - "+str(BANK+MONEY[m-1]))


def round_start():
    global TIME_LEFT, tick, SKIP_LEFT, FLIPS, otvet_na_zamenu, no_more_left_z, no_more_left_q, morna, s, LAPS_PASSED, ROUND_NUMBER
    root.after_cancel(root.startgame)
    #verno["state"], neverno["state"], \
    pas["state"], zamena["state"] = skipflip(SKIP_LEFT), skipflip(FLIPS)
    if (no_more_left_z) or (no_more_left_q):
        #verno.place_forget()
        #neverno.place_forget()
        pas.place_forget()
        zamena.place_forget()
        took_money(LAPS_PASSED, ROUND_NUMBER)
        #print("Пройдено кругов: ")
        #print(LAPS_PASSED)
        #print("Номер раунда: ")
        #print(ROUND_NUMBER)
        #print(MONEY[ROUND_NUMBER-1])
    else:
        if tick:
            TIME_LEFT -=1
            timer["text"] = time.strftime('%M:%S', time.gmtime(TIME_LEFT))
            test["state"] = "normal"
        else:
            log.write("Круг " + str(LAPS_PASSED + 1) + '. Раунд ' + str(ROUND_NUMBER) + ' (' + str(MONEY[ROUND_NUMBER]) + ')' + '\n')
            load_questions()
            morna = True
            otvet_na_zamenu = False
            test.place(x=10, y=340)
            #test["state"] = "disabled"
            #q_choose(True)
            tick = True
        if TIME_LEFT==0:
            pytania[QUESTIONS_PASSED]["image"] = cuatro
            q_after(otvet_na_zamenu)
            tk.messagebox.showerror("Время", "Время вышло!")
            log.write("Время истекло"+'\n')
            if (otvet_na_zamenu):
                log.write("Правильный ответ: " + baza_zamen_round[s]["A"][0] + '\n')
            else:
                log.write("Правильный ответ: " + bazaq_round[s]["A"][0] + '\n')
            morna = False
            test.place_forget()
            #verno.place_forget()
            #neverno.place_forget()
            pas.place_forget()
            zamena.place_forget()
            bong_game()
        else:
            root.startgame = root.after(1000, round_start)


#def sustituir(h):
    #if (h is False): #ответ на вопрос-замену


def yep():
    global QUESTIONS_PASSED, ROUND_NUMBER, tick, FLIPS, TIME_LEFT, SKIP_LEFT, bazaq_numbaz, zamen_numbaz, bazaq_round, baza_zamen, baza_zamen_round, bazaq, infa, otvet_na_zamenu, parodytas_klausimas, LAPS_PASSED, morna, BANK, MONEY, BASIC_MONEY, a_o_n_activated, a_o_n
    QUESTIONS_PASSED += 1
    pytania[QUESTIONS_PASSED-1]["image"] = cinco
    q_after(otvet_na_zamenu)
    otvet_na_zamenu = False
    if (QUESTIONS_PASSED) == ROUND_NUMBER:
        root.after_cancel(root.startgame)
        a_o_n_activated = False
        #parodytas_klausimas["text"] = ""
        tk.messagebox.showinfo("", "Верно!")
        bazaq_numbaz = []
        for i in range(len(bazaq_round)):
            bazaq.append(bazaq_round[i])
        bazaq_round = []
        #baza_zamen_round = []
        #print(len(bazaq))
        ROUND_NUMBER += 1
        QUESTIONS_PASSED = 0
        if ROUND_NUMBER > 5:
            LAPS_PASSED += 1
            ROUND_NUMBER = 1
            FLIPS = 3
            TIME_LEFT = TIME_LAP
            for i in range(3):
                zamienic[i]["image"] = ahat
            if (alt_var_enabled is True):
                BANK += MONEY[5]
                MONEY = [i*(LAPS_PASSED+1) for i in BASIC_MONEY]
        if (alt_var_enabled is False):
            infa = "У вас в банке "+str(LAPS_PASSED*MONEY[5])+'. \n В текущем круге вы заработали '+str(MONEY[ROUND_NUMBER-1])+'\n Времени осталось: '+str(time.strftime('%M:%S', time.gmtime(TIME_LEFT)))+'\n Замен осталось: '+str(FLIPS)+'\n'
        else:
            infa = "У вас в банке "+str(BANK)+'. \n В текущем круге вы заработали '+str(MONEY[ROUND_NUMBER-1])+'\n Времени осталось: '+str(time.strftime('%M:%S', time.gmtime(TIME_LEFT)))+'\n Замен осталось: '+str(FLIPS)+'\n'
        if (ROUND_NUMBER==1):
            hhru=5
            ik = LAPS_PASSED
        else:
            hhru=ROUND_NUMBER-1
            ik=LAPS_PASSED+1
            log.write('Времени осталось: ' + str(time.strftime('%M:%S', time.gmtime(TIME_LEFT))) + '\nЗамен осталось: ' +str(FLIPS)+'\n')
        if tk.messagebox.askyesno("Раунд "+str(hhru)+' круга №'+str(ik)+' пройден!', infa+"Будете ли вы играть дальше?"):
            tick = False
            test["state"] = "disabled" #nado
            morna  = False
            # ROUND_NUMBER+=1
            # QUESTIONS_PASSED = 0
            # if ROUND_NUMBER>5:
            #     LAPS_PASSED +=1
            #     ROUND_NUMBER=1
            #     FLIPS=3
            #     TIME_LEFT=240
            #root.title(time.strftime('%M:%S', time.gmtime(TIME_LEFT)))
            if (ROUND_NUMBER==1):
                 for i in range(3):
                     zamienic[i]["image"] = ahat
                 for i in range(len(baza_zamen_round)):
                     baza_zamen.append(baza_zamen_round[i])
                 load_zamen()
            for i in range(ROUND_NUMBER):
                pytania[i]["image"] = uno
            for i in range(ROUND_NUMBER, 5, 1):
                pytania[i]["image"] = dos
            SKIP_LEFT = 5 - ROUND_NUMBER
            #load_questions()
            root.startgame = root.after(1000, round_start)
        elif (a_o_n is True) and ((TIME_LEFT < 60) or ((FLIPS == 0) and (len(baza_zamen)>0))) and (ROUND_NUMBER-1==4) and (LAPS_PASSED>0):
            #print("Есть!")
            if (TIME_LEFT<60):
                if tk.messagebox.askyesno("А если рискнёте?", "Предлагаю рискнуть своим банком, а взамен увеличу время для последнего раунда на минуту! Вы согласны?"):
                    a_o_n_activated = True
                    TIME_LEFT += 60
                    timer["text"] = time.strftime('%M:%S', time.gmtime(TIME_LEFT))
                    log.write("Игрок пользуется опцией Всё или ничего, получая на пятый раунд дополнительную минуту."+'\n')
                    tick = False
                    test["state"] = "disabled"  # nado
                    morna = False
                    for i in range(ROUND_NUMBER):
                        pytania[i]["image"] = uno
                    for i in range(ROUND_NUMBER, 5, 1):
                        pytania[i]["image"] = dos
                    SKIP_LEFT = 5 - ROUND_NUMBER
                    # load_questions()
                    root.startgame = root.after(1000, round_start)
                else:
                    morna = False
                    test["state"] = "disabled"
                    took_money(LAPS_PASSED, ROUND_NUMBER)
            elif ((FLIPS == 0) and (len(baza_zamen)>0)):
                if tk.messagebox.askyesno("А если рискнёте?", "Предлагаю рискнуть своим банком, а взамен дам на пятый раунд одну замену! Вы согласны?"):
                    a_o_n_activated = True
                    FLIPS = 1
                    log.write("Игрок пользуется опцией Всё или ничего, получая на пятый раунд одну замену."+'\n')
                    tick = False
                    test["state"] = "disabled"  # nado
                    morna = False
                    for i in range(ROUND_NUMBER):
                        pytania[i]["image"] = uno
                    for i in range(ROUND_NUMBER, 5, 1):
                        pytania[i]["image"] = dos
                    SKIP_LEFT = 5 - ROUND_NUMBER
                    zamen_numbaz = []
                    baza_zamen_round = []
                    a = randint(0, len(baza_zamen) - 1)
                    if (baza_zamen[a] not in baza_zamen_round):
                        baza_zamen_round.append(baza_zamen[a])
                        zamen_numbaz.append(a)
                    baza_zamen[:] = [x for i, x in enumerate(baza_zamen) if i not in zamen_numbaz]
                    zamienic[-1]["image"] = ahat
                    root.startgame = root.after(1000, round_start)
                else:
                    morna = False
                    test["state"] = "disabled"
                    took_money(LAPS_PASSED, ROUND_NUMBER)
        else:
            morna = False
            test["state"] = "disabled"
            took_money(LAPS_PASSED, ROUND_NUMBER)
            #дописать
        #verno["state"], neverno["state"],\
        pas["state"], zamena["state"] = "disabled", "disabled"
    else:
        tk.messagebox.showinfo("", "Верно!")
        if (otvet_na_zamenu is True):
            otvet_na_zamenu = False
        q_choose(True)

def nope():
    #verno["state"], neverno["state"], \
    pas["state"], zamena["state"] = "disabled", "disabled"
    root.after_cancel(root.startgame)
    #log.write("Ответ игрока: "+guess.get())
    q_after(otvet_na_zamenu)
    pytania[QUESTIONS_PASSED]["image"] = cuatro
    tk.messagebox.showerror("Вы ошиблись!", "Ваш ответ неправильный")
    test.place_forget()
    bong_game() #debug
    pass

def skip():
    global SKIP_LEFT, ROUND_NUMBER, otvet_na_zamenu
    log.write("Игрок пасует. " + '\n')
    log_pravotv(otvet_na_zamenu)
    q_after(otvet_na_zamenu)
    tk.messagebox.showinfo("", "Пас")
    SKIP_LEFT -=1
    pas["state"]  = skipflip(SKIP_LEFT)
    pytania[ROUND_NUMBER+SKIP_LEFT]["image"] = tres
    otvet_na_zamenu = False
    q_choose(True)
    pass

def flip():
    global FLIPS, otvet_na_zamenu, bazaq_round, baza_zamen_round
    log.write("Игрок заменяет вопрос. " + '\n')
    log_pravotv(otvet_na_zamenu)
    q_after(otvet_na_zamenu)
    otvet_na_zamenu = True
    tk.messagebox.showinfo("", "Замена")
    FLIPS -=1
    zamienic[2-FLIPS]["image"] = shtayim
    zamena["state"] = skipflip(FLIPS)
    q_choose(False)
    pass

def stopgame():
    global stagegong, bong_summa_index, timer, bong_stopped, bong_howmuchsaved
    if stagegong == bongstage.inprogress:
        root.after_cancel(root.bongtimer)
        stagegong = bongstage.stopped
        bong_stopped = True
        bong_howmuchsaved = var_ready[bong_summa_index]
        log.write('Выигрыш в гонг-игре: '+str(bong_howmuchsaved)+'\n')
        tk.messagebox.showinfo('Отыгрыш', 'Вы отыграли '+str(bong_howmuchsaved))
        #aux_list[active]['sgor'] = var_ready[bong_summa_index]
        #zaideju_pinigai[active]['text'] = str(aux_list[active]['sgor']) + ' + ' + str(aux_list[active]['nesgor']) + ' = ' + str(aux_list[active]['sgor'] + aux_list[active]['nesgor']) + '\n'
        #print(str(var_ready[bong_summa_index]))
        bong_stop["text"] = "Смотреть дальше"
    elif stagegong == bongstage.stopped:
        bong_summa_index += 1
        if (bong_summa_index < len(var_ready)):
            bong_summa["text"] = str(var_ready[bong_summa_index])
        elif (bong_summa_index == len(var_ready)):
            blah()
            #zaideju_pinigai[active]['text'] = str(aux_list[active]['sgor']) + ' + ' + str(
            #log.write('Итого ' + aux_list[active]["name"] + ' выигрывает ' + str(aux_list[active]['sgor'] + aux_list[active]['nesgor']) + '\n')
            #aux_list[active]["sgor"] = all_m
    elif (stagegong ==bongstage.finish):
        #next()
        pass


#root.title(time.strftime('%M:%S', time.gmtime(TIME_LEFT)))
# tk.messagebox.showinfo("Тест", rinkimas[xxx.current()]["P"])
# flips_loader = open(rinkimas[xxx.current()]["P"], 'r')
# for line in flips_loader:
#     b = {}
#     b["Q"] = line.rstrip('\n')
#     b["A"] = list(map(str, flips_loader.readline().split(", ")))
#     b["A"][-1] = b["A"][-1].rstrip("\n")
#     baza_zamen.append(b)
# flips_loader.close()
# base = open('base.txt', 'r')
# for line in base:
#     b = {}
#     b["Q"] = line.rstrip('\n')
#     b["A"] = list(map(str, base.readline().split(", ")))
#     b["A"][-1] = b["A"][-1].rstrip("\n")
#     bazaq.append(b)
# base.close()

def load_questions():
    global bazaq_numbaz, bazaq_round, baza_zamen, baza_zamen_round, bazaq, no_more_left_q
    bazaq_numbaz = []
    bazaq_round = []
    if (len(bazaq)<5):
        tk.messagebox.showinfo("Игра окончена", "В базе не осталось достаточного количества вопросов")
        no_more_left_q = True
        # root.after_cancel(root.startgame)
        # verno.place_forget()
        # neverno.place_forget()
        # pas.place_forget()
        # zamena.place_forget()
    else:
        for i in range(5):
            while True:
                a = randint(0, len(bazaq)-1)
                if (bazaq[a] not in bazaq_round):
                    bazaq_round.append(bazaq[a])
                    bazaq_numbaz.append(a)
                    #print(bazaq_round[i]["Q"]) #debug
                    break
        bazaq[:] = [x for i, x in enumerate(bazaq) if i not in bazaq_numbaz]
        #print(len(bazaq))
        #for tt in range(len(bazaq)):
            #print(bazaq[tt]["Q"])
        q_choose(True)

def check(*args):
    global otvet_na_zamenu, s, odgovor, morna
    odgovor = guess.get()
    if (morna is True) and (odgovor!=''):
        if (otvet_na_zamenu):
            uy = []
            for i in range(len(baza_zamen_round[s]["A"])):
                uy.append(baza_zamen_round[s]["A"][i])
                uy[i] = uy[i].replace(' ', '')
                uy[i]=uy[i].lower()
            odgovor = odgovor.lower()
            odgovor = odgovor.replace(' ', '')
            if (odgovor in uy):
                j = uy.index(odgovor)
                if (j==0):
                    log.write("Правильный ответ: "+baza_zamen_round[s]["A"][j]+'\n')
                else:
                    log.write("Правильный ответ: "+baza_zamen_round[s]["A"][j]+" ("+baza_zamen_round[s]["A"][0]+")"+'\n')
                yep()
            else:
                log.write("Ответ игрока: " + guess.get()+'\n')
                log.write("Правильный ответ: "+baza_zamen_round[s]["A"][0]+'\n')
                nope()
        else:
            uy = []
            for i in range(len(bazaq_round[s]["A"])):
                uy.append(bazaq_round[s]["A"][i])
                uy[i] = uy[i].replace(' ', '')
                uy[i] = uy[i].lower()
            odgovor = odgovor.lower()
            odgovor = odgovor.replace(' ', '')
            if (odgovor in uy):
                j = uy.index(odgovor)
                if (j == 0):
                    log.write("Правильный ответ: "+bazaq_round[s]["A"][j]+'\n')
                else:
                    log.write("Правильный ответ: "+bazaq_round[s]["A"][j]+" ("+bazaq_round[s]["A"][0]+")"+'\n')
                yep()
            else:
                log.write("Ответ игрока: " + guess.get()+'\n')
                log.write("Правильный ответ: "+bazaq_round[s]["A"][0]+'\n')
                nope()
        guess.set("")





def start():
    global bazaq, rinkimas, baza_zamen, pytania, zamienic
    bazaq = []
    #for_cb = []
    baza_zamen = []
    options.place_forget()
    #tk.messagebox.showinfo("Тест", rinkimas[xxx.current()]["P"])
    flips_loader = codecs.open(rinkimas[xxx.current()]["P"], 'r', "utf_8_sig")
    log.write("Тема замен: "+rinkimas[xxx.current()]["T"]+'\n')
    for line in flips_loader:
        b = {}
        b["Q"] = line.rstrip('\n')
        b["A"] = list(map(str, flips_loader.readline().split(", ")))
        b["A"][-1]=b["A"][-1].rstrip("\n")
        baza_zamen.append(b)
    flips_loader.close()
    base = codecs.open('base.txt', 'r', "utf_8_sig") #должно быть base.txt
    for line in base:
        b = {}
        b["Q"] = line.rstrip('\n')
        b["A"] = list(map(str, base.readline().split(", ")))
        b["A"][-1]=b["A"][-1].rstrip("\n")
        bazaq.append(b)
    base.close()
    #tk.messagebox.showinfo("Вопросы-замены", "Их "+str(len(baza_zamen)))
    xxx["state"]='disabled'
    ppp.place_forget()
    load_zamen()
    parodytas_klausimas.place(x=10, y=220, width=450, height=70)
    tk.messagebox.showinfo("Игра началась", "У вас 4 минуты на 5 раундов")
    #root.title(time.strftime('%M:%S', time.gmtime(TIME_LAP)))
    root.startgame = root.after(1000, round_start)
    for i in range (5):
        pytania[i].place(x=10 + 36 * i, y=300)
    for i in range(3):
        zamienic[i].place(x=350 + 36 * i, y=300)
    timer.place(x=10, y=120, width=50, height=30)
    timer["text"] = time.strftime('%M:%S', time.gmtime(TIME_LEFT))
    # for a in range(len(bazaq)):
    #     print(bazaq[a])

def alt_changed():
    global alt_var_enabled, a_o_n, risk
    if alt_yes.get()==1:
        alt_var_enabled = True
        risk['state'] = ["normal"]
        #print('1')
    else:
        alt_var_enabled = False
        risk['state'] = ["disabled"]
        a_o_n = False
        risk.deselect()
        #print('0')


def aon_changed():
    global a_o_n
    if allornothing.get()==1:
        a_o_n = True
        #print('11')
    else:
        a_o_n = False
        #print('10')

# flip_topic_choose = ttk.LabelFrame(root, text = 'Тема для замены', width=258, height=45)
# flip_topic_choose.place(relx=0.40, rely=0.75)
# xxx = ttk.Combobox(flip_topic_choose, values = for_cb)
# xxx.state = 'readonly'
# xxx.place(relx = 0, rely=0)
# xxx.current(0)
ppp = tk.Button(flip_topic_choose, text="Выбрать", command=start, width=6, height=1)
ppp.place(relx=0.7, rely=0)
guess = tk.StringVar()
test = ttk.Entry(root, width=29, textvariable=guess)
test.bind("<Return>", check)

#verno = tk.Button(root, text="Верно", command=yep, width=4, height=1)
#neverno = tk.Button(root, text="Неверно", command=nope, width=4, height=1)
pas = tk.Button(root, text="Пас", command=skip, width=6, height=1)
zamena = tk.Button(root, text="Замена", command=flip, width=6, height=1)
#verno.place(relx=0.2, rely=0)
#neverno.place(relx=0.4, rely=0)
pas.place(relx=0.05, rely=0.8)
zamena.place(relx=0.23, rely=0.8)
game_alt = tk.Checkbutton(options, text="Увеличивать стоимость раундов с каждым кругом", variable=alt_yes, command=alt_changed, onvalue=1, offvalue=0)
game_alt.pack()
risk = tk.Checkbutton(options, text="Предлагать опцию Всё или ничего", variable=allornothing, command=aon_changed, onvalue=1, offvalue=0)
risk['state'] = 'disabled'
risk.pack()
#verno["state"], neverno["state"],\
pas["state"], zamena["state"] = "disabled", "disabled"
root.protocol('WM_DELETE_WINDOW', doSomething)
root.mainloop()