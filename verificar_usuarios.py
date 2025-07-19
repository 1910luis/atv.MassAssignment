import sqlite3

# Conecta ao banco
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Busca todos os usuários com seus status de admin
cursor.execute("SELECT id, username, is_admin FROM users")
usuarios = cursor.fetchall()

# Exibe os resultados
print("Usuários registrados:")
print("=" * 30)
for id, username, is_admin in usuarios:
    status = "Administrador" if is_admin else "Comum"
    print(f"ID: {id} | Usuário: {username} | is_admin: {is_admin} ({status})")

conn.close()
