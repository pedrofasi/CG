from ast import increment_lineno
from re import A
from time import sleep
from tkinter import *
import tkinter.messagebox
import tkinter as tk
from turtle import position
import math
from numpy import place

WIDTH, HEIGHT = 640, 480
MEIOX, MEIOY = int(WIDTH/2), int(HEIGHT/2)

# ALUNO: Pedro Henrique Reis Rodrigues
# MATRÍCULA: 668443

# Criação da Matriz de Pixels através do TkInter
window = Tk()

# Cria a janela, com tamanho de 640x480p, com fundo Preto.

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()

# Declara img como uma variável para plotar os Pixels
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
canvas.configure(scrollregion=canvas.bbox("ALL"))


# Declaração de variável para armazenar as coordenadas dos pontos obtidos
# Através do click do mouse
mousepos_x = []
mousepos_y = []

# Função para plotar nos restantes 8 octantes da circunferencia


def SetPixel_Circunferencia(x, y, xc, yc):
    img.put("#ffffff", (x+xc+MEIOX, y+yc+MEIOY))
    img.put("#ffffff", (x+xc+MEIOX, -y+yc+MEIOY))
    img.put("#ffffff", (-x+xc+MEIOX, y+yc+MEIOY))
    img.put("#ffffff", (-x+xc+MEIOX, -y+yc+MEIOY))
    img.put("#ffffff", (y+xc+MEIOX, x+yc+MEIOY))
    img.put("#ffffff", (y+xc+MEIOX, -x+yc+MEIOY))
    img.put("#ffffff", (-y+xc+MEIOX, x+yc+MEIOY))
    img.put("#ffffff", (-y+xc+MEIOX, -x+yc+MEIOY))


def Circunferencia():
    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    xc = int(circunCxlabel.get(1.0, "end-1c"))
    yc = int(circunCylabel.get(1.0, "end-1c"))
    r = int(circunRlabel.get(1.0, "end-1c"))

    yc = yc * (-1)

    p = 3 - 2*r
    x = 0
    y = r

    SetPixel_Circunferencia(x, y, xc, yc)

    while(x < y):
        if(p < 0):
            p += 4*x + 6
        else:
            p += 4*(x-y)+10
            y -= 1
        x += 1
        SetPixel_Circunferencia(x, y, xc, yc)

# Esta função DDA, vista em sala de aula, obtem-se os pontos através dos labels
# E plota esses pontos


def DDA():
    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    x1 = int(retaX1label.get(1.0, "end-1c"))
    y1 = int(retaY1label.get(1.0, "end-1c"))
    x2 = int(retaX2label.get(1.0, "end-1c"))
    y2 = int(retaY2label.get(1.0, "end-1c"))

    y1 = y1 * (-1)
    y2 = y2 * (-1)

    dx = int(x2-x1)
    dy = int(y2-y1)

    if(abs(dx) > abs(dy)):
        passos = abs(dx)
    else:
        passos = abs(dy)
    x_incr = dx/passos
    y_incr = dy/passos

    x = x1
    y = y1

    img.put("#ffffff", (round(x+MEIOX), round(y+MEIOY)))

    for k in range(1, passos, 1):
        x = x+x_incr
        y = y+y_incr
        img.put("#ffffff", (round(x+MEIOX), round(y+MEIOY)))

    return

# Esta função Bresenham, vista em sala de aula, obtem-se os pontos através dos labels
# E plota esses pontos


def Bresenham():
    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    x1 = int(retaX1label.get(1.0, "end-1c"))
    y1 = int(retaY1label.get(1.0, "end-1c"))
    x2 = int(retaX2label.get(1.0, "end-1c"))
    y2 = int(retaY2label.get(1.0, "end-1c"))

    y1 = y1 * (-1)
    y2 = y2 * (-1)

    dx = int(x2-x1)
    dy = int(y2-y1)
    if(dx >= 0):
        incrx = 1
    else:
        incrx = -1
        dx = dx = -dx
    if(dy >= 0):
        incry = 1
    else:
        incry = -1
        dy = -dy

    x = x1
    y = y1

    img.put("#ffffff", (x+MEIOX, y+MEIOY))

    if(dy < dx):
        p = 2*dy - dx
        const1 = 2*dy
        const2 = 2*(dy-dx)
        for i in range(dx):
            x += incrx
            if(p < 0):
                p += const1
            else:
                y += incry
                p += const2
            img.put("#ffffff", (x+MEIOX, y+MEIOY))
    else:
        p = 2*dx - dy
        const1 = 2*dx
        const2 = 2*(dx-dy)
        for i in range(dy):
            y += incry
            if(p < 0):
                p += const1
            else:
                x += incrx
                p += const2
            img.put("#ffffff", (x+MEIOX, y+MEIOY))

    return


