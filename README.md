# 🎥 StreamVibe - Plataforma de Avaliações

Este projeto consiste em uma plataforma de avaliações que recompensa os usuários com cripto através do da interação dele com a plataforma.

## 🎯 Funcionalidades

- Inserção de filmes
- Cadastro de filmes
- Uso de tokens para recompensar os usuários
- Conexão back-end com cripto

## 📋 Estrutura do Projeto

O site é composto por aplicativos divididos através de cada funcionalidade do site:

- **filmes**: Principal app do projeto, aqui é onde o cadastro, leitura, edição e eliminação dos filmes é feita.
- **usuarios**: Gerenciamento de usuário cadastrados no banco de dados.
- **sistema**: Antigo app do projeto que armazenava as informações gerais, mas sofreu uma refatoração. 

## 🚀 Tecnologias Utilizadas

As principais tecnologias utilizadas no desenvolvimento deste projeto são:

- **Django**: Para criar o back-end do projeto através do framework.
- **SQLite**: Para armazenar as informações em um banco de dados.
- **Solidity**: Para programar os tokens do sistema.

## 📦 Como Rodar o Projeto

1. Faça o download ou clone este repositório:

```bash
git clone https://github.com/andre-fe-santana/projetoDjango
```

2. Ative o ambiente virtual (venv):

```bash
venv/Scripts/activate
```

3. Rode o servidor local:
```bash
python manage.py runserver
```

## 🏗️ Estrutura das pastas
📁**base_static/base_templates:**
Guarda os arquivos estáticos do projeto, seja CSS, HTML, JS e imagens do site.

📁**filmes:**
App da funcionalidade de filmes do projeto, guarda views e URLs do app.

📁**imagens:**
Guarda as imagens gerais do projeto, seja de usuários, filmes, etc.

📁**media:**
Guarda as imagens enviadas pelo usuário

📁**usuarios:**
App de usuários, guarda views e URLs do app.

## 📸 Capturas de Telas
### Tela inicial
![image](https://github.com/user-attachments/assets/09f111b8-85a8-4097-ace7-f773ec7f31a0)
### Login
![image](https://github.com/user-attachments/assets/950e021e-9dfe-4bbd-a8a2-dc4b44ce2eee)
### Cadastro
![image](https://github.com/user-attachments/assets/262e6ed9-3008-4319-844e-70a551cf46f6)


## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir *issues* e *pull requests*.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
