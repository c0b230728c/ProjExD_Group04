import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Score:
    """
    正解の工科トンを選択した場合スコアを加算するクラス
    スコアの色が時間経過とともに変わる
    """
    def __init__(self):
        self.font = pg.font.Font(None, 50)
        self.color = pg.Color(0, 0, 255)
        self.value = 0
        self.image = self.font.render(f"Score: {self.value}", 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = 10, 850  # 左下に位置するように調整

    def update(self, screen: pg.Surface, time):
        # 色相を時間経過に応じて変化させる
        hue = (time % 360) / 360  # 0から1の範囲にする
        self.color.hsva = (int(hue * 360), 100, 100, 100)  # 色相を変更
        self.image = self.font.render(f"Score: {self.value}", True, self.color)
        self.rect = self.image.get_rect(topleft=(10, 850))
        screen.blit(self.image, self.rect)

    def add_points(self, points):
        self.value += points

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    Fscreen = pg.transform.flip(bg_img,True,False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img,10,1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    x=0
    y=0
    score = Score()

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        
        # スコアを時間経過に応じて虹色に変化させる
        score.update(screen, tmr)
        
        pg.display.update()
        clock.tick(60)
        tmr += 1  # 
        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img,kk_rct)     
        score.update(screen,tmr)
        pg.display.update()
        clock.tick(200)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()