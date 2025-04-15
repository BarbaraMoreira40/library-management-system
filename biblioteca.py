import pyodbc

def conectar():
    return pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=localhost;"
        "DATABASE=BibliotecaDB;"
        "Trusted_Connection=yes;"
    )
def adicionar_livro(titulo, autor, ano_publicacao, genero):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO Livros (Titulo, Autor, Ano_Publicacao, Genero) VALUES (?, ?, ?, ?)",
        (titulo, autor, ano_publicacao, genero),
    )
    conexao.commit()
    conexao.close()
    print("Livro adicionado com sucesso!")
def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Livros")
    livros = cursor.fetchall()
    conexao.close()

    for livro in livros:
        print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Gênero: {livro[4]}")
def atualizar_livro(id_livro, titulo, autor, ano_publicacao, genero):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE Livros SET Titulo=?, Autor=?, Ano_Publicacao=?, Genero=? WHERE Id=?",
        (titulo, autor, ano_publicacao, genero, id_livro),
    )
    conexao.commit()
    conexao.close()
    print("Livro atualizado com sucesso!")
def deletar_livro(id_livro):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Livros WHERE Id=?", (id_livro,))
    conexao.commit()
    conexao.close()
    print("Livro removido com sucesso!")
def menu():
    while True:
        print("\n--- Gerenciamento de Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Atualizar Livro")
        print("4. Remover Livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            genero = input("Gênero: ")
            adicionar_livro(titulo, autor, ano, genero)

        elif escolha == "2":
            listar_livros()

        elif escolha == "3":
            id_livro = int(input("ID do livro: "))
            titulo = input("Novo Título: ")
            autor = input("Novo Autor: ")
            ano = int(input("Novo Ano de Publicação: "))
            genero = input("Novo Gênero: ")
            atualizar_livro(id_livro, titulo, autor, ano, genero)

        elif escolha == "4":
            id_livro = int(input("ID do livro a remover: "))
            deletar_livro(id_livro)

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

# Executar o menu
menu()
