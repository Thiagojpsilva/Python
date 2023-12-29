from log import LogFileMixin, LogPrintMixin

class Eletronico:
    def __init__(self,nome):
        self._nome = nome
        self._ligado = False
        
    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class SmartPhone(Eletronico, LogFileMixin):
    
    def ligar(self):
         super().ligar()
         
         if self._ligado:
             msg = f'SmartPhone {self._nome} foi ligado.'
             self.log_success(msg)
         
    def desligar(self):
        super().desligar()
        
        if not self._ligado:
            msg = f'SmartPhone {self._nome} foi desligado.'
            self.log_error(msg)            
    