# Esta função Reta é idêntica ao algoritmo bresenham, porém com as coordenadas dos pontos já recebidas
# Por parâmetro
def Reta(x1, y1, x2, y2):

    dx = int(x2-x1)
    dy = int(y2-y1)
    if(dx >= 0):
        incrx = 1
    else:
        incrx = -1
        dx = dx = -dx
    if(dy >= 0):
        incry = 1
    else:
        incry = -1
        dy = -dy

    x = x1
    y = y1

    img.put("#ffffff", (x, y))

    if(dy < dx):
        p = 2*dy - dx
        const1 = 2*dy
        const2 = 2*(dy-dx)
        for i in range(dx):
            x += incrx
            if(p < 0):
                p += const1
            else:
                y += incry
                p += const2
            img.put("#ffffff", (x, y))
    else:
        p = 2*dx - dy
        const1 = 2*dx
        const2 = 2*(dx-dy)
        for i in range(dy):
            y += incry
            if(p < 0):
                p += const1
            else:
                x += incrx
                p += const2
            img.put("#ffffff", (x, y))

    return

# Esta função apaga os pontos, e também os objetos exibidos na tela.


def resetCanvas():
    mousepos_x.clear()
    mousepos_y.clear()
    img.blank()

# Esta função é apenas para os algoritmos de Recorte, onde é retirado o visor e se plota os pontos normais.


def undoCanvas():
    img.blank()
    plotPoints()

# Esta função é apenas para limpar os objetos vistos na tela (Mas não se perde os pontos)


def UpdateFunction():
    img.blank()

# Função Translação, vista também em sala de Aula, na qual recebe valores xt e yt
# através dos labels correspondentes, e é somado aos pontos já obtidos em mousepos_x e mousepos_y


def translacao():
    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    xt = int(transXlabel.get(1.0, "end-1c"))
    yt = int(transYlabel.get(1.0, "end-1c"))

    tam = len(mousepos_x)

    for x in range(0, tam, 1):
        mousepos_x[x] = mousepos_x[x]+xt
        mousepos_y[x] = mousepos_y[x]+yt

    UpdateFunction()
    for x in range(0, tam-1, 1):
        Reta(mousepos_x[x]+xt, mousepos_y[x]+yt,
             mousepos_x[x+1]+xt, mousepos_y[x+1]+yt)

    Reta(mousepos_x[0]+xt, mousepos_y[0]+yt,
         mousepos_x[tam-1]+xt, mousepos_y[tam-1]+yt)


# Função que retorna a correlação matemática para realizar a rotação de X de um ponto.
def pegaXrot(x, y, g):
    return int(x*math.cos(g) - y*math.sin(g))

# Função que retorna a correlação matemática para realizar a rotação de Y de um ponto.


def pegaYrot(x, y, g):
    return int(x*math.sin(g) + y*math.cos(g))

# Função Rotação, vista em sala de aula, para se rotacionar tal objeto que está sendo
# seus pontos armazenados nas varias mousepos_x e mousepos_y.


