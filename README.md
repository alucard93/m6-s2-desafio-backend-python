# m6-s2-desafio-backend-python

 [![Typing SVG](https://readme-typing-svg.herokuapp.com/?font=Roboto&color=e1e1e6&size=35&center=true&vCenter=true&weight=700&width=1000&lines=A+aplicação+consiste+em+parsear+arquivo+de+texto+CNBAB;+salvando+suas+informações+[transações+financeiras];em+uma+base+de+dados;Seja+bem-vindo+!+:%29)](https://git.io/typing-svg)
 <br> 
 <br> 

<h2> Tecnologias utilizadas </h2>
<ul>
    <li>Python</li>
    <li>Django</li>
    <li>Bootstrap</li>
</ul>


<h2>Prossiga com os passos:</h2>

<br>
1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

1. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```
<br> 

### Instale as dependências

```
pip install -r requirements.txt
```
<br>

### Execute as migrações

```
python manage.py migrate
```
<br> 

### Inicie o servidor

```
python manage.py runserver
```

### A aplicação possui 2 endpoint

```
http://127.0.0.1:8000 - default
```
- Utilizada para demostrar todos os dados.
- Possui um botão que redireciona para a url que realiza o somatório e a filtragem
```
http://127.0.0.1:8000/cnab/filtro
```
 - Utilizada para realização dos filtros e para apresentação do somatório por loja.
## Possui as seguintes funcionalidade:
- Um campo para pesquisa que filtra com base no nome da loja e com base na pesquisa retorna o cálculo das operações
- Um botão para voltar a tela default
- Paginação ao final da página

