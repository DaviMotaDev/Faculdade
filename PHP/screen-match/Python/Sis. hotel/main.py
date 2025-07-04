from Hotel import Hotel
from Quarto import Quarto
from Hospede import Hospede
from Reserva import Reserva
#Importando as classes criadas

def exibir_menu():
    print("=== Sistema de Gerenciamento de Hotel ===")
    print("\n--- Menu do Hotel ---")
    print("1. Adicionar Quarto")
    print("2. Remover Quarto")
    print("3. Registrar Hóspede")
    print("4. Fazer Reserva")
    print("5. Cancelar Reserva")
    print("6. Listar Quartos")
    print("7. Sair")
    print("--------------------")
    opcao = input("Digite a opção desejada: ")
    return opcao

def main():
    hotel = Hotel()
    
    while True:
        opcao = exibir_menu()
        if opcao == "1": # Adicionar Quarto
           
            numero = int(input("Digite o número do quarto: "))
            tipo = input("Digite o tipo do quarto: ")
            quarto = Quarto(numero, tipo)
            hotel.add_quarto(quarto)
            print("Quarto adicionado com sucesso!")
        
        elif opcao == "2":# Remover Quarto
            
            numero = int(input("Digite o número do quarto a ser removido: "))
            quarto = Quarto(numero, "") # Aqui, o tipo não importa para remover
            hotel.remover_quarto(quarto)
            print("Quarto removido com sucesso!")
       
        elif opcao == "3":  # Registrar Hóspede
            
            nome = input("Digite o nome do hóspede: ")
            email = input("Digite o email do hóspede: ")
            id = int(input("Digite o ID do hóspede: "))
            hospede = Hospede(nome, email, id)
            hotel.registrar_hospede(hospede)
            print("Hóspede registrado com sucesso!")
        
        elif opcao == "4":  # Fazer Reserva

            id_hospede = int(input("Digite o ID do hóspede: "))
            numero_quarto = int(input("Digite o número do quarto: "))
            # Encontrar hóspede e quarto
            hospede = None
            quarto = None
            for h in hotel._hospedes:
                if h.get_id() == id_hospede:
                    hospede = h
            for q in hotel._quartos:
                if q._numero == numero_quarto:
                    quarto = q
            if hospede and quarto:
                if quarto.esta_disponivel():
                    reserva = Reserva(hospede, quarto)
                    hospede.fazer_reserva(reserva)
                    quarto.reservar()
                    hotel._reservas.append(reserva)
                    print("Reserva feita com sucesso!")
                else:
                    print("O quarto não está disponível.")
            else:
                print("Hóspede ou quarto não encontrados.")
        
        elif opcao == "5":  # Cancelar Reserva

            id_hospede = int(input("Digite o ID do hóspede: "))
            numero_quarto = int(input("Digite o número do quarto: "))
            # Encontrar reserva
            reserva = None
            for r in hotel._reservas:
                if r.get_hospede().get_id() == id_hospede and r.get_quarto()._numero == numero_quarto:
                    reserva = r
            if reserva:
                hotel.cancelar_reserva(reserva)
                print("Reserva cancelada com sucesso!")
            else:
                print("Reserva não encontrada.")
        
        elif opcao == "6":# Listar Quartos
            
            hotel.listar_quartos()
       
        elif opcao == "7":# Sair
            
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    main()