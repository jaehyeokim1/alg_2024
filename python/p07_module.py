import math
import pygame as pg

# pt1과 pt2의 좌표를 변경
pt1, pt2 = [ -200, -150 ], [ 200, 250 ]  # 좌표를 변경하여 다른 위치의 점을 사용
distance = math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print(f'두 점 {pt1} 과 {pt2} 사이의 거리는 {distance:.2f} 이다')

# atan2로 각도 계산
angle_radian = math.atan2((pt2[1]-pt1[1]), (pt2[0]-pt1[0]))
angle_degree = 180 * angle_radian / math.pi
print(f'두 점 사이의 선이 만드는 각도는 Radian 으로는 {angle_radian:.2f}, Degree 로는 {angle_degree:.2f}° 이다')

# 회전 후 좌표 계산, 각도 배수를 1.5로 변경
dx = distance * math.cos(1.5 * angle_radian)  # 각도를 1.5배로 회전
dy = distance * math.sin(1.5 * angle_radian)
pt3 = [pt1[0] + dx, pt1[1] + dy]
print(f'pt1 을 기준으로 {angle_degree:.2f}° 만큼 더 회전한 점은 [{pt3[0]:.2f}, {pt3[1]:.2f}] 이다')

# pygame 화면 설정 및 색상 변경
RED, GREEN, BLUE = (255,0,0), (0,255,0), (0,0,255)  # 더 밝은 색상으로 변경
BLACK, WHITE = (0,0,0), (200,200,200)  # 흰색을 약간 어둡게
pg.init()
screen = pg.display.set_mode([1200, 1200])  # 화면 크기를 1200x1200으로 변경
font = pg.font.SysFont("arial", 16)
pg.display.set_caption('Test')
screen.fill(WHITE)

def m2s(pt):  # 수학 좌표계를 pygame 좌표계로 변경
    return [pt[0] + 600, 600 - pt[1]]  # 중심점이 600,600으로 변경됨

def d_line(pt1, pt2, color=BLACK):
    pg.draw.line(screen, color, m2s(pt1), m2s(pt2))

def d_pt(pt, color=BLACK, name=None):
    xy = m2s(pt)
    pg.draw.circle(screen, color, xy, 5, 1)
    if name != None:
        img = font.render(name, True, color)
        screen.blit(img, xy)

# x축과 y축을 그려준다
d_line([-600, 0], [600, 0])  # 축 길이 조정
d_line([0, -600], [0, 600])

# 세 개의 점을 그려 준다
d_pt(pt1, RED, 'pt1')
d_pt(pt2, GREEN, 'pt2')
d_pt(pt3, BLUE, 'pt3')

# Line 세 개를 그려서 각도가 보이도록 해 본다
d_line(pt1, [pt1[0] + distance, pt1[1]], (251,180,174))
d_line(pt1, pt2, (204,235,197))
d_line(pt1, pt3, (179,205,227))

pg.display.flip()

loop = True
while loop:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            loop = False
            break
        elif e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            pg.quit()
            loop = False
            break

pg.quit()
