from . import globals, resources
import pygame

def draw_statevector_grid(screen):
    font = resources.Font()
    basis_states = [
        '|00>',
        '|01>',
        '|10>',
        '|11>'
    ]
    statevector_height = int(round(globals.FIELD_HEIGHT / len(basis_states))) #8 basis states

    for i in range(len(basis_states)):
        text = font.vector_font.render(basis_states[i], 1, globals.WHITE)
        screen.blit(text, (globals.WINDOW_WIDTH - text.get_width(),
                            i*statevector_height + text.get_height()))

def draw_score(screen, classical_score, quantum_score):
    font = resources.Font()

    text = font.player_font.render("Classical Computer", 1, globals.GRAY)
    text_pos = text.get_rect(center = (globals.WINDOW_WIDTH*0.3, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(classical_score), 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.3, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

    text = font.player_font.render("Quantum Computer", 1, globals.GRAY)
    text_pos = text.get_rect(center = (globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*2))
    screen.blit(text, text_pos)

    text = font.score_font.render(str(quantum_score), 1, globals.GRAY)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH*0.7, globals.WIDTH_UNIT*8))
    screen.blit(text, text_pos)

def draw_dashed_line(screen):
    for i in range(10, globals.FIELD_HEIGHT, 2*globals.WIDTH_UNIT):
        pygame.draw.rect(
            screen,
            globals.GRAY,
            (globals.WINDOW_WIDTH // 2 - 5, i, 0.5 * globals.WIDTH_UNIT, globals.WIDTH_UNIT),
            0,
        )

def draw_lose_scene(screen):
    font = resources.Font()

    
    gameover_text = "Game Over"
    text = font.gameover_font.render(gameover_text, 1, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*10))
    screen.blit(text, text_pos)

    gameover_text = "Classical computer"
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*22))
    screen.blit(text, text_pos)

    gameover_text = "still rules the world"
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*27))
    screen.blit(text, text_pos)

def draw_win_scene(screen):
    font = resources.Font()

    gameover_text = "Congratulations!"
    text = font.gameover_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*10))
    screen.blit(text, text_pos)

    gameover_text = "You demonstrated quantum advantage"
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*22))
    screen.blit(text, text_pos)

    gameover_text = "for the first time in human history!"
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*27))
    screen.blit(text, text_pos)