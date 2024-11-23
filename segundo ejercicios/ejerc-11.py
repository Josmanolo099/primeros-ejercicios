int main() {
    char idJugador1[50], idJugador2[50];
    int modoJuego, puntosJugador1 = 0, puntosJugador2 = 0;
    char continuar = 's';
    int cicloPC = 1; // Control para las elecciones del PC

    // Bienvenida
    printf("Bienvenido a Piedra, Papel o Tijera.\n");

    // Solicitar IDs de los jugadores
    printf("Ingrese el ID del Jugador 1: ");
    scanf("%s", idJugador1);

    printf("Seleccione el modo de juego:\n");
    printf("1. Jugar contra el PC\n");
    printf("2. Modo Multijugador (dos jugadores)\n");
    printf("Ingrese su elección: ");
    scanf("%d", &modoJuego);

    if (modoJuego == 2) {
        printf("Ingrese el ID del Jugador 2: ");
        scanf("%s", idJugador2);
    } else {
        sprintf(idJugador2, "PC"); // Asignar "PC" como ID del jugador 2
    }

    while (continuar == 's' || continuar == 'S') {
        int eleccionJugador1, eleccionJugador2;

        // Jugador 1 elige
        printf("\nOpciones:\n1. Piedra\n2. Papel\n3. Tijera\n");
        printf("%s, ingrese su elección (1-3): ", idJugador1);
        scanf("%d", &eleccionJugador1);

        // Validar entrada de jugador 1
        while (eleccionJugador1 < 1 || eleccionJugador1 > 3) {
            printf("Entrada inválida. Intente nuevamente: ");
            scanf("%d", &eleccionJugador1);
        }

        // Jugador 2 o PC elige
        if (modoJuego == 2) {
            printf("%s, ingrese su elección (1-3): ", idJugador2);
            scanf("%d", &eleccionJugador2);

            // Validar entrada de jugador 2
            while (eleccionJugador2 < 1 || eleccionJugador2 > 3) {
                printf("Entrada inválida. Intente nuevamente: ");
                scanf("%d", &eleccionJugador2);
            }
        } else {
            eleccionJugador2 = cicloPC;         // PC elige cíclicamente
            cicloPC = (cicloPC % 3) + 1;       // Cambia entre 1, 2, 3
            printf("%s eligió: %d\n", idJugador2, eleccionJugador2);
        }

        // Determinar ganador de la ronda
        if (eleccionJugador1 == eleccionJugador2) {
            printf("La ronda terminó en empate.\n");
        } else if ((eleccionJugador1 == 1 && eleccionJugador2 == 3) || 
                   (eleccionJugador1 == 2 && eleccionJugador2 == 1) || 
                   (eleccionJugador1 == 3 && eleccionJugador2 == 2)) {
            printf("%s gana esta ronda.\n", idJugador1);
            puntosJugador1++;
        } else {
            printf("%s gana esta ronda.\n", idJugador2);
            puntosJugador2++;
        }

        // Mostrar puntuación actual
        printf("\nPuntuación actual:\n");
        printf("%s: %d puntos\n", idJugador1, puntosJugador1);
        printf("%s: %d puntos\n", idJugador2, puntosJugador2);

        // Preguntar si desean jugar otra ronda
        printf("\n¿Desean jugar otra ronda? (s/n): ");
        scanf(" %c", &continuar);
    }

    // Determinar el ganador final
    printf("\nPartida finalizada.\n");
    if (puntosJugador1 > puntosJugador2) {
        printf("El ganador es: %s con %d puntos.\n", idJugador1, puntosJugador1);
    } else if (puntosJugador1 < puntosJugador2) {
        printf("El ganador es: %s con %d puntos.\n", idJugador2, puntosJugador2);
    } else {
        printf("La partida terminó en empate.\n");
    }

    return 0;
}
