
from pyclbr import Function

import pygame_widgets
import pygame
import keyboard
import math
import time
import random


import pygame.camera

from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.toggle import Toggle
start_time = 0
anim_time = 1


pygame.init()

def Get_CAM_zvt_prost():
        return ['RGB','HSV','YUV']
def Mod(num):
    if num < 0:num = -num
    return num

# 1
class Vec2:
        def __init__(self,vect2d_start=[-1],vect2d_end=[-1],pos=[0,0]): 
            if vect2d_start[0]!=-1 and vect2d_end[0]!=-1:
                self.vect2d_start = vect2d_start
                self.vect2d_end = vect2d_end
                self.vec2D = [self.vect2d_start,self.vect2d_end]
                self.x = vect2d_end[0]-vect2d_start[0]
                self.y = vect2d_end[1]-vect2d_start[1]
            else:
                self.x = pos[0]
                self.y = pos[1]
            self.size = int(math.sqrt(self.x**2+self.y**2))
            self.absv = Mod(self.size)
            self.pos1 = [self.x,self.y]
        def raV_2D(self,vector2D):
            parperx_st_ = int(vector2D.vect2d_start[0]-self.vect2d_start[0])
            parperx_en_ = int(vector2D.vect2d_end[0]-self.vect2d_end[0])
            parpery_st_ = int(vector2D.vect2d_start[1]-self.vect2d_start[1])
            parpery_en_ = int(vector2D.vect2d_end[1]-self.vect2d_end[1])
            if Mod(parperx_st_) == Mod(parperx_en_) and Mod(parpery_st_) == Mod(parpery_en_):
                return True
            else:
                return False
        def poV_2D(self,ugl):
            pos = [int(self.x*math.cos(ugl)-self.y*math.sin(ugl)),int(self.y*math.cos(ugl)+self.x*math.sin(ugl))]
            vec3 = Vec2(pos=pos)
            return vec3
        def sum(self,vector2D):
            pos=[self.x+vector2D.x,self.y+vector2D.y]
            vec3 = Vec2(pos=pos)
            return vec3
        def raz(self,vector2D):
            pos=[self.x-vector2D.x,self.y-vector2D.y]
            vec3 = Vec2(pos=pos)
            return vec3
        def umn(self,delta):
            pos=[self.x*delta,self.y*delta]
            vec3 = Vec2(pos=pos)
            return vec3
        def scal(self,vector2D):
            scl = self.x*vector2D.x+self.y*vector2D.y
            return scl
        def nul(self):
            if self.vect2d_end==self.vect2d_start:return True
            else:return False
        def nap(self,vector2D):
            parperx_st_ = int(vector2D.vect2d_start[0]-self.vect2d_start[0])
            parperx_en_ = int(vector2D.vect2d_end[0]-self.vect2d_end[0])
            parpery_st_ = int(vector2D.vect2d_start[1]-self.vect2d_start[1])
            parpery_en_ = int(vector2D.vect2d_end[1]-self.vect2d_end[1])
            
            if parperx_en_ == parperx_st_ and parpery_en_ == parpery_st_ :
                    return True
            else:
                    return False     
# 2
class Surfases:
    def __init__(self,size=[]):
        self.surf = pygame.Surface((size[0],size[1]))
        surf1 = self.surf
        return surf1

    def set_alphal(self,al):
        if al > 255:al=255
        if al < 0:al=0
        self.surf.set_alpha(al)
        
    def draw_surf(self,pos=[]):
        screen.blit(self.surf,(pos[0],pos[1]))

    def draw_on_surf(self,sr1,sr2,pos=[]):
        sr1.blit(sr2,(pos[0],pos[1]))

    def fill_surf(self,col=()):
        self.surf.fill(col)

    class Trans:
        def __init__(self):
            pass
# 3        
class Kamera:
    def __init__(self,size,zvet_prost='RGB',num=0):
        self.size = size
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[num],(size[0],size[1]), zvet_prost)
        self.cam.set_controls(True,False,1)

    def List_cam(self):
        cams = pygame.camera.list_cameras()
        return cams
    
    def Start(self):self.cam.start()

    def End(self):self.cam.stop()

    def Get_img(self):
        img = self.cam.get_image()
        return img

    def Get_size(self):
        width , height = self.cam.get_size()
        return width , height
    
    def Set_setings(self,wflip,hflip,sun):
        self.cam.set_controls(wflip,hflip,sun)

    def Get_setings(self):
        cont = self.cam.get_controls()
        return cont
# 4
class TimeGR:
    def __init__(self):
        pass
    def DELY(self,MLsec):
        time.sleep(MLsec)
