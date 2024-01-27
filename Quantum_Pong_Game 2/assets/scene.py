import pygame
from . import globals

class Scene:

    def __init__(self):
        super().__init__()
        Scene = Scene.start()
        self.begin = False
        self.restart = False
        self.qubit_num = 3

    def start(self, screen, ball):
        screen.fill(globals.BLACK)

        gameover_text = "Qpong"
        text = self.font.gameover_font.render(gameover_text, 1, globals.WHITE)
        text_pos = text.get_rect(center=(globals.WINDOW_WIDTH / 2, globals.WIDTH_UNIT * 15))
        screen.blit(text, text_pos)

        gameover_text = "Enter Number of Qubits: "
        text = self.font.replay_font.render(gameover_text, 5, globals.WHITE)
        text_pos = text.get_rect(center=(globals.WINDOW_WIDTH / 2, globals.WIDTH_UNIT * 30))
        screen.blit(text, text_pos)