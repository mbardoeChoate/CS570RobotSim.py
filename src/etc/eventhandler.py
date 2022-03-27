import pygame


class EventHandler:

    def __init__(self, main):
        self.main = main

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.main.running = False
