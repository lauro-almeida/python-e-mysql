import MySQLdb


def conectar():
    """
    Função para conectar ao servidor.
    """
    try:
        conn = MySQLdb.connect(
            db='pmysql',
            host='localhost',
            user='lauro',
            password='*******'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro na conexão ao MySQL Server: {e}')


def desconectar(conn):
    """
    Função para desconectar o servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Essa função lista os produtos.
    """

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        for produto in produtos:
            print('...Listando produtos...')
            print('-----------------------')
            print(f"ID: {produto[0]}")
            print(f"Produto: {produto[1]}")
            print(f"Preço: {produto[2]}")
            print(f"Estoque: {produto[3]}")
            print('-----------------------')
    else:
        print('Ainda não existem produtos cadastrados.')
    desconectar(conn)


def inserir():
    """
    Função para inserir novos produtos.
    """
    conn = conectar()
    cursor = conn.cursor()

    nome = input('Informe o nome do produto: ')
    preco = float(input('Informe o preço do produto: R$'))
    estoque = int(input('Informe a quantidade de produtos em estoque: '))

    cursor.execute(f"INSERT INTO produtos(nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O produto {nome} foi adicionado com sucesso.")
    else:
        print('Não foi possível adicionar o produto.')
    desconectar(conn)


def atualizar():
    """
    Essa função atualiza um produto.
    """

    conn = conectar()
    cursor = conn.cursor()

    listar()
    codigo = input('Informe o código (ID) do produto que deseja atualizar: ')

    
    print('Qual dado do produto deseja atualizar:')
    print('[1] - Nome')
    print('[2] - Preço')
    print('[3] - Quantidade em estoque')
    print('[4] - Cancelar atualização')
    opcao = int(input('Opção: '))

    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            nome = input('Informe o novo nome: ')
            cursor.execute(f"UPDATE produtos SET nome='{nome}' WHERE id={codigo}")
            conn.commit()
        elif opcao == 2:
            preco = float(input('Informe o novo preço: R$'))
            cursor.execute(f"UPDATE produtos SET preco={preco} WHERE id={codigo}") 
            conn.commit()
        elif opcao == 3:
            estoque = int(input('Informe a nova quantidade em estoque: '))
            cursor.execute(f"UPDATE produtos SET estoque={estoque} WHERE id={codigo}")
            conn.commit()
        else:
            pass
    else:
        print('Opção inválida!')

    if cursor.rowcount == 1:
        print(f'O produto foi atualizado com sucesso.')
    else:
        print('Não foi possível atualizar o produto.')
    desconectar(conn)
        

def deletar():
    """
    Essa função deleta um produto.
    """
    conn = conectar()
    cursor = conn.cursor()

    listar()

    codigo = int(input('Informe o código (ID) do produto que deseja deletar: '))
    confirmacao = str(input('ATENÇÃO! Essa ação é irreversível. Deseja continuar? (S/N): ')).upper()
    if confirmacao == 'S':
        cursor.execute(f'DELETE FROM produtos WHERE id={codigo}')
        conn.commit()
    else:
        pass
    if cursor.rowcount == 1:
        print('Produto deletado com sucesso.')
    else:
        print('Não foi possível deletar o produto.')
    desconectar(conn)

def menu():
    """
    Essa função gera um menu interativo com o usuário através do terminal.
    """

    while True:
        print(f"{'='*10}Gerenciador de produtos{'='*10}")
        print('Selecione uma das opções:')
        print('[1] - Listar produtos')
        print('[2] - Inserir produto')
        print('[3] - Atualizar produto')
        print('[4] - Deletar produto')
        print('[5] - Sair')
        opcao = int(input('Opção: '))

        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            else:
                print('Desconectado')
                exit()
        else:
            print('Opção inválida!')