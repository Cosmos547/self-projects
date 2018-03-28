import pyglet
from random import randint

width, height = 500, 500

window = pyglet.window.Window(width=width, height=height)

image = pyglet.image.SolidColorImagePattern((77, 77, 255, 0)).create_image(width, height)

flake = pyglet.image.load('7-snowflake-png-image.png')

frame_counter = 0
batch = pyglet.graphics.Batch()

class SnowFlake(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.vx, self.vy = randint(-12,12), -randint(60,120)

        self.x, self.y  = randint(1,499), 500
        self.counter = 0
        self.scale = randint(3,5)/200

    def update(self, dt):
        self.counter += 1
        if (self.counter > 60):
            self.counter = 0
            self.vx = randint(-12, 12)
        self.x += self.vx*dt
        self.y += self.vy*dt


flakes = []


fps_display = pyglet.clock.ClockDisplay()

def update(dt):
    rx = randint(0, 100)
    if (rx < 95):
        flakes.append(SnowFlake(flake, batch = batch))
    for i in range(len(flakes)):
        if (i == len(flakes)):
            break
        print(str(i) + " " + str(len(flakes)))
        if (flakes[i].y < 0):
            del flakes[i]
            i -= 1
            continue
        flakes[i].update(dt)

pyglet.clock.schedule_interval(update, 1/60.0)


@window.event
def on_draw():
    global frame_counter
    window.clear()
    image.blit(0,0)
    batch.draw()
    pyglet.image.get_buffer_manager().get_color_buffer().save('saved/' + '%0*d' % (4, frame_counter)  + '.png')
    frame_counter += 1

pyglet.app.run()
