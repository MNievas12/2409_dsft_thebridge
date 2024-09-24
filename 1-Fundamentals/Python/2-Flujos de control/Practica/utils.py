import random

def jugar(vidas=2):
    print("Bienvenido a una nueva partida")
    n_oculto = random.randint(1,5)
    vidas_partida = vidas

    while vidas_partida > 0:
        # jugar el turno, si no acierto, perderé una vida
        print("Tienes", vidas_partida, "vidas")
        n_usuario = int(input("Introduce número"))
        if n_usuario == n_oculto:
            print("You win! :)")
            print("Fin del juego.")
            break
        else:
            print("No has acertado!")
            vidas_partida = vidas_partida - 1
    else:
        print("You lose! :(")
        print(n_oculto, "era el número")
        if vidas - 1 > 0:
            jugar(vidas-1)

