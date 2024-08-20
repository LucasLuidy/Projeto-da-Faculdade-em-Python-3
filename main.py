import math

def main():
    calcular_opcao1 = False
    calcular_opcao2 = False
    calcular_opcao3 = False

    while True:
        print("********** Calculadora de Isolamento em Tubulações **********")

        if calcular_opcao1 or calcular_opcao2 or calcular_opcao3:
            if calcular_opcao1:
                print(f"Transferência de calor máxima admissível: {transferencia_maxima:.2f} (W/m)")
            if calcular_opcao2:
                print(f"Resistência térmica necessária: {resistencia_termica:.2f} (K/W)")
            if calcular_opcao3:
                print(f"Espessura do isolante: {espessura_isolante:.2f} (m)")
            print()

        print("[1] Máxima de Transferência de Calor")

        if calcular_opcao1:
            print("[2] Resistência Térmica")

        if calcular_opcao2:
            print("[3] Espessura do Isolante")

        print("[4] Sair")
        opcao_escolhida = input("Escolha uma das opções disponiveis: ")
        print("************************\n")

        if opcao_escolhida not in {'1', '2', '3', '4'}:
            print("Voce inseriu uma opção inválida!\n")
            continue

        if opcao_escolhida == '4':
            return

        if opcao_escolhida == '1':
            vazao_massica = float(input("Informe a Vazão Mássica[kg/s]: "))
            comprimento_tubulacao = float(input("Informe o Comprimento da Tubulação[m]: "))
            aumento_temperatura_maxima = float(input("Informe o Aumento da Temperatura Máxima Admissível[ºC]: "))
            transferencia_maxima = (vazao_massica * 4190 * aumento_temperatura_maxima) / comprimento_tubulacao
            print(f"A Transferência de calor máxima admissível é: {transferencia_maxima:.2f} (W/m)\n")
            calcular_opcao1 = True
            calcular_opcao2 = False
            calcular_opcao3 = False

        elif opcao_escolhida == '2':
            if calcular_opcao1:
                temperatura_ambiente = float(input("Informe a Temperatura do Ambiente: "))
                temperatura_fluido = float(input("Informe a Temperatura do Fluido: "))
                resistencia_termica = (temperatura_ambiente - temperatura_fluido) / transferencia_maxima
                print(f"A Resistência térmica necessária é: {resistencia_termica:.2f} (K/W)\n")
                calcular_opcao2 = True
                calcular_opcao3 = False
            else:
                print("É necessário calcular a Opção 1 antes de usar a Opção 2!\n")

        elif opcao_escolhida == '3':
            if calcular_opcao1 and calcular_opcao2:
                diametro_externo_tubulacao = float(input("Informe o Diâmetro Externo da tubulação: "))
                condutividade_isolante = float(input("Informe a Condutividade Térmica do Isolante: "))
                pi = 3.14
                F = 2 * pi * condutividade_isolante * resistencia_termica
                espessura_isolante = diametro_externo_tubulacao / 2 * (math.exp(F) - 1)
                print(f"A Espessura do isolante é: {espessura_isolante:.2f} (m)\n")
                calcular_opcao3 = True
            else:
                print("É necessário calcular a Opção 1 e a Opção 2 antes de usar a Opção 3!\n")

main()
