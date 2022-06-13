import random

class jokenpo:
  
    def __init__(self, player01, player02, rounds):
      
        self.player01 = player01
        self.player02 = player02
        self.points01 = 0
        self.points02 = 0
        self.rounds = int(rounds)
        self.movs = ['tesoura', 'pedra', 'papel']
        
    def Add_Point(self, input):
      
        if input == "player01":
          
            self.points01+=1
            
        elif input == "player02":
          
            self.points02+=1
            
    def verificador(self, mov1, mov2):
      
        movs = self.movs
        
        if mov1 == movs[0]:
          
            if mov2 == movs[0]:
                return "Empate"
              
            elif mov2 == movs[1]:
                return False
              
            elif mov2 == movs[2]:
              
                return True
              
        if mov1 == movs[1]:
          
            if mov2 == movs[1]:
              
                return "Empate"
              
            elif mov2 == movs[2]:
                return False
              
            elif mov2 == movs[0]:
                return True
              
        if mov1 == movs[2]:
          
            if mov2 == movs[2]:
              
                return "Empate"
              
            elif mov2 == movs[0]:
              
                return False
              
            elif mov2 == movs[1]:
              
                return True

new_game = jokenpo(input("Digite um nome para o Jogador 01 :"), input("Digite um nome para o Jogador 01 :"),input("Quantidades de rodadas: "))

while new_game.points01+new_game.points02 < new_game.rounds:
  
    mov1 = random.choice(new_game.movs)
    mov2 = random.choice(new_game.movs)
    
    retorno = new_game.verificador(mov1,mov2)
    
    print(f"{new_game.player01} jogou {mov1}, {new_game.player02} jogou {mov2}")
    
    if retorno == "Empate":
        print("Empate, outra rodada.")
        
    elif retorno:
        print(f"{new_game.player01} venceu")
        new_game.Add_Point("player01")
        
    else:
        print(f"{new_game.player02} venceu")
        new_game.Add_Point("player02")
    print("=-"*30)
    
print(f"Pontuação do {new_game.player01}: {new_game.points01}")
print(f"Pontuação do {new_game.player02}: {new_game.points02}")
