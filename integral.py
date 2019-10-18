import  pygame
class Integral:
    def __init__(self,screen,gameSet,stats):
        self.gameSet=gameSet
        self.screen=screen
        self.screen_rect=self.screen.get_rect()
        self.stats=stats
        self.text_color=(40,40,40)
        self.font=pygame.font.SysFont(None,50)
        self.prep_score()
        self.prep_final_score()
        self.prep_level()
    def prep_score(self):
        score_str="{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.gameSet.color)
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)


    def prep_final_score(self):

        final_score_str ="{:,}".format(self.stats.final_score)
        self.final_score_image = self.font.render(final_score_str, True, self.text_color, self.gameSet.color)
        self.final_score_rect = self.score_image.get_rect()
        self.final_score_rect.center = self.screen_rect.center
        self.final_score_rect.top = 20

    def show_final_score(self):
        self.screen.blit(self.final_score_image, self.final_score_rect)

    def prep_level(self):
        level_str = "{:,}".format(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.gameSet.color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom+20

    def level_show(self):
        self.screen.blit(self.level_image, self.level_rect)