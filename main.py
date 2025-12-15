import pygame
from  cards import Card, random_card
from hand import Hand
from constants import *


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dark_grey = (30, 30, 30)

font = pygame.font.SysFont("arial", 24)

# Main game functions
def draw_card_back(screen, x, y):
    pygame.draw.rect(screen, CARD_BORDER, (x, y, CARD_WIDTH, CARD_HEIGHT), border_radius=6)
    pygame.draw.rect(screen, (150, 0, 0), (x+3, y+3, CARD_WIDTH-6, CARD_HEIGHT-6), border_radius=4)

def draw_card_face(screen, x, y, card, font):
    pygame.draw.rect(screen, CARD_BORDER, (x, y, CARD_WIDTH, CARD_HEIGHT), border_radius=6)
    pygame.draw.rect(screen, CARD_WHITE, (x+3, y+3, CARD_WIDTH-6, CARD_HEIGHT-6), border_radius=4)

    text = card.name[:3].upper()
    surf = font.render(text, True, (0, 0, 0))
    screen.blit(surf, (x + 8, y + 8))

def draw_hand(screen, hand, y, font, hide_first=False, center_x = None):
    num_cards = len(list(hand))
    if num_cards == 0:
        return 
    total_width = num_cards * CARD_WIDTH + (num_cards - 1) * CARD_SPACING

    if center_x is None:
        center_x = screen.get_width() // 2
    
    start_x = center_x - total_width // 2

    x = start_x
    for i, card in enumerate(hand):
        if hide_first and i == 0:
            draw_card_back(screen, x, y)
        else:
            draw_card_face(screen, x, y, card, font)
        x += CARD_WIDTH + CARD_SPACING

player_hand = Hand()
dealer_hand = Hand()

#quick test
for _ in range(2):
    player_hand.add_card(random_card())
    dealer_hand.add_card(random_card())


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(dark_grey)

    #player
    draw_hand(screen, player_hand, y=450, font=font, hide_first=False)

    #dealer
    draw_hand(screen, dealer_hand, y=100, font=font, hide_first=True)

    pygame.display.flip()
    clock.tick(60)