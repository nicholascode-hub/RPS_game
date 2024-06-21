# importing 

import random


#main 

class RPS:
    def __init__(self):
        self.player_wins = 0  # Inicializa o contador de vitórias do jogador
        self.python_wins = 0  # Inicializa o contador de vitórias do Python
        self.total_games = 0  # Inicializa o contador de total de jogos

        self.player_name = None  # Variável para armazenar o nome do jogador

        self.loop_RPS()

    def loop_RPS(self):
        # Loop principal do jogo
        while True:
            if not self.player_name:
                self.get_player_name()  # Solicita o nome do jogador apenas se não estiver definido ainda

            self.game()  # Inicia o jogo

    def get_player_name(self):
        while True:
            player = input('Type your name: \n')

            # Verifica se o nome contém apenas letras ou é alfanumérico
            if player.isalnum() and not player.isdigit():
                self.player_name = player
                break  # Sai do loop se o nome for válido
            else:
                print('Invalid input! Name must contain at least one letter and can\'t be numbers only.')

    def game(self):
        round_choice = int(input('1. Rock\n2. Paper\n3. Scissors\n0. Quit\n'))

        if round_choice == 0:
            print(f'{self.player_name} See you later, alligator!')
            self.display_stats()
            exit()  # Termina o programa se o usuário escolher 0

        python_choice = int(random.choice('123'))
        print(f'{self.player_name} chose {round_choice}, Python chose {python_choice}')

        self.total_games += 1  # Incrementa o contador de total de jogos

        # Determina o resultado do jogo
        if round_choice == python_choice:
            print('It\'s a draw!')
        elif (round_choice == 1 and python_choice == 3) or \
             (round_choice == 2 and python_choice == 1) or \
             (round_choice == 3 and python_choice == 2):
            print(f'{self.player_name} wins!')
            self.player_wins += 1  # Incrementa o contador de vitórias do jogador
        else:
            print('Python wins!')
            self.python_wins += 1  # Incrementa o contador de vitórias do Python

        self.display_stats()  # Mostra as estatísticas após cada jogo

    def display_stats(self):
        print(f'\nStats so far:')
        print(f'Total games played: {self.total_games}')
        print(f'{self.player_name}\'s wins: {self.player_wins}')
        print(f'Python\'s wins: {self.python_wins}')
        print('------------------------')

# Criando uma instância da classe RPS para iniciar o jogo
if __name__ == "__main__":
    game = RPS()

