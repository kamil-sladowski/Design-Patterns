from Player import Player
from Caretaker import Caretaker
from Game import Game

if __name__ == '__main__':
    player = Player()
    caretaker = Caretaker(player)
    game = Game(player, caretaker)
    game.play()
