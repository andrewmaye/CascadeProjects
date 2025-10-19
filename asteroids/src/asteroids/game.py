"""Main game module for the Asteroids game."""
import sys
import pygame

# Initialize pygame modules
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Game:
    """Main game class that manages the game loop and display."""

    def __init__(self):
        """Initialize the game window and set up the game."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Asteroids")
        self.clock = pygame.time.Clock()
        self.running = True
        self.background = BLACK

    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Update game state."""
        pass  # Will be implemented in future iterations

    def draw(self):
        """Draw the current game state."""
        self.screen.fill(self.background)
        pygame.display.flip()

    def run(self):
        """Run the main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game."""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
