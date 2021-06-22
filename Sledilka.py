import tkinter, time

okno = tkinter.Tk();
okno.geometry('600x600+700+1');

holst = tkinter.Canvas(okno, width = 600, height = 600);
holst.pack();

holst['bg'] = '#BBAADD';

v = holst.create_polygon(100,100,
                         120,120,
                         80,120,
                         fill='#DDAABB');


kudKuda_x = 100;
kudKuda_y = 100;


def vadim(event):
    global kudKuda_x, kudKuda_y, dx, dy;
    kudKuda_x = event.x;
    kudKuda_y = event.y;
    ne = holst.coords(v);
    dx = (kudKuda_x - ne[0]) / 1000;
    dy = (kudKuda_y - ne[1]) / 1000;
    vv = abs(dx)+abs(dy);
    dx = 1 * dx / vv;
    dy = 1 * dy / vv;
    print(dx, dy);
okno.bind('<Button-1>', vadim);

while True:
    okno.update();
    time.sleep(0.001);

    ne = holst.coords(v);
    if kudKuda_x - 7 < ne[0] < kudKuda_x + 7:
       if kudKuda_y - 7 < ne[1] < kudKuda_y + 7:
           dx=0;
           dy=0;
    #0 === 0.0 ?
    holst.move( v , dx , dy);
    
    
