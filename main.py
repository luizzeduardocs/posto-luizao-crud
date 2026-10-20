from conexao import conectar


def fazer_login():
    print("\n====== LOGIN - POSTO LUIZÃO ======")
    email = input("E-mail: ").strip()
    senha = input("Senha: ").strip()

    conexao = conectar()
    if not conexao:
        return None

    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome FROM usuarios WHERE email = %s AND senha = %s",
        (email, senha),
    )
    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    if usuario:
        print(f"\nLogin realizado com sucesso! Bem-vindo(a), {usuario[1]}")
        return usuario[0]
    else:
        print("\nE-mail ou senha incorretos.")
        return None


def cadastrar_abastecimento(usuario_id):
    print("\n--- Novo Abastecimento ---")
    cliente = input("Nome do cliente: ").strip()
    combustivel = input("Tipo de combustível (gasolina/etanol/diesel): ").lower().strip()

    try:
        litros = float(input("Quantidade de litros: ").replace(",", "."))
        valor_litro = float(input("Valor por litro (R$): ").replace(",", "."))
    except ValueError:
        print("Valor inválido.")
        return

    total = litros * valor_litro

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """
        INSERT INTO abastecimentos (cliente, combustivel, litros, valor_litro, total, pago, usuario_id)
        VALUES (%s, %s, %s, %s, %s, FALSE, %s)
    """,
        (cliente, combustivel, litros, valor_litro, total, usuario_id),
    )

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Abastecimento cadastrado com sucesso!")


def listar_abastecimentos():
    print("\n--- Lista de Abastecimentos ---")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, cliente, combustivel, litros, valor_litro, total, pago FROM abastecimentos"
    )
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    if not registros:
        print("Nenhum abastecimento cadastrado.")
        return

    print("-" * 75)
    print("ID | Cliente          | Combustível | Litros | Total    | Pago")
    print("-" * 75)
    for r in registros:
        pago_str = "Sim" if r[6] else "Não"
        print(
            f"{r[0]:<2} | {r[1][:16]:<16} | {r[2]:<11} | {r[3]:<6.2f} | R${r[5]:<6.2f} | {pago_str}"
        )


def atualizar_abastecimento():
    print("\n--- Atualizar / Marcar como Pago ---")
    listar_abastecimentos()
    
    try:
        id_reg = int(input("\nDigite o ID do abastecimento que deseja atualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    print("1 - Marcar como Pago")
    print("2 - Alterar dados do cliente/litros")
    opcao = input("Escolha a opção de atualização: ").strip()

    conexao = conectar()
    cursor = conexao.cursor()

    if opcao == "1":
        cursor.execute("UPDATE abastecimentos SET pago = TRUE WHERE id = %s", (id_reg,))
        conexao.commit()
        print("Abastecimento marcado como PAGO com sucesso!")
    elif opcao == "2":
        novo_cliente = input("Novo nome do cliente: ").strip()
        try:
            novos_litros = float(input("Nova quantidade de litros: ").replace(",", "."))
            novo_preco = float(input("Novo valor por litro (R$): ").replace(",", "."))
        except ValueError:
            print("Valores inválidos.")
            cursor.close()
            conexao.close()
            return
        
        novo_total = novos_litros * novo_preco
        cursor.execute(
            """
            UPDATE abastecimentos 
            SET cliente = %s, litros = %s, valor_litro = %s, total = %s 
            WHERE id = %s
            """,
            (novo_cliente, novos_litros, novo_preco, novo_total, id_reg)
        )
        conexao.commit()
        print("Abastecimento atualizado com sucesso!")
    else:
        print("Opção inválida.")

    cursor.close()
    conexao.close()


def excluir_abastecimento():
    print("\n--- Excluir Abastecimento ---")
    listar_abastecimentos()
    
    try:
        id_reg = int(input("\nDigite o ID do abastecimento que deseja EXCLUIR: "))
    except ValueError:
        print("ID inválido.")
        return

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM abastecimentos WHERE id = %s", (id_reg,))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Registro excluído com sucesso!")


def filtrar_por_combustivel():
    print("\n--- Filtro por Combustível ---")
    tipo = input("Digite o tipo de combustível para filtrar (ex: gasolina, etanol, diesel): ").lower().strip()

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, cliente, combustivel, litros, valor_litro, total, pago FROM abastecimentos WHERE combustivel = %s",
        (tipo,)
    )
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    if not registros:
        print(f"Nenhum abastecimento encontrado para o combustível '{tipo}'.")
        return

    print("-" * 75)
    print(f"Filtro: {tipo.upper()}")
    print("ID | Cliente          | Combustível | Litros | Total    | Pago")
    print("-" * 75)
    for r in registros:
        pago_str = "Sim" if r[6] else "Não"
        print(
            f"{r[0]:<2} | {r[1][:16]:<16} | {r[2]:<11} | {r[3]:<6.2f} | R${r[5]:<6.2f} | {pago_str}"
        )


def menu(usuario_id):
    while True:
        print("\n====== PAINEL - POSTO LUIZÃO ======")
        print("1 - Cadastrar abastecimento")
        print("2 - Listar abastecimentos")
        print("3 - Atualizar abastecimento / Marcar pago")
        print("4 - Excluir abastecimento")
        print("5 - Filtrar abastecimentos por combustível")
        print("0 - Sair / Logout")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_abastecimento(usuario_id)
        elif opcao == "2":
            listar_abastecimentos()
        elif opcao == "3":
            atualizar_abastecimento()
        elif opcao == "4":
            excluir_abastecimento()
        elif opcao == "5":
            filtrar_por_combustivel()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


def main():
    while True:
        print("\n=== SISTEMA POSTO LUIZÃO ===")
        print("1 - Fazer Login")
        print("0 - Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            usuario_id = fazer_login()
            if usuario_id:
                menu(usuario_id)
        elif op == "0":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()