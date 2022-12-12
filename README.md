# NewLand
A fantasy adventure, with traces of the history of 1500 ("Discovery of Brazil").
Uma aventura de fantasia, com traços da historia de 1500("Descoberta do Brasil").

Descrever o projeto e instruções de como instalar os pacotes necessarios e rodar o programa

Link de Demonstração da Gameplay:
    -https://youtu.be/7KAp_Wlxi8

- Basico da história:
    O jogo conta a historia de uma tentativa de invasão dos portugueses no Brasil, porém a natureza escolhe 
quatro indivíduos para salvar toda a população que vive ali.

- Instalação:
    Foram utilizados modulos já pre-instalados do Python.
    Para funcionamento do Game, utiliza-se o PyGame.

-Instruções de Gameplay:

    -Teclas básicas:
        -Player 1:
            - W A S D (Movimentação Padrão) 
            - Q (Ataque Básico)
            - E (Habilidade Especial)
        
        -Player 2:
            - I J K L (Movimentação Padrão) 
            - U (Ataque Básico)
            - O (Habilidade Especial)
    
    -Personagens:
        Aliados: ------------------------

            -Clerigo:
                -Basica(CD 0.2seg ): Lança um furacão, causando dano no primeiro inimigo atingido
                -Especial(CD 5.0seg.): Carrega uma área ao redor do personagem, aplicando stun em TODOS
                            inimigos próximos.
            -Duelista:
                -Basica(CD 0.66seg): Realiza um ataque simples de florete, causando dano nos inimigos
                        atingidos.
                -Especial(CD 5.0seg):Avança com um ataque rápido, causando dano nos inimigos
                        em sua frente.
            -Shaman:
                -Basica(CD 0.1seg): Lança uma bola de fogo, causando dano no primeiro inimigo atingido
                -Especial(CD 15seg):Pausa a tela até selecionar a área atingida.
                            Invoca uma área, causando dano por segundo nos inimigos que estavam na hora do impacto.
            -Tanker:
                -Basica(CD 1.8seg): Avança com uma barrigada, causando dano e stun nos inimigos
                        atingidos
                -Especial(CD 7.0seg): Invoca um poder de cura, recupando parte de sua vida perdida.
        
        Inimigos: ------------------------

            -Soldado: 
                -Basica(CD 2.3seg): Realiza um ataque simples de machado, causando dano nos inimigos
                        atingidos.
                -Especial(CD 8.3seg): Joga um bastão com corrente, causando dano e stun nos inimigos atingidos.

            -Boss: 
                -Basica(CD 2.3seg): Realiza um ataque simples de chicote, causando dano e aplica redução de velocidade nos inimigos atingidos.
                -Especial(CD 9.3seg): Utiliza os poderes do portal, invocando de sua terra natal, aliados para atacar por ele.

        Estruturas e Areas de efeito: ---------

            -Totem:
                -Especial: Ao ser destruido, invoca o poder de cura, recuperando parte da vida perdida de todos aliados proximos.
            -Circulo de Gelo:
                -Especial: Ao encontrar um alvo proximo, se aproxima até ativar a magia, aplicando redução na velocidade por um breve momento.
            -Circulo de Teleporte:
                -Especial: Ao encontrar um alvo proximo, se aproxima até ativar a magia, teleportando o alvo para um local aleatório.