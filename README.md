<h1 align="center"><strong>integral</strong>.pjbl</h1>

<p align="center">Trabalho da faculdade para exemplo de cliente e servidor, com execução em paralelo</p>

<h4 align="center"> 
	- Status: ✅ -
</h4>

### ☑️ Sobre
---

<p>
  De acordo com as aulas da matéria "Programação Distribuída, Paralela e Concorrente", criei este repositório.
  O foco é que ele tenha chamadas cliente e servidor, mas as execuções devem ser feitas simulando 4 servidores para que os cálculos sejam em paralelo
</p>

### 🔌 Como rodar o projeto

Para rodar o projeto você deverá executar o cliente e os servidores:

```bash
# Cliente
cd .\client\client-integral-pjbl\

# Baixa as dependencias
npm install

# Executa o cliente
npm run dev

# cliente rodando na url: http://127.0.0.1:5173/
```

```bash
# Servidor
cd .\server\

# Virtualização
python3 -m venv venv
```

> **Warning**</br>
> Para o comando ```./venv/bin/pip``` caso esteja no **Windows** deverá substituir para ```./venv/Scripts/pip```

```bash
# Atualiza o pip
./venv/bin/pip install --upgrade pip

# Baixa dependencias
./venv/bin/pip install -r requirements.txt

# Executa o servidor, importante rodar o mesmo comando paras portas 8001, 8002 e 8003.
./venv/bin/python -m uvicorn app.main:app --port=8000 --reload

# servidor rodando na url: http://127.0.0.1:8000/
```

### 🔋 Tecnologias
---

- [Vue](https://vuejs.org/)
- [Python](https://python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

### 🎲 Feito por
---

<a href="https://github.com/LeonardoLuize">
 <img src="https://avatars.githubusercontent.com/u/74014082?v=4" width="100px;"/>
 <br />
 <sub><b>Leonardo Luize</b></sub></a> <a href="https://github.com/LeonardoLuize" >💻</a>


Feito por Leonardo Luize 😁

[![Linkedin Badge](https://img.shields.io/badge/-Leonardo-blue?style=rounded&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/leonardoluize/)](https://www.linkedin.com/in/leonardoluize/) 
[![Gmail Badge](https://img.shields.io/badge/-leonardo.luize2@gmail.com-c14438?style=rounded&logo=Gmail&logoColor=white&link=mailto:leonardo.luize2@gmail.com)](mailto:leonardo.luize2@gmail.com)

