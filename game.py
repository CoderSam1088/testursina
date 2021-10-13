from ursina import *
import random

random_generator = random.Random()
textoffset = 0.0
textoffset2 = 0.0
cubes = []

def update():
   for i in range(len(cubes)):
      cubes[i].rotation_y += time.dt * 5       #rotates cube vertically
   if held_keys['q']:
      camera.position += (0, time.dt, 0)  #move up vertically if q is pressed
   if held_keys['a']:
      camera.position -= (0, time.dt, 0)  #move down vertically if a is pressed
   if held_keys['w']:
      camera.position += (time.dt, 0, 0)  #move right if q is pressed
   if held_keys['s']:
      camera.position -= (time.dt, 0, 0)  #move left if a is pressed
   if held_keys['z']:
      camera.position += (0, 0, time.dt)  #move in if z is pressed
   if held_keys['x']:
      camera.position -= (0, 0, time.dt)  #move out if x is pressed
   global textoffset
   global textoffset2
   textoffset += time.dt * 0.2            #increment slightly based on time
   setattr(cube, "texture_offset", (0, textoffset))   #set the texture offset
   textoffset2 += time.dt * 0.3
   setattr(cube2, "texture_offset", (0,textoffset2))
   #print(mouse.hovered_entity)
   if mouse.hovered_entity == cube:
      info.visible = True              #make text visible
   else:
      info.visible = False

def input(key):
   if key == 'space':
      """create random color"""
      red = random_generator.random() * 255
      green = random_generator.random() * 255
      blue = random_generator.random() * 255
      cube.color = color.rgb(red, green, blue)
   elif key == 'c':
      newx = random_generator.random()*5 -2.5
      newy = random_generator.random()*5 -2.5
      newz = random_generator.random()*5 -2.5
      red = random_generator.random() * 255
      green = random_generator.random() * 255
      blue = random_generator.random() * 255
      s = random_generator.random() * 1
      texnum = random_generator.random() * 1
      print(texnum)
      if texnum<0.5:
         tex = 'shroom_color.png'
      else:
         tex = 'shroom_color2.png'
      newcube = Entity(parent=cube, model='cube', color = color.rgb(red,green,blue), position = (newx, newy, newz), scale = (s,s/3,s), texture='crate')
      newcube = Entity(parent=cube, model='shrooms.obj', position = (newx, newy-1, newz), scale = (2*s, 2*s/3, 2*s), texture=tex)
      cubes.append(newcube)

      #create another child cube with the newcube as its parent
      num = random_generator.random()*5
      
      for i in range(int(num)):
         
         childcube = Entity(parent=newcube, model='cube', color=color.rgb(red,green,blue), position = (1,0,i), scale=(s/2,s/2,s/2), texture='crate')
         cubes.append(childcube)

   elif key == 'n':
      """create random scale"""
      newscale = random_generator.random()*5
      cube.scale = (newscale, newscale*3, newscale)
   elif key == 'p':
      """create random location"""
      newx = random_generator.random()*10 -5
      newy = random_generator.random()*10 -5
      cube.x = newx
      cube.y = -newy
      
      

app = Ursina()			          #initialize app

"""Setting up the window"""
window.title = 'My Game'		        #The window title
window.borderless = False		#Show a border
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True	#show the Frames per second counter

"""adding objects"""
cube = Entity(model='cube', color = color.white, scale = (2,6,2), texture='water', collider='box')
cube2 = Entity(parent=cube, model='cube', color = color.rgba(255,255,255,178), scale = (1.1, 1, 1.1), texture='water')
cubes.append(cube)
cubes.append(cube2)

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text ="A powerful waterfall roaring on the mountains")
info.x = -0.5
info.y = 0.4
info.background = True
info.visible = False            #Do not show the text


app.run()
