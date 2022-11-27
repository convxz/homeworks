from turtle import *
delay(0)

def notch(ln, flag):
    """
    Вспомогательная для основной функция, делает насечку и пишет число на оси OX
    :param ln: число
    :param flag: определяет, будут ли числа на прямой
    :return: None
    """
    left(90)
    forward(5)
    if flag:
        if ln != 0:
            write(ln)
    back(10)
    forward(5)
    right(90)


def notchy(ln, flag):
    """
    Вспомогательная для основной функция, делает насечку и пишет число на оси OX
    :param ln: число
    :param flag: определяет, будут ли числа на прямой
    :return: None
    """
    left(90)
    forward(5)
    back(10)
    if flag:
        if ln != 0:
            write(ln)
    forward(5)
    right(90)


def arrow():
    """
    Вспомогательная для основной функция, делает стрелку в конце оси
    :return:
    """
    right(135)
    forward(12)
    backward(12)
    right(90)
    forward(12)
    backward(12)
    right(135)


# длина осей (разная) , центр координат, цвет оси, флаг, определяющий наличие цифр, масштаб
def main(len_x, len_y, center_pos=[0, 0], clr='black', flag=True, scale=30):
    """
    Функция рисует декартову плоскость с заданной длиной осей, с заданным центром, с возможностью убрать цифры, с
    регулируемым масштабом, а также можно задать цвет
    :param len_x: длина оси OX, если нечетная, прибавляется 1
    :param len_y: длина оси OY, если нечетная, прибавляется 1
    :param center_pos: координаты центра осей (по умолчанию (0;0))
    :param clr: цвет
    :param flag: если True, то плоскость с цифрами, иначе без
    :param scale: масштаб (сколько пикселей в отрезке длиной 1), по умолчанию равен 30
    :return: None
    """
    penup()
    setpos(center_pos[0], center_pos[1])
    pendown()
    color(clr)
    if len_x % 2 != 0:
        len_x += 1
    if len_y % 2 != 0:
        len_y += 1
    len_x *= scale
    len_y *= scale
    back(len_x//2)
    ln = -(len_x // 2)
    while ln < 0:
        notch(ln//scale, flag)
        forward(scale)
        ln += scale
    ln = len_x // 2
    i = 0
    while ln > 0:
        notch(i, flag)
        forward(scale)
        ln -= scale
        i += 1
    arrow()
    back(len_x//2)
    left(90)
    ln = 0
    while ln != len_y//2:
        notchy(ln//scale, flag)
        ln += scale
        forward(scale)
    arrow()
    back(ln)
    ln = -(len_y//2)
    i = 0
    while ln < 0:
        notchy(-1*i, flag)
        ln += scale
        back(scale)
        i += 1
    notchy(i, flag)
    forward(len_y//2)
    hideturtle()


main(8, 8, [0, 0], "#f23425", True, 70)
i = 0
while i < 14:
    right(60)
    forward(70)
    right(60)
    forward(70)
    right(270)
    i += 1
mainloop()
