from arena import personagem, boss

def main():
    jogador = personagem(100, 50, 45,20,  100)
    inimigo = boss(100, 50, 45, 100)
    while True:
        painel = input(f'''
=============================================================
Boss:
{inimigo.vida_boss()}
{inimigo.armor_boss()}

Personagem:
{jogador.vida()}
{jogador.armadura()}
Digite sua ação agora!!

[A]taque [H]ealer [E]special
=> ''').lower()
        
        if painel == 'a':
            inimigo.vida_boss() + inimigo.armor_boss() - jogador.ataque()

        if painel == 'h':
            jogador.cura()

        if painel == 'e':
            inimigo.vida_boss() + inimigo.armor_boss() - jogador.especial()



if __name__ == '__main__':
    main()