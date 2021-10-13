from ursina import *


app = Ursina()

cube = Entity(model = 'shrooms.obj', color = color.white, scale=(4,4,4), texture='shroom_color2')
app.run()
