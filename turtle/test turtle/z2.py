from turtle import *

def slupek(wys):
    pencolor(0,0,0)
    fillcolor(0,0,1)
    fd(20)
    lt(90)
    down()
    begin_fill()
    fd(wys-1)
    rt(90)
    fd(40)
    rt(90)
    fd(wys-1)
    rt(90)
    fd(40)
    end_fill()
    rt(180)
    up()
    fd(40)

def linie(ilosc,dlugosc,odstep):
    width(3)
    fd(dlugosc)
    width(1)
    up()
    bk(dlugosc)
    pencolor(0.3,0.3,0.4)
    for i in range(ilosc):
        lt(90)
        fd(odstep)
        down()
        rt(90)
        fd(dlugosc)
        up()
        bk(dlugosc)
    rt(90)
    fd(5*25)
    lt(90)

    lt(90)
    fd(1)
    rt(90)


linie(5,250,25)
slupek(112.5)
slupek(30)
slupek(50)
slupek(20)
done()