def rotacao():
    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    g = int(rotAnglelabel.get(1.0, "end-1c"))
    g = math.radians(g)

    tam = len(mousepos_x)

    posx = mousepos_x[0]
    posy = mousepos_y[0]

    cordsX = []
    cordsY = []
    # Calculo para ver o quanto é necessário para transladar o PONTO INICIAL para chegar no CENTRO
    aux = MEIOX - mousepos_x[0]
    aux1 = MEIOY - mousepos_y[0]
    # Com as auxiliares calculadas, translada os pontos para o centro
    for i in range(0, tam, 1):
        mousepos_x[i] = mousepos_x[i]+aux
        mousepos_y[i] = mousepos_y[i]+aux1
    # Aplica as correlações matemáticas
    for i in range(0, tam, 1):
        cordsX.append(pegaXrot(mousepos_x[i]-MEIOX, mousepos_y[i]-MEIOY, g))
        cordsY.append(pegaYrot(mousepos_x[i]-MEIOX, mousepos_y[i]-MEIOY, g))
    # Translada novamente para a posição original.
    for i in range(0, tam, 1):
        mousepos_x[i] = cordsX[i]+posx
        mousepos_y[i] = cordsY[i]+posy
    UpdateFunction()
    # Printa novamente os pontos já rotacionados
    for i in range(0, tam-1, 1):
        Reta(mousepos_x[i], mousepos_y[i], mousepos_x[i+1], mousepos_y[i+1])

    Reta(mousepos_x[0], mousepos_y[0], mousepos_x[tam-1], mousepos_y[tam-1])

# Função Escala, vista em sala de aula, para se escalonar tal objeto que está sendo
# seus pontos armazenados nas varias mousepos_x e mousepos_y.


def escala():
    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    esc = float(escalalabel.get(1.0, "end-1c"))

    tam = len(mousepos_x)
    posx = mousepos_x[0]
    posy = mousepos_y[0]
    # Calculo para ver o quanto é necessário para transladar o PONTO INICIAL para chegar no CENTRO
    aux = MEIOX - mousepos_x[0]
    aux1 = MEIOY - mousepos_y[0]
    # Com as auxiliares calculadas, translada os pontos para o centro
    for x in range(0, tam, 1):
        mousepos_x[x] = mousepos_x[x]+aux
        mousepos_y[x] = mousepos_y[x]+aux1
    # Aplica as correlações matemáticas
    for x in range(0, tam, 1):
        mousepos_x[x] = round((mousepos_x[x]-MEIOX)*esc)
        mousepos_y[x] = round((mousepos_y[x]-MEIOY)*esc)
    # Translada novamente para a posição original.
    for x in range(0, tam, 1):
        mousepos_x[x] = mousepos_x[x]+posx
        mousepos_y[x] = mousepos_y[x]+posy
    UpdateFunction()
    # Printa novamente os pontos já rotacionados
    for i in range(0, tam-1, 1):
        Reta(mousepos_x[i], mousepos_y[i],
             mousepos_x[i+1], mousepos_y[i+1])
    Reta(mousepos_x[0], mousepos_y[0],
         mousepos_x[tam-1], mousepos_y[tam-1])


def reflexao_XY():
    # inverte o sinal das duas coordenadas, ficando no plano x negativo, y positivo
    tam = len(mousepos_x)
    posx = mousepos_x[0]
    posy = mousepos_y[0]
    # Calculo para ver o quanto é necessário para transladar o PONTO INICIAL para chegar no CENTRO
    aux = MEIOX - mousepos_x[0]
    aux1 = MEIOY - mousepos_y[0]
    # Com as auxiliares calculadas, translada os pontos para o centro
    # Realiza as correlações matemáticas e translada para o ponto inicial novamente.
    for i in range(0, tam, 1):
        mousepos_x[i] = mousepos_x[i]+aux
        mousepos_y[i] = mousepos_y[i]+aux1
        mousepos_x[i] = (mousepos_x[i]-MEIOX)*(-1)
        mousepos_y[i] = (mousepos_y[i]-MEIOY)*(-1)
        mousepos_x[i] = int(mousepos_x[i]+posx)
        mousepos_y[i] = int(mousepos_y[i]+posy)
    UpdateFunction()
    # Printa novos pontos já refletidos
    for i in range(0, tam-1, 1):
        Reta(mousepos_x[i], mousepos_y[i],
             mousepos_x[i+1], mousepos_y[i+1])
    Reta(mousepos_x[0], mousepos_y[0],
         mousepos_x[tam-1], mousepos_y[tam-1])


