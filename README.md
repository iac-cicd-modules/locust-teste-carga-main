# Locust Teste de Carga KXC

Modelo inicial para ECS de teste de carga a ser utilizado pela KXC.



## O que esse repositório faz?

Ao editar o arquivo locustfile.py, irá triggar uma pipeline na KXC call que automaticamente irá atualizar o ECS na KXC call para subir com acesso via IP Público um container para realizar teste de carga com clientes.


## Como utilizar esse repositório

### Clonando repositório

Clone o repositório em sua máquina

### Criando arquivo .har

https://github.com/SvenskaSpel/har2locust

Acima há a documentação para "Gravar" a tela e poder gerar o arquivo que será transformado no arquivo em python que o Locust lê.

### Substituir valor do arquivo gerado para o arquivo python do repositório

Substitua o arquivo gerado pelo arquivo deste repositório e realize o commit para triggar a pipeline

Obs: ECS com task zerada, subir para 1 após o deploy, acessar via IP Público na porta 8089.

Documentação:

https://docs.locust.io/en/stable/running-in-docker.html

https://docs.locust.io/en/stable/writing-a-locustfile.html
