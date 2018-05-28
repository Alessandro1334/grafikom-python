from graphics import *
import polyline

def main():
    win = GraphWin("Alessandro - Grafikom", 850, 250)
    win.setBackground(color_rgb(236, 240, 241))

    # bentuk Angka 2
    garis1 = Line(Point(50,200), Point(100,200))
    garis1.setWidth(5)
    garis1.draw(win)
    garis2 = Line(Point(100,202), Point(50,100))
    garis2.setWidth(5)
    garis2.draw(win)
    garis3 = Line(Point(50,102), Point(50,80))
    garis3.setWidth(5)
    garis3.draw(win)
    garis4 = Line(Point(50,80), Point(100,80))
    garis4.setWidth(5)
    garis4.draw(win)
    garis5 = Line(Point(100,80), Point(100,100))
    garis5.setWidth(5)
    garis5.draw(win)

    # bentuk Angka 0
    angka0_2 = Rectangle(Point(150,80), Point(200,200))
    angka0_2.setWidth(5)
    angka0_2.draw(win)

    # bentuk Angka 0
   
    angka0_1 = Rectangle(Point(250,80), Point(300,200))
    angka0_1.setWidth(5)
    angka0_1.draw(win)

    #bentuk Angka 6
    angka6 = Rectangle(Point(350,150), Point(400,200))
    angka6.setWidth(5)
    angka6.draw(win)
    angka6_1 = Line(Point(400,150), Point(400,80))
    angka6_1.setWidth(5)
    angka6_1.draw(win)
    angka6_2 = Line(Point(400,80), Point(350,80))
    angka6_2.setWidth(5)
    angka6_2.draw(win)
    angka6_3 = Line(Point(350,80), Point(350,110))
    angka6_3.setWidth(5)
    angka6_3.draw(win)

    #Bentuk Angka 1
    angka1 = Line(Point(450,80), Point(450,200))
    angka1.setWidth(5)
    angka1.draw(win)
    angka1_1 = Line(Point(450,80), Point(460,100))
    angka1_1.setWidth(5)
    angka1_1.draw(win)

    # Angka 0 Angkatan 
    angka0 = Rectangle(Point(500,80), Point(550,200))
    angka0.setWidth(5)
    angka0.draw(win)

    # Huruf A
    a_1 = Line(Point(625,80), Point(600,200))
    a_1.setWidth(5)
    a_1.draw(win)
    a_2 = Line(Point(625,80), Point(650,200))
    a_2.setWidth(5)
    a_2.draw(win)
    a_3 = Line(Point(610,150), Point(640,150))
    a_3.setWidth(5)
    a_3.draw(win)

    #Bentuk Angka 1
    angka1 = Line(Point(700,80), Point(700,200))
    angka1.setWidth(5)
    angka1.draw(win)
    angka1_1 = Line(Point(700,80), Point(710,100))
    angka1_1.setWidth(5)
    angka1_1.draw(win)
    
    #Bentuk huruf G
    g_1 = Line(Point(750,80), Point(750,110))
    g_1.setWidth(5)
    g_1.draw(win)
    g_2 = Line(Point(750,80), Point(800,80))
    g_2.setWidth(5)
    g_2.draw(win)
    g_3 = Line(Point(800,80), Point(800,200))
    g_3.setWidth(5)
    g_3.draw(win)
    g_4 = Line(Point(800,200), Point(750,200))
    g_4.setWidth(5)
    g_4.draw(win)
    g_5 = Line(Point(750,200), Point(750,150))
    g_5.setWidth(5)
    g_5.draw(win)
    g_6 = Line(Point(750,150), Point(770,150))
    g_6.setWidth(5)
    g_6.draw(win)
   
    win.getMouse()
    win.close()


main()