def reflexao_X():
    # inverte o sinal da coordenada y
    tam = len(mousepos_x)
    posy = mousepos_y[0]
    # Calculo para ver o quanto é necessário para transladar o PONTO INICIAL para chegar no CENTRO
    aux = MEIOY - mousepos_y[0]
    # Com as auxiliares calculadas, translada os pontos para o centro
    # Realiza as correlações matemáticas e translada para o ponto inicial novamente.
    for i in range(0, tam, 1):
        mousepos_y[i] = mousepos_y[i]+aux
        mousepos_y[i] = (mousepos_y[i]-MEIOY)*(-1)
        mousepos_y[i] = int(mousepos_y[i]+posy)
    UpdateFunction()
    # Printa novos pontos já refletidos
    for i in range(0, tam-1, 1):
        Reta(mousepos_x[i], mousepos_y[i],
             mousepos_x[i+1], mousepos_y[i+1])
    Reta(mousepos_x[0], mousepos_y[0],
         mousepos_x[tam-1], mousepos_y[tam-1])


def reflexao_Y():
    # inverte o sinal da coordenada x
    tam = len(mousepos_x)
    posx = mousepos_x[0]
    # Calculo para ver o quanto é necessário para transladar o PONTO INICIAL para chegar no CENTRO
    aux = MEIOX - mousepos_x[0]
    # Com as auxiliares calculadas, translada os pontos para o centro
    # Realiza as correlações matemáticas e translada para o ponto inicial novamente.
    for i in range(0, tam, 1):
        mousepos_x[i] = mousepos_x[i]+aux
        mousepos_x[i] = (mousepos_x[i]-MEIOX)*(-1)
        mousepos_x[i] = int(mousepos_x[i]+posx)
    UpdateFunction()
    # Printa novos pontos já refletidos
    for i in range(0, tam-1, 1):
        Reta(mousepos_x[i], mousepos_y[i], mousepos_x[i+1], mousepos_y[i+1])

    Reta(mousepos_x[0], mousepos_y[0], mousepos_x[tam-1], mousepos_y[tam-1])

# Region Code, modificado um pouco para se adaptar ao
# Canvas onde a posição 0,0 não é no centro, mas sim no superior esquerdo.
# Logo, Y terá influencia, pois será inversamente proporcional, logo ao invés
# do padrão ser os bits TOP DOWN RIGHT LEFT, será DOWN TOP RIGHT LEFT.


def region_code(x, y, xmin, xmax, ymin, ymax):
    codigo = 0
    if(x < xmin and y < ymin):
        codigo = 5
    elif(x < xmin and y > ymax):
        codigo = 9
    elif(x < xmin and y >= ymin and y <= ymax):
        codigo = 1
    elif(x >= xmin and x <= xmax and y > ymax):
        codigo = 8
    elif(x >= xmin and x <= xmax and y < ymin):
        codigo = 4
    elif(x > xmax and y < ymin):
        codigo = 6
    elif(x > xmax and y > ymax):
        codigo = 10
    elif(x > xmax and y >= ymin and y <= ymax):
        codigo = 2
    return codigo

# Algoritmo de Recorte Cohen Sutherland visto em sala de aula.


