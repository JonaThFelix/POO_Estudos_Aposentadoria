class Pessoa:
  def __init__(self,nome,ano,sexo,pais):
    self.nome = nome
    self.ano = ano
    self.sexo = sexo
    self.pais = pais
    self.idade = 2023 - self.ano

  def apresentacao(self):
    print(f'Olá, eu me chamo {self.nome}, tenho {self.idade} anos, sexo {self.sexo} e moro no {self.pais}.')

  def aposentadoria(self):
    if self.idade >= 65:
      print(f'{self.nome} já pode se aposentar.')
    else:
      print(f'Infelizmente {self.nome} não está na idade de aposentadoria, pois só tem {self.idade} anos.\nRestando {65-self.idade} anos.')
