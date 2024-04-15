gerencia_estoque = []
def adicionaProduto(nome, preco, qtd):
    global gerencia_estoque
    produto = [nome, preco, qtd]
    gerencia_estoque.append(produto)
    print('Produto adicionado com sucesso!')

def exibeEstoque():
    for produto in gerencia_estoque:
        nome = produto[0]
        preco = produto[1]
        qtd = produto[2]
        total = preco * qtd
        print('------------------------------------')
        print(f'Produto: {nome}')
        print(f'Custo: R${preco}')
        print(f'Qtd. em estoque: {qtd}')
        print(f'Total em produtos: R${total}')
        print('------------------------------------')

def atualizaQuantidade(nome_produto, nova_qtd):
    global gerencia_estoque
    encontra_produto = False
    while encontra_produto == False:
        for produto in gerencia_estoque:
            if produto[0] == nome_produto:
                produto[2] = nova_qtd
                print(f'Quantidade de "{nome_produto} atualizado para {nova_qtd}"')  
                encontra_produto = True 
            else:
                print(f'Produto "{nome_produto}" não encontrado em estoque')  
                encontra_produto = True  
    

while True:
    print('===========================')
    print('GERENCIAMENTO DE ESTOQUE')
    print('===========================')
    print('[1] Adicionar novo produto\n[2] Exibir estoque atual\n[3] Atualizar quantidade de um produto\n[4] Sair')
    print('')
    op = int(input('Escolha uma opção: '))

    if op == 1:
       
        nome = str(input('Nome do produto: ')).lower().strip()
        preco = float(input('Digite o valor R$'))
        qtd = int(input('Quantidade em estoque: '))
        adicionaProduto(nome, preco, qtd)

    elif op == 2:
        exibeEstoque() 

    elif op == 3:
        nome_produto = str(input("Digite o nome do produto que deseja atualizar o estoque: ")).lower().strip()     
        nova_qtd = int(input("Digite a nova quantidade em estoque: "))
        atualizaQuantidade(nome_produto, nova_qtd)

    elif op == 4:
        break

    else:
        print('opção inválida')

    