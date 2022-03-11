import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


GUI = Builder.load_file('C:/lgabriel/projetos/aplicativo/aply.kv')

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        cot_dol = self.pc('USD')
        #self.on_press()
        self.root.ids['m1'].text = f"A cotação do dólar é R$ {cot_dol}"

    def pc(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dict_req = requisicao.json()
        cot = dict_req[f"{moeda}BRL"]["bid"]
        return cot
    
    def on_press(self):
        self.root.ids['b1'].text = 'Pressed'

MeuAplicativo().run()