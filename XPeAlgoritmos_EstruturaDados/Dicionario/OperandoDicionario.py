
#Criando um dicionario
dict_funcionarios = {
    'funcionario1':{
        'nome': 'João',
        'sobrenome': 'Silva',
        'id': 1
    },
    'funcionario2':{
        'nome': 'Maria',
        'sobrenome': 'Santos',
        'id':2
    }
}

#Método para exibir todos os funcionários
def exibir_funcionarios():
    for funcionario in dict_funcionarios:
        print(dict_funcionarios[funcionario])

#Método para adicionar novos funcionários
def adicionar_funcionario(nome, sobrenome, id):
    novo_funcionario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'id': id
    }
    dict_funcionarios['funcionario'+str(id)] = novo_funcionario

#Método para remover funcionários
def remover_funcionario(id):
    del dict_funcionarios['funcionario'+str(id)]

#Método para buscar funcionários
def buscar_funcionario(id):
    return dict_funcionarios['funcionario'+str(id)]

print(buscar_funcionario(1))
remover_funcionario(1)
print (dict_funcionarios)
adicionar_funcionario('Jorge Parreira', 'Pereira', 3)
buscar_funcionario(2)

