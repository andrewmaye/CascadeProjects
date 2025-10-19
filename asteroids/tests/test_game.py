"""Tests for the asteroids game."""
import pytest
import pygame
from unittest.mock import patch, MagicMock

# Mock pygame modules to prevent display initialization during tests
pygame.display = MagicMock()
pygame.init = MagicMock(return_value=None)
pygame.time = MagicMock()
pygame.time.Clock = MagicMock()


def test_game_initialization():
    """Test that the game initializes correctly."""
    from asteroids.game import Game, SCREEN_WIDTH, SCREEN_HEIGHT
    
    # Create a mock for the screen
    mock_screen = MagicMock()
    mock_clock = MagicMock()
    
    # Set up the mocks
    pygame.display.set_mode.return_value = mock_screen
    pygame.time.Clock.return_value = mock_clock
    
    # Create a game instance
    game = Game()
    
    # Verify pygame.display.set_mode was called with the correct arguments
    pygame.display.set_mode.assert_called_once_with((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Verify screen and other attributes
    assert game.screen == mock_screen
    assert game.clock == mock_clock
    assert game.running is True
    assert game.background == (0, 0, 0)  # BLACK


def test_game_quit_event():
    """Test that the game can handle quit events."""
    from asteroids.game import Game
    
    with patch('pygame.event.get') as mock_event_get:
        # Mock a QUIT event
        mock_event = MagicMock()
        mock_event.type = pygame.QUIT
        mock_event_get.return_value = [mock_event]
        
        game = Game()
        game.handle_events()
        
        # The game should stop running after QUIT event
        assert game.running is False


def test_escape_key():
    """Test that the ESC key quits the game."""
    from asteroids.game import Game
    
    with patch('pygame.event.get') as mock_event_get:
        # Mock a KEYDOWN event for ESC key
        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_ESCAPE
        mock_event_get.return_value = [mock_event]
        
        game = Game()
        game.handle_events()
        
        # The game should stop running after ESC key is pressed
        assert game.running is False
