import os
from pygame import mixer
import time
import random

# Coloque o caminho onde os áudios estão localizados abaixo:
CAMINHO_ARQUIVO = "C:\\Users\\Windows\\Desktop\\projeto-10"

lista_de_arquivos = os.listdir(CAMINHO_ARQUIVO)
lista_de_audios = []

if __name__ == "__main__":
    for arquivo in lista_de_arquivos:
        if ".wav" in arquivo:
            lista_de_audios.append(arquivo)

    while True:
        if len(lista_de_audios) == 0:
            print("Não existem áudios para serem executados.")
            break

        mixer.init()
        audio = random.choice(lista_de_audios) 
        lista_de_audios.remove(audio)
        print(f"O arquivo de áudio que está sendo executado é: {audio}")

        mixer.music.load(audio)
        mixer.music.play()

        while mixer.music.get_busy():
            time.sleep(0.1)
