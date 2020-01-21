import sys
import pygame
from consts import RADIUS_STEP, X_MAX, Y_MAX, PLAYER_COLOR, MOVE_RIGHT,MOVE_LEFT,MOVE_UP,MOVE_DOWN


class Game:

    def __init__(self, player, memento_caretaker):
        self.memento_caretaker = memento_caretaker
        self.player = player
        pygame.init()
        self.screen = pygame.display.set_mode((X_MAX, Y_MAX))

    def __check_quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def play(self):

        while True:
            event = pygame.event.wait()
            self.__check_quit(event)

            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move(MOVE_LEFT)
            elif keys[pygame.K_RIGHT]:
                self.player.move(MOVE_RIGHT)
            elif keys[pygame.K_UP]:
                self.player.move(MOVE_UP)
            elif keys[pygame.K_DOWN]:
                self.player.move(MOVE_DOWN)

            if keys[pygame.K_s]:
                self.memento_caretaker.makeBackup()
            if keys[pygame.K_r]:
                self.memento_caretaker.rollback()

            self.screen.fill((0, 0, 0))
            self.draw_player()
            pygame.display.update()
            pygame.event.clear()

    def draw_player(self):
        x, y = self.player.getPosition()
        x *= RADIUS_STEP * 2
        y *= RADIUS_STEP * 2
        pygame.draw.circle(self.screen, PLAYER_COLOR, (x, y), RADIUS_STEP, 0)
