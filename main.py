import pygame 
from sklearn.linear_model import LogisticRegression
import numpy as np

def draw_left(screen, pos, radius):
    pygame.draw.circle(screen, "red", pos, radius)
    pygame.display.update()

def draw_right(screen, pos, radius):
    pygame.draw.circle(screen, "blue", pos, radius)
    pygame.display.update()
    
def draw_new(screen, pos, radius, color):
    pygame.draw.circle(screen, color, pos, radius)
    pygame.display.update()

def generate_dataset(arr1, arr2):
    point = []
    target = []
    for p in range(len(arr1)):
        point.append(arr1[p])
        target.append(0)
        
    for p in range(len(arr2)):
        point.append(arr2[p])
        target.append(1)
    
    return np.array(point), np.array(target)

pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill("#FFFFFF")
pygame.display.update()

radius = 5

points_red = []

points_blue = []

learned = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            draw_left(screen, pos, radius)
            points_red.append(pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pos = event.pos
            draw_right(screen, pos, radius)
            points_blue.append(pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                X, y = generate_dataset(points_red, points_blue)
                clf = LogisticRegression(random_state=0).fit(X, y)
                print("Started")
                learned = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and learned == True:
            coords = event.pos
            pos = np.array([event.pos])
            print(pos)
            prediction = clf.predict(pos)
            if 1 in prediction:
                color = 'blue'
                draw_new(screen, coords, radius, color)
            else:
                color = 'red'
                draw_new(screen, coords, radius, color)
            
                