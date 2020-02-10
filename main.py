import pygame
from random import randrange

try:
    pygame.init()
except:
    print('Problema ao iniciar o módulo pygame')

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

largura = 320
altura = 280
tamanho = 10
placar = 40

recorde = 0

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')

#converter para ogg fica melhor
#audio_fundo = pygame.mixer.Sound('fundo.mp3')
#pygame.mixer.music.stop()

#pygame.mixer.music.load("fundo.mp3")


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, azul, [XY[0], XY[1], tamanho, tamanho])

def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, vermelho, [maca_x, maca_y, tamanho, tamanho])


def menu():
    tipo = 0
    sair = True

    while sair:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    tipo = 1
                    sair = False
        
                if event.key == pygame.K_l:
                    tipo = 2
                    sair = False
        
        fundo.fill(branco)

        texto('Snake Game', preto, 50, 50, 60)

        pygame.draw.rect(fundo, preto, [45, 120, 180, 27]) #x=45,y=120, 180=largura, 27=altura
        texto('Modo Clássico(A)', branco, 30, 50, 125)
        
        pygame.draw.rect(fundo, preto, [45, 160, 145, 27])
        texto('Modo Livre(L)', branco, 30, 50, 165)
        
        pygame.display.update()
    return tipo


def jogo(tipo):
    sair = True
    fimDeJogo = False
    
    pos_x = randrange(0, largura-tamanho ,10)
    pos_y = randrange(0, altura-tamanho-placar ,10)

    maca_x = randrange(0, largura-tamanho, 10)
    maca_y = randrange(0, altura-tamanho-placar, 10)

    velocidade_x = 0
    velocidade_y = 0
    
    CobraXY = []
    CobraComp = 1

    pontuacao = 0

    #pygame.mixer.music.play()

    while sair:
        while fimDeJogo:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sair = False
                    fimDeJogo = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimDeJogo = False
                        
                        pos_x = randrange(0, largura-tamanho ,10)
                        pos_y = randrange(0, altura-tamanho-placar ,10)

                        maca_x = randrange(0, largura-tamanho, 10)
                        maca_y = randrange(0, altura-tamanho-placar, 10)

                        velocidade_x = 0
                        velocidade_y = 0
                        
                        CobraXY = []
                        CobraComp = 1

                        pontuacao = 0

                    elif event.key == pygame.K_s:
                        sair = False
                        fimDeJogo = False
                    
                    elif event.key == pygame.K_m:
                        sair = False
                        fimDeJogo = False
                        main()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        sair = True
                        fimDeJogo = False
                        
                        pos_x = randrange(0, largura-tamanho ,10)
                        pos_y = randrange(0, altura-tamanho-placar ,10)

                        maca_x = randrange(0, largura-tamanho, 10)
                        maca_y = randrange(0, altura-tamanho-placar, 10)

                        velocidade_x = 0
                        velocidade_y = 0
                        
                        CobraXY = []
                        CobraComp = 1

                        pontuacao = 0
                    
                    elif x > 190 and y > 120 and x < 265 and y < 147:
                        sair = False
                        fimDeJogo = False

            #pygame.mixer.music.stop()
            fundo.fill(branco)
            
            texto('Fim de Jogo', vermelho, 50, 65, 30)
            texto(f'Pontuação Final: {pontuacao}', preto, 30, 70, 80)
            
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            texto('Continuar(C)', branco, 30, 50, 125)
            
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto('Sair(S)', branco, 30, 195, 125)

            pygame.draw.rect(fundo, preto, [20, 150, 282, 27])
            texto('Voltar ao Menu Principal(M)', branco, 30, 25, 155)
            
            pygame.display.update()
        

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_y = -tamanho
                    velocidade_x = 0
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_y = tamanho
                    velocidade_x = 0
        if sair:
            fundo.fill(preto)
            
            pos_x+=velocidade_x
            pos_y+=velocidade_y

            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura-tamanho, 10)
                maca_y = randrange(0, altura-tamanho-placar, 10)
                CobraComp+=1
                pontuacao+=1
            
            if tipo == 1:
                if pos_x + tamanho > largura:
                    fimDeJogo = True
                if pos_x < 0:
                    fimDeJogo = True
                if pos_y + tamanho > altura - placar:
                    fimDeJogo = True
                if pos_y < 0:
                    fimDeJogo = True
            
            elif tipo == 2:
                if pos_x + tamanho > largura:
                    pos_x = 0
                if pos_x < 0:
                    pos_x = largura-tamanho
                if pos_y + tamanho > altura - placar:
                    pos_y = 0
                if pos_y < 0:
                    pos_y = altura-tamanho - placar

            CobraInicio = []
            
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)

            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimDeJogo = True
            
            
            pygame.draw.rect(fundo, branco, [0, altura-placar,largura, placar])
            texto(f'Pontuação: {pontuacao}', preto, 30, 10, altura-placar+10)

            cobra(CobraXY)
            maca(maca_x, maca_y)
            
            pygame.display.update()
            relogio.tick(15)
        


def main():
    tipo = menu()
    
    if tipo != 0:
        jogo(tipo)
    
    pygame.quit()

main()