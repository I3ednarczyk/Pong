import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {'paddle': (40,100), 'ball': (30,30)}
POS = {'player': (WINDOW_WIDTH - 50, WINDOW_HEIGHT / 2), 'opponent': (50, WINDOW_HEIGHT / 2)}
SPEED = {'player': 400, 'opponent': 300, 'ball': 550}
COLORS = {
    'paddle': '#eb7e02',
    'ball': '#db0000',
    'bg': '#3f9b0b',
    'bg detail': '#ffffff'
}