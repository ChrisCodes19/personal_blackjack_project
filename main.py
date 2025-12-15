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

game_state = "player_turn"

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

# buttons for hit, stand, etc...
def draw_button(screen, rect, text, font):
    # outer button 
    pygame.draw.rect(screen, "white", rect, 0, border_radius=4)
    #inner colored area
    inner_rect = rect.inflate(-6, -6)
    pygame.draw.rect(screen, "green", inner_rect, border_radius=4)
    #render text
    surf = font.render(text, True, (0, 0, 0))
    text_width, text_height = surf.get_size()
    #center text
    text_x = rect.x + (rect.width - text_width) / 2
    text_y = rect.y + (rect.height - text_height) / 2
    screen.blit(surf, (text_x, text_y))

hit_button = pygame.Rect(100, 600, 120, 40)
stand_button = pygame.Rect(260, 600, 120, 40)

#Helper for hit logic
def hit_player():
    global game_state
    hit_card = random_card()
    player_hand.add_card(hit_card)
    if player_hand.total() > 21:
        game_state = "round_over"


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if hit_button.collidepoint(mx, my) and game_state == "player_turn":
                hit_player()
            if stand_button.collidepoint(mx, my) and game_state == "player_turn":
                game_state = "dealer_turn"

    screen.fill(dark_grey)

    #player
    draw_hand(screen, player_hand, y=450, font=font, hide_first=False)

    #dealer
    draw_hand(screen, dealer_hand, y=100, font=font, hide_first=True)

    #buttons
    draw_button(screen, hit_button, "Hit", font)
    draw_button(screen, stand_button, "Stand", font)

    pygame.display.flip()
    clock.tick(60)