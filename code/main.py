from settings import *
from sprites import *
import pygame
import json
import asyncio
import requests

class Game():
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites))
        self.ball = Ball(self.all_sprites, self.paddle_sprites, self.update_score)
        Opponent((self.all_sprites, self.paddle_sprites), self.ball)

        pygame.font.init()
        self.score = {'player': 0, 'opponent': 0}
        self.font = pygame.font.Font(None, 160)

    def display_score(self):
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_surf, player_rect)

        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center=(WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_surf, opponent_rect)

        pygame.draw.line(self.display_surface, COLORS['bg detail'], (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 10)

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    async def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                    try:
                        # Replace with your Firebase URL
                        firebase_url = ""
                        data = {
                            "opponent": self.score['player'],
                            "player": self.score['opponent'],

                        }
                        response = requests.put(firebase_url, json=data)
                        if response.status_code == 200:
                            print("Score successfully sent to Firebase.")
                        else:
                            print(f"Failed to send score: {response.status_code}, {response.text}")
                    except Exception as e:
                        print("Could not send score to Firebase:", e)

            # Update and draw
            self.all_sprites.update(dt)
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

            # Pygbag: yield control to browser
            await asyncio.sleep(0)


async def main():
    pygame.init()
    game = Game()
    await game.run()

asyncio.run(main())
