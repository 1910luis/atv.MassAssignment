# Mass Assignment Attack - Exemplo em Flask

## Como executar

1. Instale as dependências:
```
pip install flask
```

2. Inicialize o banco de dados:
```
python database.py
```

3. Rode a aplicação vulnerável:
```
python app.py
```
Acesse: http://127.0.0.1:5000/

Para testar o ataque, envie `is_admin=1` via Postman ou form.

4. Rode a aplicação protegida:
```
python app_sanitizado.py
```
Agora qualquer envio de `is_admin` será ignorado.

5. Verifique os usuários cadastrados:
```
python verificar_usuarios.py
```
