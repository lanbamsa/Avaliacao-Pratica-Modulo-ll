import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()

print("Tabela 'alunos' criada com sucesso!")
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ('João Silva', 20, 'joao@example.com'))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ('Maria Oliveira', 22, 'maria@example.com'))
cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", ('Carlos Souza', 19, 'carlos@example.com'))

conn.commit()

print("Registros inseridos com sucesso!")
cursor.execute("SELECT * FROM alunos")
alunos = cursor.fetchall()

print("Lista de alunos:")
for aluno in alunos:
    print(aluno)
def buscar_por_id(id):
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (id,))
    aluno = cursor.fetchone()
    if aluno:
        print(f"Aluno encontrado: {aluno}")
    else:
        print("Aluno não encontrado.")

buscar_por_id(1)
def atualizar_aluno(id, nome, idade, email):
    cursor.execute("UPDATE alunos SET nome = ?, idade = ?, email = ? WHERE id = ?", (nome, idade, email, id))
    conn.commit()
    print(f"Aluno com ID {id} atualizado com sucesso!")

atualizar_aluno(1, 'João Silva Neto', 21, 'joao.neto@example.com')

buscar_por_id(1)
def deletar_aluno(id):
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    conn.commit()
    print(f"Aluno com ID {id} deletado com sucesso!")

deletar_aluno(3)

cursor.execute("SELECT * FROM alunos")
alunos_restantes = cursor.fetchall()

print("Lista de alunos após a exclusão:")
for aluno in alunos_restantes:
    print(aluno)
conn.close()
