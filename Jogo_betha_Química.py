import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Definições de tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Tabuleiro Químico")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Variáveis do jogo
position = 0
questions = [
    ("Qual é o símbolo químico do Hidrogênio?", "H"),
    ("Qual é o símbolo químico do Oxigênio?", "O"),
    ("Qual é o símbolo químico do Carbono?", "C"),
    ("Qual é o símbolo químico do Nitrogênio?", "N"),
    ("Qual é o símbolo químico do Ouro?", "Au"),
    ("Qual é o símbolo químico do Ferro?", "Fe"),
    ("Qual é o símbolo químico do Cálcio?", "Ca"),
    ("Qual é o símbolo químico do Potássio?", "K"),
    ("Qual é o símbolo químico do Enxofre?", "S"),
    ("Qual é o símbolo químico do Mercúrio?", "Hg"),
]

def draw_board():
    screen.fill(WHITE)
    for i in range(10):
        pygame.draw.rect(screen, BLACK, (50 + (i * 70), 300, 60, 60), 1)
        text = font.render(str(i + 1), True, BLACK)
        screen.blit(text, (50 + (i * 70) + 20, 320))
        
    pygame.draw.circle(screen, GREEN, (50 + (position * 70) + 30, 350), 10)

def ask_question():
    question, answer = random.choice(questions)
    return question, answer

def main():
    global position
    while True:
        draw_board()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                question, answer = ask_question()
                print(question)  # Para teste, mostre a pergunta no console
                user_answer = input("Sua resposta: ")
                if user_answer.strip().upper() == answer:
                    position += 1
                    if position >= 10:
                        print("Você venceu!")
                        pygame.quit()
                        sys.exit()
                # Se errar, a posição permanece a mesma

if __name__ == "__main__":
    main()

