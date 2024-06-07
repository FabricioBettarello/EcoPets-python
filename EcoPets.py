# Define a função principal do programa.
def main():
    # Inicia um loop infinito.
    while True:
        # Dá as boas-vindas e explica o propósito do questionário.
        print("Bem-vindo ao questionário EcoPet!")
        print("Vamos encontrar o melhor EcoPet para você.")
        print("-----------------------------------------")
        # Mostra um desenho ASCII de um pet.
        print("""
  _____     ____
 /      \  |  o | 
|        |/ ___\| 
|_________/     
|_|_| |_|_|
""")

        # Lista de possíveis EcoPets.
        pets = ["Tartaruga", "Golfinho", "Tubarão"]
        # Perguntas que serão feitas ao usuário.
        questoes = [
            "Você prefere um EcoPet que possa nadar rapidamente (sim/não)? ",
            "Você prefere um EcoPet que possa mergulhar profundamente (sim/não)? ",
            "Você prefere um EcoPet que possa viver em águas quentes (sim/não)? "
        ]
        # Respostas esperadas para cada EcoPet.
        resps = [
            ["não", "sim", "sim"],  # Tartaruga
            ["sim", "não", "sim"],  # Golfinho
            ["sim", "sim", "não"]   # Tubarão
        ]
        # Lista para armazenar as respostas do usuário.
        resps_usuario = []
        # Loop para fazer as perguntas e coletar as respostas.
        for questao in questoes:
            while True:
                # Pede a resposta do usuário e a converte para minúsculas.
                resp = input(questao).lower()
                # Verifica se a resposta é válida.
                if resp in ["sim", "não"]:
                    # Adiciona a resposta válida à lista.
                    resps_usuario.append(resp)
                    break
                else:
                    # Informa ao usuário que a resposta foi inválida.
                    print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

        # Variáveis para determinar o melhor EcoPet e sua pontuação.
        melhor_pet = None
        melhor_pont = -1
        # Loop para comparar as respostas do usuário com as esperadas.
        for i in range(len(pets)):
            # Contador de pontuação para o EcoPet atual.
            pont = 0
            # Loop para verificar cada resposta.
            for j in range(len(resps[i])):
                # Se a resposta do usuário corresponder à esperada, aumenta a pontuação.
                if resps[i][j] == resps_usuario[j]:
                    pont += 1
            # Se a pontuação for a maior até agora, atualiza o melhor EcoPet.
            if pont > melhor_pont:
                melhor_pet = pets[i]
                melhor_pont = pont

        # Mostra o resultado para o usuário.
        print("-----------------------------------------")
        print(f"O melhor EcoPet para você é o {melhor_pet}!")

        # Loop para perguntar se o usuário quer continuar.
        while True:
            # Pede ao usuário para decidir se continua ou não.
            cont = input("Deseja continuar o questionário? Digite 1 para continuar ou 0 para concluir: ")
            # Verifica se a entrada é válida.
            if cont in ["0", "1"]:
                break
            else:
                # Informa ao usuário que a entrada foi inválida.
                print("Entrada inválida. Por favor, digite 1 para continuar ou 0 para concluir.")
        
        # Se o usuário decidir concluir, sai do loop infinito.
        if cont == "0":
            break

# Chama a função principal para iniciar o programa.
main()