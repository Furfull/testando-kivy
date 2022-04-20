from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

kv = """

<Incrementador>:
    Menu:
        name: 'menu'
    Janela:
        name: 'janela'
    Karaoke:
        name: '00001'
    Catalogo:
        name: 'catalogo'
    Karaoke2:
        name: '00002'
    Karaoke3:
        name: '00003'
    Karaoke4:
        name: '00004'
    Karaoke5:
        name: '00005'
<Menu>:
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: "C:/lgabriel/projetos/karaoke/imagem.jpg"
            allow_stretch: True
        Button: 
            background_color: '#EC6DFF'
            size_hint: 1, 0.3
            text: 'CANTAR!'
            on_release: app.root.current = 'janela'
<Janela>:
    id: janela
    BoxLayout:
        id: box1
        orientation: 'vertical'
        TextInput:
            id: tex
            size_hint: 1, 0.1
            text: ''
            hint_text: 'Digite o código da sua música'
        Button:
            background_color: '#EC6DFF'
            id: pesquisar
            text: 'Pesquisar'
            size_hint: 1, 0.1
            on_release: app.root.current = tex.text
        Button:
            id: caalogo
            background_color: '#EC6DFF'
            text: 'Catalogo'
            size_hint: 1, 0.1
            on_release: app.root.current = 'catalogo'
        Image:
            source: "C:/lgabriel/projetos/karaoke/imagem.jpg"
            allow_stretch: True

<Catalogo>:
    id: catalogo
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True

        Label:
            size_hint_y: None
            height: self.texture_size[1]
            text_size: self.width, None
            padding: 10, 10
            text:
                " Espanhola cod - 00001 A ha   Hunting High and Low cod - 00002  Doors Down - Here Without You cod - 00003  Ana Carolina -  Garganta cod - 00004  Almir Sater - Tocando em frente cod - 00005"
    Button:
        id: botao
        background_color: 0.5, 0.5, 0.5, 1
        size_hint: 1, 0.1
        text: 'ESCOLHER'
        on_release: app.root.current = 'janela'

<Karaoke>:
    id: 00001
    BoxLayout:
        orientation: 'vertical'
        VideoPlayer:
            id: videok
            source: "C:/lgabriel/projetos/karaoke/Espanhola.avi"
            state: "pause"
            options: {'eos': 'loop'}
            allow_stretch: True
            size: 1920, 1080
        Button:
            id: botao
            background_color: 0.5, 0.5, 0.5, 1
            size_hint: 1, 0.1
            text: 'SAIR'
            on_release: app.root.current = 'menu'
<Karaoke2>:
    id: 00002
    BoxLayout:
        orientation: 'vertical'
        VideoPlayer:
            source: "C:/lgabriel/projetos/karaoke/A ha   Hunting High and Low.avi"
            state: "stop"
            options: {'eos': 'loop'}
            allow_stretch: True
        Button:
            size_hint: 1, 0.1
            background_color: 0.5, 0.5, 0.5, 1
            text: 'SAIR'
            on_release: app.root.current = 'menu'
<Karaoke3>:
    id: 00003
    BoxLayout:
        orientation: 'vertical'
        VideoPlayer:
            source: "C:/lgabriel/projetos/karaoke/Doors Down - Here Without You.mp4"
            state: "stop"
            options: {'eos': 'loop'}
            allow_stretch: True
        Button:
            size_hint: 1, 0.1
            background_color: 0.5, 0.5, 0.5, 1
            text: 'SAIR'
            on_release: app.root.current = 'menu'
<Karaoke4>:
    id: 00004
    BoxLayout:
        orientation: 'vertical'
        VideoPlayer:
            source: "C:/lgabriel/projetos/karaoke/Ana Carolina -  Garganta.avi"
            state: "stop"
            options: {'eos': 'loop'}
            allow_stretch: True
        Button:
            size_hint: 1, 0.1
            background_color: 0.5, 0.5, 0.5, 1
            text: 'SAIR'
            on_release: app.root.current = 'menu'
<Karaoke5>:
    id: 00005
    BoxLayout:
        orientation: 'vertical'
        VideoPlayer:
            id: videokaraoke5
            source: "C:/lgabriel/projetos/karaoke/Almir Sater - Tocando em frente.avi"
            state: "stop"
            options: {'eos': 'loop'}
            allow_stretch: True
        Button:
            size_hint: 1, 0.1
            background_color: 0.5, 0.5, 0.5, 1
            text: 'SAIR'
            on_release: app.root.current = 'menu'
"""


class Incrementador(ScreenManager):
    pass
class Menu(Screen):
    pass
class Janela(Screen):
    pass
class Karaoke(Screen):
    pass
class Catalogo(Screen):
    pass
class Karaoke2(Screen):
    pass
class Karaoke3(Screen):
    pass
class Karaoke4(Screen):
    pass
class Karaoke5(Screen):
    pass
class TransferOKE(App):
    def build(self):
        return Incrementador()
        #return Builder.load_string(kv)
TransferOKE().run()
