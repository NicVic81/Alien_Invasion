import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize pygame, settings, and screen object."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        # Redraw the screen during each pass through the loop and display the most recent version.
        gf.update_screen(ai_settings, screen, ship)


run_game()
