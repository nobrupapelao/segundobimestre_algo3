import time
ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia ):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo =novo_tempo
        potencia =nova_potencia
        print(f'microondas ligado por {tempo} segundos na potencia {potencia}')
        iniciar_cronometro(tempo)
        desligar() #delisgar automatico

    else:
        print('o microondas ja esta ligado')

def desligar():
    global ligado
    if ligado:
        ligado = False
        print('microondas esta desligado')
    else:
         print('o microondas esta desligado')

def status():
    if ligado:
       print(f'tempo: {tempo} segundos s/n potencia {potencia}')
    else:
        print('o microondas esta desligado')

def iniciar_cronometro(segundos):
    while segundos >0 :
        print(f'tempo restante : {segundos} segundos', end='\r')

        time.sleep(1)
        segundos -= 1
    print(' \n tempo esgotado')

def pipoca() :
    ligar(30,100)

pipoca()