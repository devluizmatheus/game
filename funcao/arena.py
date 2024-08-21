from dados import rolagem_dados

class personagem:
    def __init__(self, hp, armor, attack, healer, especial_damage):
        self.hp = hp
        self.armor = armor
        self.attack = attack
        self.healer = healer
        self.especial_damage = especial_damage

    def vida(self):
        return self.hp 
    
    def armadura(self):
        return self.armor
    def status_personagem(self):
        print(f'HP{self.hp}')
        print(f'Amor{self.armor}')

    def ataque(self):
        return (self.attack + rolagem_dados('d20')) * rolagem_dados('d6')
    
    def cura(self):
        self.hp += self.healer 

    def especial(self):
        return (self.especial_damage + rolagem_dados('d100'))



class boss:
    def __init__(self, hp, attack, armor, damage_especial):
        self.hp = hp
        self.attack = attack
        self.armor = armor
        self.damage_especial = damage_especial
    
    def vida_boss(self):
        return self.hp
    
    def armor_boss(self):
        return self.armor
    def status_boss(self):
        print(f'HP: {self.hp}')
        print(f'Armor: {self.armor}')

        


    def ataque(self):
        return self.attack + rolagem_dados('d20')

    def especial(self):
        return self.especial + rolagem_dados('d100')