# 5 
class Text_:
    def __init__(self,screen_size=[],text='',glass=False,col=(),font='arial',pix=0,pos=[]):
        
        pygame.font.init()

        self.win_w = screen_size[0]
        self.win_h = screen_size[1]
        self.text = text
        self.pos = pos
        self.pix = pix
        self.font = font
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.pos = [self.x,self.y]
        self.glass = glass
        self.col = col
        textt = pygame.font.SysFont(self.font,self.pix)
        texttt = textt.render(self.text,self.glass,self.col)
        screen1 = pygame.display.set_mode((self.win_w,self.win_h))
        self.init_text = textt
        self.texttt = texttt   
        self.screen1 = screen1
    def Render(self,pos=[None,None]): 
        if pos[0]!=None and pos[1]!=None:
            self.x = pos[0] ; self.y = pos[1]
        screen.blit(self.texttt,(self.x,self.y))
    def Set_text(self,text=''):
        self.text = text
    def Set_pos(self,pos=[]):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]  
    def Set_col(self,col):
        self.col = col
    def Get_col(self):
        return self.col
    def Set_bg(self,col=(0,0,0)):
        bg = Screen_.Shape2D.Rect(col,[self.x,self.y],[len(self.text)*12.5+len(self.text)+len(self.text),self.pix+10],0,self.screen1)
        bg.Draw()
        screen.blit(self.texttt,(self.x,self.y))      
# 6 -- new !! do not work
class Math_:
    def __init__(self):
        pass
    def COS(self,ugl):
        return math.cos(ugl)
    def SIN(self,ugl):
        return math.sin(ugl) 
    def Rast(self,pos1=[],pos2=[]):
        if pos1[0]>pos2[0]:w = pos1[0]-pos2[0]
        else:              w = pos2[0]-pos1[0]
        if pos1[1]>pos2[1]:h = pos1[1]-pos2[1]
        else:              h = pos2[1]-pos1[1]
        dl = math.sqrt(w*w+h*h)
        return dl   
# 7 
class Color_:
    def __init__(self,r,g,b,hsv=0):
        self.hsv = hsv
        self.r = r
        self.b = b
        self.g = g
        if self.r == 'r' or self.r == 'R':self.r = random.randint(0,255)
        if self.g == 'r' or self.g == 'R':self.g = random.randint(0,255)
        if self.b == 'r' or self.b == 'R':self.b = random.randint(0,255)
        self.r = self.r - self.hsv
        self.g = self.g - self.hsv
        self.b = self.b - self.hsv
        if self.r < 0:    self.r = 0
        if self.g < 0:    self.g = 0
        if self.b < 0:    self.b = 0
        if self.r > 255:  self.r = 255
        if self.g > 255:  self.g = 255
        if self.b > 255:  self.b = 255
        self.color = (self.r,self.g,self.b)
    def Set_hsv(self,hsv):

        self.hsv = hsv
        self.r = self.r - self.hsv
        self.g = self.g - self.hsv
        self.b = self.b - self.hsv
        if self.r < 0:    self.r = 0
        if self.g < 0:    self.g = 0
        if self.b < 0:    self.b = 0
        if self.r > 255:  self.r = 255
        if self.g > 255:  self.g = 255
        if self.b > 255:  self.b = 255
        self.color = (self.r,self.g,self.b)
        return self.color
    def Color_mesh(self,color,mesh=0.5):
        hsv = (self.hsv + color.hsv)/mesh
        r = (self.r + color.r)/mesh
        g = (self.g + color.g)/mesh
        b = (self.b + color.b)/mesh
        col = Color_(r,g,b,hsv)
        return col   
    def Color_Reverse(self):
        if self.r <= 127.5:r = 127.5+(127.5-self.r) 
        if self.g <= 127.5:g = 127.5+(127.5-self.g) 
        if self.b <= 127.5:b = 127.5+(127.5-self.b)  
        if self.r >  127.5:r = 127.5-(self.r - 127.5 ) 
        if self.g >  127.5:g = 127.5-(self.g - 127.5 ) 
        if self.b >  127.5:b = 127.5-(self.b - 127.5 ) 
        hsv = -self.hsv
        col = Color_(r,g,b,hsv)
        return col  
    def Set_hb(self):
        gr = (self.color[0]+self.color[1]+self.color[2])/3
        hsv = 0
        col = Color_(gr,gr,gr,hsv)
        return col
# 8 
class Sub_:
    def __init__(self):
        pass
    class Bord:
        def __init__(self):
            pass
        def On_key_press(self,key):
            on = keyboard.is_pressed(key)
            return on
        def Key_function(self,key,function):
            if True==keyboard.is_pressed(key):
                function()
    class Mouse:
        def __init__(self):
            pass
        def Get_Pos(self):
            pos = pygame.mouse.get_pos();  return pos
        def Get_pres(self,but=""):
            pr = pygame.mouse.get_pressed()
            if but == "l":  return pr[0]
            elif but == "r":  return pr[2]
            elif but == "m":  return pr[1]
        def Pres_function(self,button,function):
            pr = pygame.mouse.get_pressed()
            if button == "l" and pr[0] == True:  
                function()
            elif button == "r" and pr[2] == True:  
                function()
            elif button == "m" and pr[1] == True:  
                function()
        def Set_viz(self,viz):
            pygame.mouse.set_visible(viz)
        def Get_viz(self):
            viz = pygame.mouse.get_visible()
            return viz
        def Set_pos(self,pos=[]):
            pygame.mouse.set_pos([pos[0],pos[1]])
