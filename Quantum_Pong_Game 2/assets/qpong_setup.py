import pygame
from pygame.locals import *

class SetupScreen:
    def __init__(self):
        pygame.init()

        # Set up Pygame window for setup
        self.screen = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Quantum Pong Setup")

        self.font = pygame.font.Font(None, 36)
        self.clock = pygame.time.Clock()

        self.qubits = 3  # Default number of qubits

    def setup_screen(self):
        while True:
            self.screen.fill((255, 255, 255))

            # Display instructions and current number of qubits
            text = self.font.render("Use UP/DOWN arrows to set qubits", True, (0, 0, 0))
            self.screen.blit(text, (50, 50))

            text = self.font.render(f"Number of Qubits: {self.qubits}", True, (0, 0, 0))
            self.screen.blit(text, (50, 100))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.qubits += 1
                    elif event.key == K_DOWN and self.qubits > 1:
                        self.qubits -= 1
                    elif event.key == K_RETURN:
                        return self.qubits

            self.clock.tick(30)

if __name__ == "__main__":
    selected_qubits = SetupScreen().setup_screen()
    print(f"Selected Qubits: {selected_qubits}")
