class Televisor:
    def __init__(self, canal, volume):
        self.ligado = False
        self.canal = canal
        self.volume = volume
        self.max_volume = 100
        self.min_volume = 0
        self.max_canal = 100
        self.min_canal = 0
    
    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def aumentar_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
    
    def diminuir_volume(self):
        if self.volume > self.min_volume:
            self.volume -= 1

    def aumentar_canal(self):
        if self.canal < self.max_canal:
            self.canal += 1

    def diminuir_canal(self):
        if self.canal > self.min_canal:
            self.canal -= 1

    def imprimir(self):
        print(f'Canal: {self.canal}, Volume: {self.volume}, Ligado? {self.ligado}')

tv = Televisor(7, 30)
tv.ligar()
tv.aumentar_volume()
tv.imprimir()