def cohen_sutherland():
    aceite = False
    feito = False
    # Resgata os dados obtidos nos labels correspondentes e armazena nas variaveis
    # da janela
    xmin = int(RGxminlabel.get(1.0, "end-1c"))
    ymin = int(RGyminlabel.get(1.0, "end-1c"))
    xmax = int(RGxmaxlabel.get(1.0, "end-1c"))
    ymax = int(RGymaxlabel.get(1.0, "end-1c"))

    UpdateFunction()

    Reta(xmin, ymin, xmin, ymax)  # PRINTANDO JANELA
    Reta(xmin, ymin, xmax, ymin)  # printando janela
    Reta(xmax, ymin, xmax, ymax)  # PRINTANDO JANELA
    Reta(xmin, ymax, xmax, ymax)  # printando janela

    tam = len(mousepos_x)
    # Fazendo recortes entre os pontos
    # Só entra se tam for maior que 2, uma vez que se não for, significa que só existem
    # 2 pontos no poligono, portanto não é necessário um for para percorrer os pontos.
    if (tam > 2):
        for i in range(0, tam-1, 1):
            x1 = mousepos_x[i]
            y1 = mousepos_y[i]
            x2 = mousepos_x[i+1]
            y2 = mousepos_y[i+1]

            aceite = False
            feito = False

            while(not feito):
                c1 = region_code(x1, y1, xmin, xmax, ymin, ymax)
                c2 = region_code(x2, y2, xmin, xmax, ymin, ymax)

                if(c1 == 0 and c2 == 0):  # segmento totalmente dentro
                    aceite = True
                    feito = True
                elif(c1 & c2) != 0:
                    feito = True
                else:
                    if(c1 != 0):
                        cfora = c1
                    else:
                        cfora = c2
                    if(int(bin(cfora)[2:].zfill(8)[7]) == 1):  # indice 0 do bit
                        xint = xmin
                        yint = y1 + (y2-y1)*((xmin-x1)/(x2-x1))
                    elif(int(bin(cfora)[2:].zfill(8)[6]) == 1):  # indice 1 do bit
                        xint = xmax
                        yint = y1 + (y2-y1)*((xmax-x1)/(x2-x1))
                    elif(int(bin(cfora)[2:].zfill(8)[5]) == 1):  # indice 2 do bit
                        yint = ymin
                        xint = x1 + (x2 - x1)*(ymin - y1)/(y2-y1)
                    elif(int(bin(cfora)[2:].zfill(8)[4]) == 1):  # indice 3 do bit
                        yint = ymax
                        xint = x1 + (x2 - x1)*((ymax - y1)/(y2-y1))
                    if(c1 == cfora):
                        x1 = xint
                        y1 = yint
                    else:
                        x2 = xint
                        y2 = yint
                if(aceite):
                    Reta(round(x1), round(y1), round(x2), round(y2))

    # Fazendo o recorte entre o ultimo ponto e o primeiro agora.

    x1 = mousepos_x[0]
    y1 = mousepos_y[0]
    x2 = mousepos_x[tam-1]
    y2 = mousepos_y[tam-1]

    aceite = False
    feito = False

    while(not feito):
        c1 = region_code(x1, y1, xmin, xmax, ymin, ymax)
        c2 = region_code(x2, y2, xmin, xmax, ymin, ymax)

        if(c1 == 0 and c2 == 0):  # segmento totalmente dentro
            aceite = True
            feito = True
        elif(c1 & c2) != 0:
            feito = True
        else:
            if(c1 != 0):
                cfora = c1
            else:
                cfora = c2
            if(int(bin(cfora)[2:].zfill(8)[7]) == 1):  # indice 0 do bit
                xint = xmin
                yint = y1 + (y2-y1)*((xmin-x1)/(x2-x1))
            elif(int(bin(cfora)[2:].zfill(8)[6]) == 1):  # indice 1 do bit
                xint = xmax
                yint = y1 + (y2-y1)*((xmax-x1)/(x2-x1))
            elif(int(bin(cfora)[2:].zfill(8)[5]) == 1):  # indice 2 do bit
                yint = ymin
                xint = x1 + (x2 - x1)*(ymin - y1)/(y2-y1)
            elif(int(bin(cfora)[2:].zfill(8)[4]) == 1):  # indice 3 do bit
                yint = ymax
                xint = x1 + (x2 - x1)*((ymax - y1)/(y2-y1))
            if(c1 == cfora):
                x1 = xint
                y1 = yint
            else:
                x2 = xint
                y2 = yint
        if(aceite):
            Reta(round(x1), round(y1), round(x2), round(y2))

# Algoritmo de ClipTest, visto em sala de aula.


def cliptest(p, q, u):
    print(p, q, u[0], u[1])
    result = True
    if(p < 0.0):
        r = q/p
        if(r > u[1]):
            result = False  # Fora da janela
        elif(r > u[0]):
            u[0] = r
    elif(p > 0.0):
        r = q/p
        if(r < u[0]):
            result = False
        elif(r < u[1]):
            u[1] = r
    elif(q < 0.0):
        result = False

    print(result)

    return result

# Função LIANG_BARSKY vista em sala de aula


