# === CONFIGURAÇÕES PERSONALIZÁVEIS ===

nome = "André Filipe"
descricao = "DevOps iniciante com foco em automação e shell script"
projetos = [
    {"titulo": "Projeto Exemplo 1", "descricao": "Descrição do projeto 1", "link": "#"},
    {"titulo": "Projeto Exemplo 2", "descricao": "Descrição do projeto 2", "link": "#"},
]
links = {
    "GitHub": "https://github.com/seuusuario",
    "LinkedIn": "https://linkedin.com/in/seuperfil",
    "E-mail": "andrefilipe@email.com",
    "Instagram Dev": "#",
    "Outro": "#"
}

# === GERAÇÃO DO HTML ===

html = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Portfólio - {nome}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            padding: 40px;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #222;
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        li {{
            margin-bottom: 10px;
        }}
        a {{
            text-decoration: none;
            color: #0066cc;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{nome}</h1>
        <p><strong>{descricao}</strong></p>

        <h2>Projetos</h2>
        <ul>
"""

for projeto in projetos:
    html += f"<li><strong>{projeto['titulo']}</strong>: {projeto['descricao']} - <a href='{projeto['link']}'>Ver projeto</a></li>"

html += """
        </ul>
        <h2>Links</h2>
        <ul>
"""

for nome_link, url in links.items():
    html += f"<li><a href='{url}' target='_blank'>{nome_link}</a></li>"

html += """
        </ul>
    </div>
</body>
</html>
"""

# === SALVANDO O ARQUIVO HTML ===

with open("portfolio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Site gerado com sucesso: portfolio.html")
