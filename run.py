import pyglet as pg
import UGsegment


NUM = 10
LEN = 50
win = pg.window.Window()
seg_list = [UGsegment.segment((0,0),LEN) for i in range(NUM)]

print('hi')
print('branch test')

def draw(x2, y2):
    batch = pg.graphics.Batch()
    for i in range(len(seg_list)):
        if(i==0):
            seg_list[0].update((x2, y2))
        else:
            seg_list[i].update(seg_list[i-1].origin)
        batch.add(2,pg.gl.GL_LINES,None,('v2i',(*seg_list[i].origin,*seg_list[i].target)))
    batch.draw()

@win.event
def on_mouse_motion(x, y, dx, dy):
    win.clear()
    draw(x,y)

pg.app.run()