def liang_barsky():

    # Resgata os valores dos labels e armazena nas variaveis correspondentes.
    xmin = int(EPxminlabel.get(1.0, "end-1c"))
    ymin = int(EPyminlabel.get(1.0, "end-1c"))
    xmax = int(EPxmaxlabel.get(1.0, "end-1c"))
    ymax = int(EPymaxlabel.get(1.0, "end-1c"))

    tam = len(mousepos_x)

    UpdateFunction()
    # Printa janela
    Reta(xmin, ymin, xmin, ymax)
    Reta(xmin, ymin, xmax, ymin)
    Reta(xmax, ymin, xmax, ymax)
    Reta(xmin, ymax, xmax, ymax)

    # Fazendo recortes entre os pontos
    # Só entra se tam for maior que 2, uma vez que se não for, significa que só existem
    # 2 pontos no poligono, portanto não é necessário um for para percorrer os pontos.
    if(tam > 2):
        for i in range(0, tam - 1, 1):
            x1 = mousepos_x[i]
            y1 = mousepos_y[i]
            x2 = mousepos_x[i+1]
            y2 = mousepos_y[i+1]
            u = []
            u.append(0.0)
            u.append(1.0)
            dx = x2 - x1
            dy = y2 - y1

            if(cliptest(-dx, x1-xmin, u)):
                if(cliptest(dx, xmax - x1, u)):
                    if(cliptest(-dy, y1-ymin, u)):
                        if(cliptest(dy, ymax-y1, u)):
                            if(u[1] < 1.0):
                                x2 = x1+u[1]*dx
                                y2 = y1+u[1]*dy
                            if(u[0] > 0.0):
                                x1 = x1+u[0]*dx
                                y1 = y1+u[0]*dy
                            Reta(round(x1), round(y1), round(x2), round(y2))

    # Recorte entre o ponto inicial e o ponto final

    x1 = mousepos_x[0]
    y1 = mousepos_y[0]
    x2 = mousepos_x[tam-1]
    y2 = mousepos_y[tam-1]
    u = []
    u.append(0.0)
    u.append(1.0)
    dx = x2 - x1
    dy = y2 - y1

    if(cliptest(-dx, x1-xmin, u)):
        if(cliptest(dx, xmax - x1, u)):
            if(cliptest(-dy, y1-ymin, u)):
                if(cliptest(dy, ymax-y1, u)):
                    if(u[1] < 1.0):
                        x2 = x1+u[1]*dx
                        y2 = y1+u[1]*dy
                    if(u[0] > 0.0):
                        x1 = x1+u[0]*dx
                        y1 = y1+u[0]*dy
                    Reta(round(x1), round(y1), round(x2), round(y2))

# Função para detectar onde o mouse está, e após o CLICK ela salva as coordenadas na variavel mousepos_x e mousepos_y
# q será utilizada para basicamente tudo dentro do código


def motion(event):
    mousepos_x.append(int(event.x))
    mousepos_y.append(int(event.y))
    tam = len(mousepos_x)
    img.put("#ff0000", (mousepos_x[tam-1], mousepos_y[tam-1]))

# Função para plotar os pontos obtidos através do click do mouse na função motion()


def plotPoints():
    tam = len(mousepos_x)
    for x in range(0, tam-1, 1):
        Reta(mousepos_x[x], mousepos_y[x],
             mousepos_x[x+1], mousepos_y[x+1])
    Reta(mousepos_x[0], mousepos_y[0],
         mousepos_x[tam-1], mousepos_y[tam-1])


canvas.bind('<Button-1>', motion)


print("Janela Criada, maximize-a para melhor utilização.")

# Manipulação de Labels e InputTexts

transXlabel = tk.Text(window, height=1, width=5)
transXlabel.pack()
transXlabel.place(x=100, y=30)

transYlabel = tk.Text(window, height=1, width=5)
transYlabel.pack()
transYlabel.place(x=150, y=30)

rotAnglelabel = tk.Text(window, height=1, width=5)
rotAnglelabel.pack()
rotAnglelabel.place(x=85, y=62)

escalalabel = tk.Text(window, height=1, width=5)
escalalabel.pack()
escalalabel.place(x=80, y=92)

