import pygame
import time
import random
import os

os.system('cls')
print( '#####################################################' )
print( '######         Seja Bem Vindo ao Jogo          ######' )
print( '###### Seu objetivo é nao deixar o gremio cair ######' )
print( '######     evite os simbolos da serie b!!      ######' )
print( '######   Ao chegar em 20 pontos você ganha!!   ######' )
print( '#####################################################' )
print('')

arquivo = open('historico.txt','r')
dados = arquivo.read()
arquivo.close()

print('Digite seu Nome:')
nome = input()
print('')

print('Digite seu Email:')
email = input()
print('') 

dados = dados +'#### Historico de jogadores ####\n'+ nome + '--->' + email + '\n'
arquivo = open("historico.txt","w")
arquivo.write(dados)
arquivo.close()
print('Historico de jogadores:')
print(dados)

time.sleep(5)

pygame.init()
largura = 1150
altura = 700
configTela = (largura, altura)
gameDisplay = pygame.display.set_mode(configTela)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
pygame.display.set_caption("Grêmio escapando da serie B")
icone = pygame.image.load("meujogo/serieb.png")
pygame.display.set_icon(icone)
gremio = pygame.image.load("meujogo/gremio.png")
larguraGremio = 110
fundo = pygame.image.load("meujogo/gremioarena.jpg")
letrab = pygame.image.load("meujogo/b2.png")
ganhemo = pygame.mixer.Sound("meujogo/inaa.mp3")
caiuSound = pygame.mixer.Sound("meujogo/segunda.mp3")
naocairSound = pygame.mixer.Sound("meujogo/naocair.mp3")
naocairSound.set_volume(0.2)

def mostraGremio(x, y):
    gameDisplay.blit(gremio, (x, y))
def mostrab(x, y):
    gameDisplay.blit(letrab, (x, y))
def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()
def escreverTela(texto):
    fonte = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(texto, fonte)
    TextRect.center = ((largura/2, altura/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game()
def escreverPlacar(contador):
    fonte = pygame.font.SysFont(None, 30)
    texto = fonte.render("pontos:"+str(contador), True, white)
    gameDisplay.blit(texto, (10, 10))
def dead():
    pygame.mixer.Sound.play(caiuSound)
    pygame.mixer.music.stop()
    escreverTela("Gremio caiu!")
def ganhou():
    pygame.mixer.Sound.play(ganhemo)
    pygame.mixer.music.stop()
    escreverTela('Gremio Não caiu!')
def game():
    gremioPosicaoX = largura*0.42
    gremioPosicaoY = altura*0.8
    movimentoX = 0
    velocidade = 20
    seriebAltura = 150
    seriebLargura = 90
    seriebVelocidade = 2
    seriebX = random.randrange(0, largura)
    seriebY = -200
    pontos = 0
    pygame.mixer.Sound.play(naocairSound)
    while True:
        acoes = pygame.event.get()  
        for acao in acoes:
            if acao.type == pygame.QUIT:
                pygame.quit()
                quit()
            if acao.type == pygame.KEYDOWN:
                if acao.key == pygame.K_LEFT:
                    movimentoX = velocidade*-1
                elif acao.key == pygame.K_RIGHT:
                    movimentoX = velocidade
            if acao.type == pygame.KEYUP:
                movimentoX = 0

        gameDisplay.fill(white)
        gameDisplay.blit(fundo, (0, 0))
        escreverPlacar(pontos)
        seriebY = seriebY + seriebVelocidade
        mostrab(seriebX, seriebY)
        if seriebY > altura:
            seriebY = -200
            seriebX = random.randrange(0, largura)
            pontos = pontos+1
            seriebVelocidade += 1.5
            pygame.mixer.Sound.play(naocairSound)
        gremioPosicaoX += movimentoX
        if gremioPosicaoX < 0:
            gremioPosicaoX = 0
        elif gremioPosicaoX > largura-larguraGremio:
            gremioPosicaoX = largura-larguraGremio
        if gremioPosicaoY < seriebY + seriebAltura:
            if gremioPosicaoX < seriebX and gremioPosicaoX+larguraGremio > seriebX or seriebX+seriebLargura > gremioPosicaoX and seriebX+seriebLargura < gremioPosicaoX+larguraGremio:
                dead()
        if pontos == 21:
            ganhou()       
        mostraGremio(gremioPosicaoX, gremioPosicaoY)
        pygame.display.update()
        clock.tick(60) 
game()
