import os
from re import S
import sys
from PySimpleGUI.PySimpleGUI import Exit, Save, Text
import pytesseract
from PIL import Image
import PySimpleGUI as sg
import pathlib
import pyttsx3
from os import system, name
import glob
from pyttsx3 import engine
from gtts import gTTS, lang #langs ler arquivo
import speech_recognition as sr #speech recognition biblioteca de voz para texto
from playsound import playsound #Musica
import darkdetect #detectar modo escuro
import docx2txt # para arquivo docx
import PyPDF2   # para pdf
from inspect import Traceback
from time import sleep
import pyglet
#import matplotlib.pyplot as plt 



file = None
#filepath = 'pequeno.txt'
class ConversorTexto:
    def __init__(self):
        file_types = [("Todos arquivos", "*.*")] # busca qualquer tipo de arquivo no FileBrowse
        fonte = 20 # tamanho da fonte
        fonte2 = 15 # dos botões
        img2 = None
        layout = [
       
            [sg.Text('dependendo do processamento de seu PC é do tamanho do arquivo de imagem pode demora um pouco.')],
            [sg.Text('se você quer ficar com o arquivo renomei ele obs: pode ser que tenha algusn erros pois depende de como esta a imagem ')],
            [sg.Text('deseja criar um arquivo de Texto.txt sera salvo no seu PC com nome arquivotxt2.txt ',font=fonte,size=(85,1)),sg.Button('Criar',key='sim_1',font=fonte2,size=(5,1))],
            [sg.Button('CarregaImage.png',key='imgq'),sg.Button('Ler Arquivo_OffLine',key='-3-',font=fonte),sg.Button('Stop',key= 'stop')],
            [sg.Output(size=(100,5)),sg.Button('Busca Arquivo',key='-1-',font=fonte),sg.Text('Busque arquivo p/exibir',font=9),sg.Button('salva',key='-2-')],
            [sg.Text('Digite o arquivo de Imagem sem aspas:',font=fonte,size=(35,1)),sg.Input(key='_arquivo_',font=fonte,size=(25,1)),sg.Button('ENTER',key='enter')],
            [sg.Text('> New file <', font=('Consolas', 10), size=(40, 1), key='_INFO_')], # salvar arquivo e updte de valores e 40 linha horizontal da barra do pequeno menu
            [sg.Multiline(font=('Consolas', 12), size=(65, 10), key='_BODY_')], # 65 horizontal da janela inferior e 10 vertical Janelinha Multiline: Caixa de texto grande: listagem de caixa de texto 
            #[sg.Button('Limpar Terminal', key='-4-'),sg.Input(size=(25, 1), key='-6-'),sg.Button('ler arquivo2',key='-5-'),sg.FileBrowse(file_types=file_types, key= 'file_browse')],   # para buscara arquivo  sg.FileBrowse    precisou de um Input antes   
            [sg.Text('Selecione um arquivo para começar!')],
            [sg.Text(size=(23,1), key='arquivo_selecionado'),sg.Button('limpar console', key= '-4-')],
            [sg.Button('Gravar', key='grava'),sg.Text('ler selecionado'),sg.Button('Ler Arquivos',key='abri_arq'),sg.Input(size=(25, 1), key="-FILE-"),sg.FileBrowse(file_types=file_types, key= 'file_browse'),sg.Button('Ler arquivo_Online', key='ler_arquivo'),sg.Text('ler arquivotxt2.txt')]
            
            ]

        # contrução da janela 
        #self.janela = sg.Window('Converso de Imagem para Texto de Alfredo ', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
        self.janela = sg.Window('Conversor de imagem em TEXTO ALF1', layout,resizable=True,return_keyboard_events=True)
    
    # para reseta arquivo 
    def new_file(self):
        '''Reset body and info bar, and clear filename variable'''
        self.janela['_BODY_'].update(value='')
        self.janela['_INFO_'].update(value='> New File <')
        file = None
        return file
    
    # As funções ficam abaixo da criação da janela
    # Função para abri arquivo    
    def open_file(self):
        '''Open file and update the infobar'''
        filename = sg.popup_get_file('Open', no_window=True)
        if filename:
            file = pathlib.Path(filename)
            self.janela['_BODY_'].update(value=file.read_text())
            self.janela['_INFO_'].update(value=file.absolute())
        return file
    
    # Função salvar arquivo
    def save_file_as(self):
        '''Save new file or save existing file with another name'''
        filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
        if filename:
            file = pathlib.Path(filename)
            file.write_text(self.values.get('_BODY_'))
            self.janela['_INFO_'].update(value=file.absolute())
            return file
    
    
    def entroducao(self):
        engine.say('Bem vindo alfredo a programação com python')
        # esperando o texto termina para poder roda o restante do codigo
        engine.runAndWait()

    def limpar_terminal(self):
        if name == 'nt':
            system('cls')
        else:
            system('clear') 
    
    def linguagem(self):  # use para trocar a linguagem no futuro 
        
        # procura uma forma de deixa o texto em portuguễs por padrão
        engine = pyttsx3.init()
        engine.setProperty('rate', 50) #90 ou 85
        engine.setProperty('voice', 'brazil-mbrola-1') 
    # teste
    def speak(text):
        tts = gTTS(text = text, lang = 'pt-br', slow= False)
        filename = 'audio.mp3'
        tts.save(filename)
        playsound(filename)
        os.remove(filename)    
    
    
    
    def faladorOffLine(self):
        # usou uma compressão de lista buscando arquivos
        lista_arquivo = [f for f in glob.glob("*.txt")]
        while True:
            engine = pyttsx3.init()
            engine.setProperty('rate', 78) #90
            engine.setProperty('voice', 'brazil-mbrola-1') 
            print(lista_arquivo)

            self.linguagem()

            arquivo_selecao = 'arquivotxt2.txt'

            with open((arquivo_selecao), 'r') as arquivo:
                # variavel texto recebe o arquivo aqui
                texto = arquivo.read()
                print(texto)
                self.linguagem()
                engine.say(texto)
                engine.runAndWait()
                self.limpar_terminal()
             
          
                print('Você pode muda o nome desse arquivo clicando com o botão direito do mouse nele para salva em seu PC de outro nome a ele não esquesa de colocar no final a extenção "txt", O Narrador\ so vai ler o arquivo que tenha o nome arquivotxt2.txt se você quer reler um arquivo basta renomealo para arquivotxt2.txt lembrando que tem que ser um aquivo de texto' )
        
            break
    def falador_Online(self):
            arq = open("arquivotxt2.txt") # nome do arqui
            linha = arq.read()  # carregamento do arquivo em uma variavel

            filename = linha
            tts = gTTS(filename, lang='pt-BR')
            filename = '/tmp/temp.mp3'
            tts.save(filename)
            

            music = pyglet.media.load(filename, streaming=False)
            music.play()

            sleep(music.duration) #prevent from killing para não remover durante a duraçõa da naração
            os.remove(filename) #remove temperory file 
    
    # criando arquivo de texto
    def criando_arquivoDtexto(self):
            # carregamento da imagem
            img = Image.open('paraler.png')

            # colocou a img numa varial é transformal de imagem para string 
            texto = pytesseract.image_to_string(img)
            with open("arquivotxt2.txt", "w") as txtfile:
                print("String Variable: {}".format(texto), file=txtfile)
            print('arquivo criado com exito! com o nome arquivotxt2.txt você pode busca ele para se exibido')       

    # vendo sem salva o arquivo
    def soexibindo(self):
        # carregamento da imagem
        img = Image.open('paraler.png')

        # colocou a img numa varial é transformal de imagem para string 
        texto = pytesseract.image_to_string(img)
        print(texto) 
    def removendo(self):
        #removendo o arquivo     
        os.remove("arquivotxt2.txt") 
        print('O arquivotxt2 foi EXECLUIDO')
    
    # grava o texto em mp3
    def gravando(self):
        arq = open("arquivotxt2.txt") # nome do arqui
        linha = arq.read()  # carregamento do arquivo em uma variavel
        tts = gTTS(text = linha, lang = 'pt-br', slow= False)
        #filename = 'audio.mp3'
        tts.save("linha.mp3") #gravando
        print('GRAVADO COM SUCESSO !')
    
    # carrga a IMAGEN selecionada
    def exibindoImagem(self):
        arquivo_selecao= str(self.values['_arquivo_'])#.lower()
        #arquivo_selecao = input('digite o nome do arquivo:')
        with Image.open((arquivo_selecao), 'r') as arquivo:#r
            arquivo.show()


    def inicial(self):
        
        while True:
      
           # extraindo dados
            #self.button, self.values = self.janela.Read()
            self.event, self.values = self.janela.Read()
            if self.event is None:
                break
            if self.event == '\r':
                elem = self.janela.FindElementWithFocus()
                if elem is not None:
                    elem.Click()

            if self.janela and self.values == sg.WINDOW_CLOSED:
                break

            elif self.event == '-1-':
                self.open_file()

            elif self.event == '-2-':
                self.save_file_as()
            # processo offline
            elif self.event == '-3-':
                self.faladorOffLine() 
            elif self.event == '-4-':
                self.limpar_terminal()
            elif self.event == 'ler_arquivo':
               self.falador_Online()
            elif self.event == 'sim_1':
                self.criando_arquivoDtexto()
            elif self.event == 'sim_2':
                self.soexibindo()
            elif self.event == 'sim_3':
                self.removendo()
            elif self.event == 'grava':
                self.gravando()
            # celecionado arqui txt
            if self.janela and self.event == 'abri_arq':
                filepath = self.values['-FILE-']
                nome_arquivo = os.path.basename(filepath)
                #abri o arquivo é 'como' text_to_read txt recebe text_to_read leitura vai abri o que esta dentro do arquivo
                with open(nome_arquivo) as text_to_read:
                    txt = text_to_read.read()
                filename = txt
                tts = gTTS(filename, lang='pt-BR')
                filename = '/tmp/temp.mp3'
                tts.save(filename)
                music = pyglet.media.load(filename, streaming=False)
                music.play()

                sleep(music.duration) #prevent from killing para não remover durante a duraçõa da naração
                os.remove(filename) #remove temperory file  
            # selecionando imagem
            if self.janela and self.event == 'imgq':
                
                folder = sg.popup_get_folder('Onde esta sua Imagem')
                if not folder:
                    exit(0)
                file_list = os.listdir(folder)
                fnames = [f for f in file_list if os.path.isfile(
                os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp", ".gif", ".ico","pdf"))]
                print(fnames)
                num_files = len(fnames)
                print('quantidade de arquivos',num_files)
                print('digite o nome do aquivo')


                
            if self.janela and self.event =='enter':
                self.exibindoImagem()



tela =  ConversorTexto()
tela.inicial()