# 9 
class Screen_:
    def __init__(self,size=[],caption='Program'):
        global screen,clock


        self.win_size = size
        self.width = self.win_size[0]
        self.height = self.win_size[1]
        self.up = 0
        self.down = self.height
        self.left = 0
        self.right = self.width

        self.caption = caption

        pygame.init()
        pygame.display.init()
        
        
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.caption)

        self.clock = clock
        self.screen = screen
    def set_alpha(self,alp):
        screen.set_alpha(alp)
    def get_color(self,x,y):
        col = screen.get_at([x,y])
        col1 = [col[0],col[1],col[2]]
        return col1
    def get_center(self):
        xc = self.width/2
        yc = self.height/2
        return xc , yc
    def set_fps(self,fps):

        if fps == "MAX":fps = 1000
        if fps == "MIN":fps = 30
        self.clock.tick(fps)
    def get_fps(self):return int(self.clock.get_fps())
    def close(self,running=True):  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        events = pygame.event.get()        
        pygame_widgets.update(events)
        
        
        return running
    def Get_event(self):
        events = pygame.event.get()
        return events
    def functions(self,functions=[]):
        for i in range(len(functions)):
            functions[i]()
    class Update:
        def __init__(self):  
            pygame.display.flip()
        def Get_time(self):
            global start_time
            start_time+=1
            return start_time
            
        def BG_col(self,col= (0,0,0)):
            screen.fill(col)
    class Shape2D:
                                            def __init__(self):
                                                pass
                                            class Rect:
                                                def __init__(self,col=(),pos=[],size=[],sh=0,surf=0):
                                                    sh2 = 1
                                                    center =  [pos[0] + size[0]/2,pos[1]+size[1]/2]
                                                    pos=[pos[0],pos[1]]
                                                    up = [pos[0],pos[1]]
                                                    down = [pos[0]+size[1],pos[1]+size[0]]
                                                    right = [pos[0]+size[1],pos[1]+size[0]]
                                                    left = [pos[0],pos[1]]
                                                    self.pos = pos
                                                    self.size = size
                                                    self.surf = surf
                                                    self.col = col
                                                    self.sh = sh
                                                    self.sh2 = sh2
                                                    self.center = center    
                                                    self.up = up
                                                    self.down = down   
                                                    self.left = left 
                                                    self.right = right      
                                                    self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])                        
                                                def Draw(self):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.rect(
                                                        self.surf, 
                                                        self.col, 
                                                        self.rect,
                                                        self.sh
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.rect(
                                                        self.surf, 
                                                        self.col, 
                                                        self.rect,
                                                        self.sh
                                                    )
                                                    
                                                    pygame.draw.rect(
                                                        self.surf,
                                                        col,
                                                        self.rect,
                                                        self.sh2
                                                    )                                             
                                                def Obv(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.rect(
                                                        self.surf,
                                                        col,
                                                        self.rect,
                                                        self.sh2
                                                    )
                                                def Set_size(self,size2=[]):
                                                    self.size = size2
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Set_col(self,col2=()):
                                                    self.col = col2
                                                def Get_size(self):
                                                    return self.size
                                                def Get_sh(self):
                                                    return self.sh
                                                def Set_sh2(self,sh2):
                                                    self.sh2=sh2
                                                def Get_center(self):
                                                    return self.center
                                                def Get_surf(self):
                                                    return self.surf
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Set_pos(self,pos):
                                                    self.pos = pos
                                                    up = [pos[0],pos[1]]
                                                    down = [pos[0]+self.size[1],pos[1]+self.size[0]]
                                                    right = [pos[0]+self.size[1],pos[1]+self.size[0]]
                                                    left = [pos[0],pos[1]]
                                                    self.up = up
                                                    self.down = down   
                                                    self.left = left 
                                                    self.right = right 
                                                    self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                def On_colider(self,rect):
                                                    none = self.rect.colliderect(rect)
                                                    return none
                                                    
                                            class Circle:
                                                def __init__(self,col=(),pos=[],rad=0,sh=0,surf=0):
                                                    center = [pos[0],pos[1]]
                                                    sh2 = 1
                                                    self.sh2 = sh2
                                                    self.col = col
                                                    self.sh = sh
                                                    self.rad = rad
                                                    self.surf = surf
                                                    self.center = center
                                                    self.center = [pos[0],pos[1]]
                                                    self.pos = pos
                                                    up_cic = [pos[0],pos[1]-self.rad]
                                                    down_cic = [pos[0],pos[1]+self.rad]
                                                    left_cic = [pos[0]-self.rad,pos[1]]
                                                    right_cic = [pos[0]+self.rad,pos[1]]
                                                    self.up = up_cic
                                                    self.down = down_cic
                                                    self.left = left_cic
                                                    self.right = right_cic
                                                    self.rect = pygame.Rect(self.pos[0]-self.rad,self.pos[1]-self.rad,self.rad*2,self.rad*2)  
                                                def Draw(self):
                                                    pygame.draw.circle (
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh
                                                    )               
                                                def Obv(self,col=(0,0,0)):
                                                    pygame.draw.circle(
                                                        self.surf,
                                                        col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh2
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    pygame.draw.circle (
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh
                                                    )
                                                    pygame.draw.circle(
                                                        self.surf,
                                                        col,
                                                        (self.pos[0],self.pos[1]),
                                                        self.rad,
                                                        self.sh2
                                                    )          
                                                def Set_rad(self,rad2):
                                                    self.rad = rad2
                                                def Set_col(self,col2=()):
                                                    self.col = col2
                                                def Get_rad(self):
                                                    return self.rad
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_center(self):
                                                    return self.center
                                                def Get_surf(self):
                                                    return self.surf
                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2
                                                def Set_sh(self,sh2):
                                                    self.sh=sh2
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Get_sh(self):
                                                    return self.sh
                                                def Set_pos(self,pos):

                                                    self.pos = pos
                                                    up_cic = [pos[0],pos[1]-self.rad]
                                                    down_cic = [pos[0],pos[1]+self.rad]
                                                    left_cic = [pos[0]-self.rad,pos[1]]
                                                    right_cic = [pos[0]+self.rad,pos[1]]
                                                    self.up = up_cic
                                                    self.down = down_cic
                                                    self.left = left_cic
                                                    self.right = right_cic
                                                    self.rect = pygame.Rect(self.pos[0]-self.rad,self.pos[1]-self.rad,self.rad*2,self.rad*2)
                                                def On_colider(self,rect):
                                                    none = self.rect.colliderect(rect)
                                                    return none

                                            class Ellips:
                                                def __init__(self,col=(),pos=[],size=[],sh=0,surf=0):
                                                    center =  [pos[0] + size[0]/2,pos[1]+size[1]/2]
                                                    size=[size[0],size[1]]
                                                    sh2 = 1
                                                    self.sh2 = sh2
                                                    self.center = center
                                                    self.size = size
                                                    self.col = col
                                                    self.pos = pos
                                                    self.sh = sh
                                                    self.surf = surf
                                                    el_up = [pos[0]+size[0]/2,pos[1]]
                                                    el_down = [pos[0]+size[0]/2,pos[1]+size[1]]
                                                    el_left = [pos[0],pos[1]+size[1]/2]
                                                    el_right = [pos[0]+size[0],pos[1]+size[1]/2]
                                                    self.up = el_up
                                                    self.down = el_down
                                                    self.left = el_left
                                                    self.right = el_right
                                                    self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                def Draw(self):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(
                                                        self.surf,
                                                        self.col,
                                                        self.rect,
                                                        self.sh
                                                    )
                                                def Obv(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(self.surf,
                                                        col,
                                                        self.rect,
                                                        self.sh2
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(
                                                        self.surf,
                                                        self.col,
                                                        self.rect,
                                                        self.sh
                                                    )
                                                    rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                    self.rect = rect
                                                    pygame.draw.ellipse(self.surf,
                                                        col,
                                                        self.rect,
                                                        self.sh2
                                                    )
                                                def Set_size(self,size=[]):
                                                    self.size = size
                                                def Get_center(self):
                                                    return self.center
                                                def Get_sh(self):
                                                    return self.sh
                                                def Fyg(self):
                                                    return self.rectt
                                                def Get_surf(self):
                                                    return self.surf
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Get_size(self):
                                                    return self.size
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Set_pos(self,pos):
                                                    self.pos = pos
                                                    el_up = [pos[0]+self.size[0]/2,pos[1]]
                                                    el_down = [pos[0]+self.size[0]/2,pos[1]+self.size[1]]
                                                    el_left = [pos[0],pos[1]+self.size[1]/2]
                                                    el_right = [pos[0]+self.size[0],pos[1]+self.size[1]/2]
                                                    self.up = el_up
                                                    self.down = el_down
                                                    self.left = el_left
                                                    self.right = el_right
                                                    self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
                                                def On_colider(self,rect):
                                                    none = self.rect.colliderect(rect)
                                                    return none

                                            class Tringl:
                                                def __init__(self,col=(),pos1=[],pos2=[],pos3=[],sh=0,surf=0):  
                                                    rectt = [pos1,pos2,pos3,col,sh]
                                                    sh2 = 1
                                                    self.sh2 = sh2
                                                    self.col = col
                                                    self.pos1 = pos1
                                                    self.pos2 = pos2
                                                    self.pos3 = pos3
                                                    self.poses = [self.pos1,self.pos2,self.pos3]
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.rectt = rectt
                                                def Draw(self):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        self.col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh
                                                    )
                                                def Obv(self,col=(0,0,0)):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh2
                                                    )
                                                def DrOb(self,col=(0,0,0)):
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        self.col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh
                                                    )
                                                    pygame.draw.polygon(
                                                        self.surf,
                                                        col,
                                                        [(self.pos1[0],self.pos1[1]),(self.pos2[0],self.pos2[1]),(self.pos3[0],self.pos3[1])],
                                                        self.sh2
                                                    )
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_sh2(self):
                                                    return self.sh2
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Set_sh2(self,sh2):
                                                    self.sh2 = sh2
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_poses(self,poses=[]):
                                                    self.poses = poses
                                                    self.pos1 = poses[0]
                                                    self.pos2 = poses[1]
                                                    self.pos3 = poses[2]
                                                def Set_pos1(self,pos1=[]):
                                                    self.pos1 = pos1
                                                def Set_pos2(self,pos2=[]):
                                                    self.pos2 = pos2
                                                def Set_pos3(self,pos3=[]):
                                                    self.pos3 = pos3

                                            class Line:
                                                def __init__(self,col=(),start_pos=[],end_pos=[],sh=1,surf=0):
                                                    xcnt = start_pos[0]+(end_pos[0]-start_pos[0])/2;ycnt = start_pos[1]+(end_pos[1]-start_pos[1])/2
                                                    center = [xcnt,ycnt]
                                                    rectt = [start_pos,end_pos,center,col,sh]
                                                    self.x_center = xcnt
                                                    self.y_center = ycnt
                                                    self.center = center
                                                    self.rectt = rectt
                                                    self.col = col
                                                    self.start_pos = start_pos
                                                    self.end_pos = end_pos
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.poses = [self.start_pos,self.end_pos]
                                                def Draw(self):
                                                    pygame.draw.line( 
                                                        self.surf,
                                                        self.col,
                                                        (self.start_pos[0],self.start_pos[1]),
                                                        (self.end_pos[0],self.end_pos[1]),
                                                        self.sh
                                                    )
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_poses(self,poses=[]):
                                                    self.poses = poses
                                                    self.start_pos = poses[0]
                                                    self.end_pos = poses[1]
                                                def Set_start_pos(self,pos=[]):
                                                    self.start_pos = pos
                                                def Set_end_pos(self,pos=[]):
                                                    self.end_pos = pos
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Get_col(self):
                                                    return self.col
                                                def Get_poses(self):
                                                    return self.poses
                                                def Get_start_pos(self):
                                                    return self.start_pos
                                                def Get_end_pos(self):
                                                    return self.end_pos

                                            class Liness:
                                                def __init__(self,col=(),points=(),snap=False,sh=1,surf=0):
                                                    rectt = [points,col,snap,sh]

                                                    self.col = col
                                                    self.points = points
                                                    self.snap = snap
                                                    self.sh = sh
                                                    self.surf = surf
                                                    self.rectt = rectt  
                                                def Draw(self):
                                                    pygame.draw.lines( 
                                                        self.surf,
                                                        self.col,
                                                        self.snap,
                                                        self.points,
                                                        self.sh
                                                    )
                                                def Get_points_ind(self,index=0,cor=None):
                                                    if cor == None:
                                                        return self.points[index]
                                                    elif cor == "x" or cor == "X":
                                                        return self.points[index][0]
                                                    elif cor == "y" or cor == "Y":
                                                        return self.points[index][1]
                                                def Get_points(self):
                                                    return self.points
                                                def Get_col(self):
                                                    return self.col
                                                def Get_sh(self):
                                                    return self.sh
                                                def Get_snap(self):
                                                    return self.snap
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2

                                            class Pixel:
                                                def __init__(self,col=(),pos=[],sh=1,surf=0):   
                                                    rectt = [pos,col,sh]
                                                    
                                                    self.rectt = rectt
                                                    self.pos = pos
                                                    self.col = col
                                                    self.sh = sh
                                                    self.surf = surf
                                                def Draw(self):
                                                    pygame.draw.line(   
                                                        self.surf,
                                                        self.col,
                                                        (self.pos[0],self.pos[1]),
                                                        (self.pos[0],self.pos[1]),
                                                        self.sh
                                                    )
                                                def Get_pos(self):
                                                    return self.pos
                                                def Get_col(self):
                                                    return self.col
                                                def Get_sh(self):
                                                    return self.sh
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_pos(self,pos=[]):
                                                    self.pos = pos
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2

                                            class Arc:
                                                def __init__(self,col=(),pos=[],start_angle=0,stop_angle=0,rad=1,sh=1,st='-',surf=0):
                                                    grad = 56.5
                                                    ugl1 = start_angle/grad
                                                    rectt=[pos,start_angle,stop_angle,col,sh,st]

                                                    self.grad = grad
                                                    self.ugl = ugl1
                                                    self.start_angl = start_angle
                                                    self.end_angl = stop_angle
                                                    self.col = col
                                                    self.pos = pos
                                                    self.rad = rad
                                                    self.sh = sh
                                                    self.st = st
                                                    self.surf = surf
                                                    self.rectt = rectt                                                   
                                                def Draw(self):
                                                    
                                                    for l in range(int(self.end_angl*3.5)):
                                                        if self.st=='-': self.ugl+=0.005
                                                        elif self.st=='+': self.ugl-=0.005
                                                        for i in range(0,self.rad,2): 
                                                            xl=self.pos[0]+i*math.sin(self.ugl);yl=self.pos[1]+i*math.cos(self.ugl)
                                                            if i == self.rad - self.sh:
                                                                xpos = xl;ypos = yl
                                                        pygame.draw.line(self.surf,
                                                                        self.col,
                                                                        [xl,yl],
                                                                        [xpos,ypos],
                                                                        5)     
                                                def Set_end_ugl(self,ugl):
                                                    self.end_angl = ugl       
                                                def Set_start_ugl(self,ugl):
                                                    self.start_angl = ugl
                                                def Set_st(self,st='-'):
                                                    self.st = st     
                                                def Get_st(self):
                                                    return self.st
                                                def Get_col(self):
                                                    return self.col
                                                def Set_col(self,col):
                                                    self.col = col
                                                def Set_rad(self,rad):
                                                    self.rad = rad
                                                def Get_rad(self):
                                                    return self.rad
                                                def Set_sh(self,sh2):
                                                    self.sh = sh2
                                                def Get_sh(self):
                                                    return self.sh
# 10 
class Sprites_:
    def __init__(self,file=''):
        img = pygame.image.load(file)
        self.img = img
        self.start_img = img
        self.img_rect = self.start_img.get_rect()

    def Draw(self,pos=[]):
        self.pos = pos
        self.rect = self.img.get_rect(bottomright=(pos[0]+self.img.get_width(),pos[1]+self.img.get_height())) 
        screen.blit(self.img,self.rect)
        return self.rect

    def Set_pos(self,pos=[]):
        self.img_rect = self.start_img.get_rect(center=(pos[0],pos[1]))
        self.pos = pos

    def Scale(self,size=[]):
        self.img = pygame.transform.scale(self.img,(size[0],size[1]))
    
    def Rotate(self,ugl):
        self.img = pygame.transform.rotate(self.start_img,ugl)
    
    def Rotate_center(self,ugl):
        rot_img = pygame.transform.rotate(self.start_img,ugl)
        self.rect = rot_img.get_rect(center = self.img_rect.center)
        self.img = rot_img

    def Blit(self,rect):
        screen.blit(self.img,rect)

    def Get_rect(self):
        return self.start_img.get_rect()

    def Save(self,plane,file_name = ''):
        pygame.image.save(plane,file_name)


    def Get_pos(self):
        return self.pos
# 11 -- new !! do not work
class Sprites_Group_:
    def __init__(self,sprites=[]):
        self.sprites = sprites
        self.sprites_pack = []
        for i in self.sprites:
            self.sprites_pack.append(pygame.image.load(i))
    def Draw(self,pos=[0,0],sprite_index=0):
        self.pos = pos
        self.rect = self.sprites_pack[sprite_index].get_rect(bottomright=(pos[0]+self.sprites_pack[sprite_index].get_width(),
                                                                          pos[1]+self.sprites_pack[sprite_index].get_height())) 
        screen.blit(self.sprites_pack[sprite_index],self.rect)
# 12
class Graphick_:
    def __init__(self):
        pass
    def SETcirclGRAPH(self,col=[],znh=[]):
        pit = [col,znh]
        return pit
    def DRcirclGRAPH_2D(self,r=1,xp=1,yp=1,grph=[]):
        kf = 0
        ugl = 1;ugl1=1
        c=r
        g1 = 0
        for g in range(len(grph[0])):
            kf = kf + grph[0][g]

        for g in range(len(grph[1])):
            coll = grph[1][g]
            ugl = ugl1
            for n in range(int(700/kf*grph[0][g1])):
                xl = xp + c * math.sin(ugl)
                yl = yp + c * math.cos(ugl)
                ugl+=0.009
                pygame.draw.line(screen,coll,(xp,yp),(xl,yl),4)
                ugl1 = ugl


            g1 +=1
# 13 -- new !!
class Widgets_:
    def __init__(self):
        pass
    class Sliders:
        def __init__(self,plane,
                            pos=[],
                            len=100,
                            size=10,
                            min=0,
                            max=100,
                            step=1,
                            color_slider=(0,0,0),
                            handl_color=(30,30,30),
                            handl_radius=10,
                            curved = True
                            ):
            self.plane = plane
            self.pos = pos
            self.posx = pos[0]
            self.posy = pos[1]
            self.len = len
            self.curved = curved
            self.size = size
            self.min = min
            self.max = max
            self.step = step
            self.color_slider = color_slider
            self.handl_color = handl_color
            self.handl_radius = handl_radius
            slide = Slider(self.plane,
                            self.posx,
                            self.posy,
                            self.len,
                            self.size,
                            min = self.min,
                            max = self.max,
                            step = self.step,
                            colour = self.color_slider,
                            handleColour = self.handl_color,
                            handleRadius = self.handl_radius,
                            curved = self.curved)
            self.slide = slide
        def Get_value(self):
            val = self.slide.getValue()
            return val
        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)
        def Set_pos(self,pos=[]):
            self.pos = pos
            self.posx = pos[0]
            self.posy = pos[1]
            self.slide.setX(pos[0])
            self.slide.setY(pos[1])
        def Set_posx(self,x):
            self.posx = x
            self.slide.setX(x)
        def Set_posy(self,y):
            self.posy = y
            self.slide.setY(y)
        def Set_width(self,width):
            self.len = width
            self.slide.setWidth(width)
        def Set_height(self,height):
            self.size = height
            self.slide.setHeight(height)
        def Set_size(self,size=[]):
            self.size = size[1]
            self.len = size[0]
            self.slide.setHeight(size[1])
            self.slide.setWidth(size[0])
        def Hide(self):
            self.slide.hide()
        def Show(self):
            self.slide.show()
        def Set_value(self,value):
            self.slide.setValue(value)
        def Get_curved(self):
            return self.curved
        def Get_pos(self):
            return self.pos
        def Get_posx(self):
            return self.posx
        def Get_posy(self):
            return self.posy
        def Get_size(self):
            return self.size
        def Get_value(self):
            return self.slide.getValue()
        def Get_min(self):
            return self.min
        def Get_max(self):
            return self.max
        def Get_step(self):
            return self.step
        def Get_slider_color(self):
            return self.color_slider
        def Get_handl_color(self):
            return self.handl_color
        def Get_handl_radius(self):
            return self.handl_radius
        def Disable(self):
            self.slide.disable()
        def Enable(self):
            self.slide.enable()
        def Set_orintation(self,orint):
            self.slide.vertical = orint
        def Get_selected(self):
            return self.slide.selected
            
    class TextBoxs:
        def __init__(self,plane,
                            pos=[],
                            size=[],
                            font_size=30,
                            border_color=(0,0,0),
                            text_color = (0,0,0),
                            onSub=Function,radius = 1,
                            border_size=5
                            ):
            self.plane = plane
            self.pos = pos
            self.size = size
            self.width = size[0]
            self.height = size[1]
            self.font_size = font_size
            self.border_color = border_color
            self.text_color = text_color
            self.radius = radius
            self.border_size = border_size
            self.posx = self.pos[0]
            self.posy = self.pos[1]
            tb = TextBox(self.plane,
                            self.posx,self.posy,
                            self.width,self.height,
                            fontSize = self.font_size,
                            borderColour = self.border_color,
                            textColour = text_color,
                            onSubmit = onSub,
                            radius = self.radius,
                            borderThickness = self.border_size)
            self.tb = tb
        def Get_text(self):
            text = self.tb.getText()
            return text
        def Set_text(self,text=''):
            self.tb.setText(text)
        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)
        def Set_size(self,size=[]):
            self.width = size[0]
            self.height = size[1]
            self.tb.setWidth(size[0])
            self.tb.setHeight(size[1])
        def Set_posx(self,x):
            self.posx = x
            self.tb.setX(x)
        def Set_posy(self,y):
            self.posy = y
            self.tb.setY(y)
        def Set_pos(self,pos=[]):
            self.posy = pos[1]
            self.tb.setY(pos[1])
            self.posx = pos[0]
            self.tb.setX(pos[0])
        def Hide(self):
            self.tb.hide()
        def Show(self):
            self.tb.show()
        def Set_output_disable(self):
            self.tb.disable()
        def Set_output_enable(self):
            self.tb.enable()
        def Set_width(self,width):
            self.width = width
            self.tb.setWidth(width)
        def Set_height(self,height):
            self.height = height
            self.tb.setHeight = height
        def Get_height(self):
            return self.tb.getHeight()
        def Get_width(self):
            return self.tb.getWidth()
        def Get_pos(self):
            return self.pos
        def Get_posx(self):
            return self.posx
        def Get_posy(self):
            return self.posy
        def Get_size(self):
            return self.size
        def Get_font_size(self):
            return self.font_size
        def Get_border_color(self):
            return self.border_color
        def Get_text_color(self):
            return self.text_color
        def Get_radius(self):
            return self.radius
        def Get_border_size(self):
            return self.border_size    
        def Disable(self):
            self.tb.disable()
        def Enable(self):
            self.tb.enable()
        def Get_selected(self):
            return self.tb.selected
         
    class Buttons:
        def __init__(self,plane,
                            pos=[],
                            size=[],
                            text='',
                            text_color=(0,0,0),
                            font_size=20,
                            margin = 20,
                            no_activ_color = (10,10,10),
                            activ_color = (30,30,30),
                            pressed_color=(60,60,60),
                            radius=20,
                            functions=Function,
                            shadow_dist = 0,
                            shadow_color = (0,0,0)
                            ):
            self.plane = plane
            self.pos = pos
            self.size = size
            self.posx = self.pos[0]
            self.posy = self.pos[1]
            self.width = self.size[0]
            self.height = self.size[1]
            self.text = text
            self.font_size = font_size
            self.margin = margin
            self.no_activ_color = no_activ_color
            self.activ_color = activ_color
            self.pressed_color = pressed_color
            self.radius = radius
            self.text_color = text_color
            self.shadow_dist = shadow_dist
            self.shadow_color = shadow_color
            bt = Button(
                self.plane,
                self.posx,self.posy,
                self.width,self.height,
                text=self.text,
                fontSize = self.font_size,
                margin = self.margin,
                inactiveColour = self.no_activ_color,
                hoverColour = self.activ_color,
                pressedColour = self.pressed_color,
                radius = self.radius,
                onClick = functions,
                textColour = self.text_color,
                shadowColour = self.shadow_color,
                shadowDistance = self.shadow_dist
            )
            self.bt = bt
        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)
        def Set_posx(self,x):
            self.posx = x
            self.bt.setX(x)
        def Set_posy(self,y):
            self.posy = y
            self.bt.setY(y)
        def Set_width(self,width):
            self.width = width
            self.bt.setWidth(width)
        def Set_height(self,height):
            self.height = height
            self.bt.setHeight(height)
        def Set_size(self,size=[]):
            self.height = size[1]
            self.width = size[0]
            self.bt.setWidth(size[0])
            self.bt.setHeight(size[1])
        def Set_pos(self,pos = []):
            self.posx = pos[0]
            self.posy = pos[1]
            self.bt.setX(pos[0])
            self.bt.setY(pos[1])
        def Set_pressed_color(self,color):
            self.pressed_color = color
            self.bt.setPressedColour(color)
        def Set_activ_color(self,color):
            self.activ_color = color
            self.bt.setHoverColour(color)
        def Set_no_activ_color(self,color):
            self.no_activ_color = color
            self.bt.setInactiveColour(color)
        def Get_pos(self):
            return self.pos
        def Get_posx(self):
            return self.posx
        def Get_posy(self):
            return self.posy
        def Get_size(self):
            return self.size
        def Get_width(self):
            return self.width
        def Get_height(self):
            return self.height
        def Get_text(self):
            return self.text
        def Get_font_size(self):
            return self.font_size
        def Get_margin(self):
            return self.margin
        def Get_no_activ_color(self):
            return self.no_activ_color
        def Get_activ_color(self):
            return self.activ_color
        def Get_pressed_color(self):
            return self.pressed_color
        def Get_radius(self):
            return self.radius
        def Get_text_color(self):
            return self.text_color
        def Get_shadow_color(self):
            return self.shadow_color
        def Get_shadow_distance(self):
            return self.shadow_dist
        def Show(self):
            self.bt.show()
        def Hide(self):
            self.bt.hide()
        def Get_pressed(self):
            return self.bt.clicked
        def Sleep(self):
            self.bt.disable()
        def Stendup(self):
            self.bt.enable()
        def Disable(self):
            self.bt.disable()
        def Enable(self):
            self.bt.enable()

            
    class Toggles:
        def __init__(self,plane,
                            pos=[],
                            size=[],
                            startType = False,
                            oncolor = (141, 185, 244),
                            offcolor =(150, 150, 150),
                            handl_oncolor = (26, 115, 232),
                            handl_offcolor = (200, 200, 200),
                            radius = 20
                            ):
            self.plane = plane
            self.pos = pos
            self.posx = self.pos[0]
            self.posy = self.pos[1]
            self.size = size
            self.width = self.size[0]
            self.height = self.size[1]
            self.startType = startType
            self.oncolor = oncolor
            self.offcolor = offcolor
            self.handl_oncolor = handl_oncolor
            self.handl_offcolor = handl_offcolor
            self.radius = radius
            tg = Toggle(
                self.plane,
                self.posx,self.posy,
                self.width,self.height,
                startOn = self.startType,
                offColour = self.offcolor,
                onColour = self.oncolor,
                handleOnColour = self.handl_oncolor,
                handleOffColour = self.handl_offcolor,
                handleRadius = self.radius
            )
            self.tg = tg
        def Update(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame_widgets.update(events)
        def Set_pos(self,pos=[]):
            self.posx = pos[0]
            self.posy = pos[1]
            self.tg.setX(pos[0])
            self.tg.setY(pos[1])
        def Set_posx(self,x):
            self.posx = x
            self.tg.setX(x)
        def Set_posy(self,y):
            self.posy = y
            self.tg.setY(y)
        def Set_width(self,width):
            self.width = width
            self.tg.setWidth(width)
        def Set_height(self,height):
            self.height = height
            self.tg.setHeight(height)
        def Hide(self):
            self.tg.hide()
        def Show(self):
            self.tg.show()
        def Get_value(self):
            val = self.tg.getValue()
            return val
        def Get_height(self):
            return self.tg.getHeight()
        def Get_width(self):
            return self.tg.getWidth()
        def Get_size(self):
            return self.size
        def Get_pos(self):
            return self.pos
        def Get_posx(self):
            return self.posx
        def Get_posy(self):
            return self.posy
        def Get_start_Type(self):
            return self.startType
        def Get_oncolor(self):
            return self.oncolor
        def Get_offcolor(self):
            return self.offcolor
        def Get_handl_oncolor(self):
            return self.handl_oncolor
        def Get_handl_offcolor(self):
            return self.handl_offcolor
        def Get_radius(self):
            return self.radius
# 14 -- new !!
class Objectes_:
    def __init__(self,name='obj'):
        self.name = name
        self.pack = []
    def Add(self,obj,mass=False):
        if mass == True:
            self.pack.append(obj)
        else:
            if len(obj)>1:
                for i in range(len(obj)):
                    self.pack.append(obj[i])
            else:
                self.pack.append(obj)   
    def Del_min(self,index):
        self.pack.pop(index)
    def Del_max(self,a_index,b_index):
        del self.pack[a_index-1:b_index]
    def Get_name(self):
        return self.name
    def Set_name(self,name):
        self.name = name
    def Get_pack(self):
        return self.pack
        







