retaX1label = tk.Text(window, height=1, width=5)
retaX1label.pack()
retaX1label.place(x=140, y=152)

retaY1label = tk.Text(window, height=1, width=5)
retaY1label.pack()
retaY1label.place(x=190, y=152)

retaX2label = tk.Text(window, height=1, width=5)
retaX2label.pack()
retaX2label.place(x=240, y=152)

retaY2label = tk.Text(window, height=1, width=5)
retaY2label.pack()
retaY2label.place(x=290, y=152)

circunCxlabel = tk.Text(window, height=1, width=5)
circunCxlabel.pack()
circunCxlabel.place(x=120, y=182)

circunCylabel = tk.Text(window, height=1, width=5)
circunCylabel.pack()
circunCylabel.place(x=170, y=182)

circunRlabel = tk.Text(window, height=1, width=5)
circunRlabel.pack()
circunRlabel.place(x=220, y=182)

RGxminlabel = tk.Text(window, height=1, width=5)
RGxminlabel.pack()
RGxminlabel.place(x=150, y=212)

RGyminlabel = tk.Text(window, height=1, width=5)
RGyminlabel.pack()
RGyminlabel.place(x=200, y=212)

RGxmaxlabel = tk.Text(window, height=1, width=5)
RGxmaxlabel.pack()
RGxmaxlabel.place(x=250, y=212)

RGymaxlabel = tk.Text(window, height=1, width=5)
RGymaxlabel.pack()
RGymaxlabel.place(x=300, y=212)

EPxminlabel = tk.Text(window, height=1, width=5)
EPxminlabel.pack()
EPxminlabel.place(x=150, y=242)

EPyminlabel = tk.Text(window, height=1, width=5)
EPyminlabel.pack()
EPyminlabel.place(x=200, y=242)

EPxmaxlabel = tk.Text(window, height=1, width=5)
EPxmaxlabel.pack()
EPxmaxlabel.place(x=250, y=242)

EPymaxlabel = tk.Text(window, height=1, width=5)
EPymaxlabel.pack()
EPymaxlabel.place(x=300, y=242)

# Manipulação de Botões

butPoints = Button(window, text="Plot Points", activebackground="black",
                   command=plotPoints)
butPoints.pack()
butPoints.place(x=880, y=500)

butRemove = Button(window, text="Reset", activebackground="black",
                   command=resetCanvas)
butRemove.pack()
butRemove.place(x=980, y=500)

butRemove = Button(window, text="Undo", activebackground="black",
                   command=undoCanvas)
butRemove.pack()
butRemove.place(x=1080, y=500)

a = Button(window, text="Translacao", activebackground="black",
           command=translacao)
a.pack()
a.place(x=20, y=30)

b = Button(window, text="Rotação", activebackground="black",
           command=rotacao)
b.pack()
b.place(x=20, y=60)

c = Button(window, text="Escala", activebackground="black",
           command=escala)
c.pack()
c.place(x=20, y=90)

d = Button(window, text="Reflexão XY", activebackground="black",
           command=reflexao_XY)
d.pack()
d.place(x=20, y=120)

d1 = Button(window, text="Reflexão X", activebackground="black",
            command=reflexao_X)
d1.pack()
d1.place(x=100, y=120)

d2 = Button(window, text="Reflexão Y", activebackground="black",
            command=reflexao_Y)
d2.pack()
d2.place(x=180, y=120)

e = Button(window, text="Bresenham", activebackground="black",
           command=Bresenham)
e.pack()
e.place(x=20, y=150)

e = Button(window, text="DDA", activebackground="black",
           command=DDA)
e.pack()
e.place(x=100, y=150)

f = Button(window, text="Circunferencia", activebackground="black",
           command=Circunferencia)
f.pack()
f.place(x=20, y=180)

g = Button(window, text="Regioes Codificadas", activebackground="black",
           command=cohen_sutherland)
g.pack()
g.place(x=20, y=210)

h = Button(window, text="Equação Paramétrica", activebackground="black",
           command=liang_barsky)
h.pack()
h.place(x=20, y=240)

mainloop()
