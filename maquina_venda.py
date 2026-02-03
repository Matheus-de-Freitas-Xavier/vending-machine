import customtkinter as ctk
from tkinter import messagebox as mb
import random

produto_nome = ['Coca-cola', 'Fanta', 'Sprite',
                'Água tônica', 'Itubaina', 'Suco de maracujá']

produto_preco = [14.09, 9.49, 6.87, 7.99, 6.99, 7.79]

produtos = {}
for i in range(len(produto_nome)):
    produtos[f'Produto_{i+1}'] = {
        'nome': produto_nome[i],
        'preco': produto_preco[i],
        'quantidade': 0,
        'estoque': random.randint(5, 10)
        }

def so_numero(char):
    if char == '':
        return True
    if char.count(',') > 1:
       return False
    if all(c in '0123456789,' for c in char):
        return True
    return False
    
def saida_troco(valor_nota, qntd):
    saida = ''
    if not 'centavo' in valor_nota and qntd == 1:
        saida += f'-> {qntd} nota de {valor_nota}\n'
    elif 'centavo' in valor_nota and qntd == 1:
        saida += f'-> {qntd} moeda de {valor_nota}\n'
    elif 'centavo' in valor_nota and qntd > 1:
        saida += f'-> {qntd} moedas de {valor_nota}\n'
    elif qntd == 0:
        return ''
    else:
        saida += f'-> {qntd} notas de {valor_nota}\n'
    return saida

def contagem_nota(troco_total, valor_da_nota):
    qntd_nota = 0
    while troco_total != 0:
        if troco_total >= valor_da_nota:
            troco_total = round(troco_total,2) - valor_da_nota
            qntd_nota += 1
        else:
            break
    return qntd_nota
    
def conta_troco(troco_real, qntd_nota, valor_da_nota):
    troco_real = troco_real - (qntd_nota * valor_da_nota)
    return troco_real

def quantidade_produto(num, sinal):
    if sinal == '-':
        produtos[f'Produto_{num}']['quantidade'] -= 1
        produtos[f'Produto_{num}']['estoque'] += 1
        botoes[num-1].configure(text=f'{produtos[f"Produto_{num}"]["nome"]}\nR$ {str(produtos[f"Produto_{num}"]["preco"]).replace(".",",")}\nEstoque: {produtos[f"Produto_{num}"]["estoque"]}')
        botoes[num-1].configure(state='enabled')
    else:
        if produtos[f'Produto_{num}']['estoque'] == 0:
            pass
        else:
            produtos[f'Produto_{num}']['quantidade'] += 1
            produtos[f'Produto_{num}']['estoque'] -= 1
            botoes[num-1].configure(text=f'{produtos[f"Produto_{num}"]["nome"]}\nR$ {str(produtos[f"Produto_{num}"]["preco"]).replace(".",",")}\nEstoque: {produtos[f"Produto_{num}"]["estoque"]}')
        
    valores = []
    for i in range(len(produtos)):
        valores.append(produtos[f'Produto_{i+1}']['preco'] * 
                       produtos[f'Produto_{i+1}']['quantidade'])
    total.configure(text=f'Total: R$ {str(round(float(sum(valores)),2)).replace(".",",")}')        

    if produtos[f'Produto_{num}']['quantidade'] == 0:
        texto_qntd[num-1].grid_forget()
        botao_menos[num-1].grid_forget()
    elif produtos[f'Produto_{num}']['estoque'] == 0:
        texto_qntd[num-1].configure(text=f'{produtos[f"Produto_{num}"]["quantidade"]} {produtos[f"Produto_{num}"]["nome"]}')
        mb.showwarning('Acabou o estoque', f'Acabou o estoque de {produtos[f"Produto_{num}"]["nome"]}')
        botoes[num-1].configure(state='disabled')
    else:
        texto_qntd[num-1].configure(text=f'{produtos[f"Produto_{num}"]["quantidade"]} {produtos[f"Produto_{num}"]["nome"]}')
        texto_qntd[num-1].grid(row=num-1, column=0, pady=2)
        botao_menos[num-1].grid(row=num-1, column=1, padx=10)


def maquina_venda():
    try:
        valores = []
        for i in range(len(produtos)):
            valores.append(produtos[f'Produto_{i+1}']['preco'] * 
                           produtos[f'Produto_{i+1}']['quantidade'])
            
        
        if entrada.get() == '':
            mb.showwarning('Sem entrada de dinheiro', 'Por favor, entre com alguma quantia')
        else:
            valor_pago = float(entrada.get().replace(',','.'))
            valor_total = float(sum(valores))
        
            if valor_total == 0.00:
                mb.showwarning('Carrinho vazio', 'Seu carrinho está vazio')
            else:
        
                if valor_pago > valor_total:
                    troco = float(valor_pago) - valor_total
                    saida = f'Troco a receber: R${troco:.2f}\n'
                    
                    nota100 = contagem_nota(troco, 100)
                    troco = conta_troco(troco, nota100, 100)
                    
                    nota50 = contagem_nota(troco, 50)
                    troco = conta_troco(troco, nota50, 50)
                    
                    nota20 = contagem_nota(troco, 20)
                    troco = conta_troco(troco, nota20, 20)
                    
                    nota10 = contagem_nota(troco, 10)
                    troco = conta_troco(troco, nota10, 10)
                    
                    nota5 = contagem_nota(troco, 5)
                    troco = conta_troco(troco, nota5, 5)
                    
                    nota2 = contagem_nota(troco, 2)
                    troco = conta_troco(troco, nota2, 2)
                    
                    nota1 = contagem_nota(troco, 1)
                    troco = conta_troco(troco, nota1, 1)
                    
                    nota050 = contagem_nota(troco, 0.50)
                    troco = conta_troco(troco, nota050, 0.50)    
                    
                    nota025 = contagem_nota(troco, 0.25)
                    troco = conta_troco(troco, nota025, 0.25)
                    
                    nota010 = contagem_nota(troco, 0.10)
                    troco = conta_troco(troco, nota010, 0.10)
                    
                    nota05 = contagem_nota(troco, 0.05)
                    troco = conta_troco(troco, nota05, 0.05)
                    
                    nota01 = contagem_nota(troco, 0.01)
                    troco = conta_troco(troco, nota01, 0.01)
                    
                    saida += '\n\nTroco composto por:\n'
                    saida += saida_troco('100 reais', nota100)
                    saida += saida_troco('50 reais', nota50)
                    saida += saida_troco('20 reais', nota20)
                    saida += saida_troco('10 reais', nota10)
                    saida += saida_troco('5 reais', nota5)
                    saida += saida_troco('2 reais', nota2)
                    saida += saida_troco('1 real', nota1)
                    saida += saida_troco('50 centavos', nota050)
                    saida += saida_troco('25 centavos', nota025)
                    saida += saida_troco('10 centavos', nota010)
                    saida += saida_troco('5 centavos', nota05)
                    saida += saida_troco('1 centavo', nota01)
                    mb.showinfo('Seu troco', saida)
                    total.configure(text='Total: R$ 0,00')
                    for i in range(6):
                        if produtos[f'Produto_{i+1}']['estoque'] == 0:
                            produtos[f'Produto_{i+1}']['estoque'] = produtos[f'Produto_{i+1}']['quantidade']
                            produtos[f'Produto_{i+1}']['quantidade'] = 0
                            botoes[i].configure(text=f'{produtos[f"Produto_{i+1}"]["nome"]}\nR$ {str(produtos[f"Produto_{i+1}"]["preco"]).replace(".",",")}\nEstoque: {produtos[f"Produto_{i+1}"]["estoque"]}', state='enable')
                        else:
                            pass
                    
                    entrada.delete(0, ctk.END)
                    for i in range(6):
                        produtos[f'Produto_{i+1}']['quantidade'] = 0
                        texto_qntd[i].grid_forget()
                        botao_menos[i].grid_forget()
                    
                elif valor_pago < valor_total and round(valor_total - valor_pago,2) == 1:
                    mb.showwarning('Dinheiro insuficiente', f'Ainda falta: R$ {valor_total - valor_pago:.2f} real')
                elif valor_pago < valor_total and round(valor_total - valor_pago,2) > 1:
                    mb.showwarning('Dinheiro insuficiente', f'Ainda faltam: R$ {valor_total - valor_pago:.2f} reais')
                elif valor_pago < valor_total and round(valor_total - valor_pago,2) < 1 and round(valor_total - valor_pago,2) > 0:
                    mb.showwarning('Dinheiro insuficiente', f'Ainda faltam: R$ {valor_total - valor_pago:.2f} centavos')
                else:
                    mb.showinfo('Dinheiro exato','Troco não necessário')
    except ValueError:
        mb.showerror('Erro de entrada', 'Erro de Entrada\nValor inválido. Use apenas números e vírgulas')

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry('360x660')
vcmd = (janela.register(so_numero), '%P')
janela.title('Máquina de venda')
ctk.CTkLabel(janela, text='--- Máquina de venda ---', font=('arial', 22, 'bold')).pack(pady=10)
Entry = ctk.CTkFrame(janela)
Entry.pack()
ctk.CTkLabel(Entry, text='R$', font=('arial', 16, 'bold')).pack(side=ctk.LEFT)
entrada = ctk.CTkEntry(Entry, width=80, validate='key', validatecommand=vcmd, font=('arial', 16, 'bold'))
entrada.pack(side=ctk.LEFT, pady=5, padx=5)
entrada.focus()

quadro_tela = ctk.CTkFrame(janela, width=100, height=30)
quadro_tela.pack(pady=15)
ctk.CTkLabel(janela, text='Escolha um ou mais produtos:', font=('arial', 18, 'bold')).pack(pady=10)

texto_qntd = [None] * 6
botao_menos = [None] * 6
for i in range(len(texto_qntd)):
    texto_qntd[i] = ctk.CTkLabel(quadro_tela, text='', justify='left', font=('arial', 16, 'bold'))    
    botao_menos[i] = ctk.CTkButton(quadro_tela, width=30, text='-1', command=lambda i=i: quantidade_produto(i+1, '-'), font=('arial', 12, 'bold'))

linha = ctk.CTkFrame(janela)
linha.pack(pady=5)
botoes = [None] * 6
for i in range(len(botoes)):
    botoes[i] = ctk.CTkButton(linha, font=('arial', 16), text=f'{produtos[f"Produto_{i+1}"]["nome"]}\nR$ {str(produtos[f"Produto_{i+1}"]["preco"]).replace(".",",")}\nEstoque: {produtos[f"Produto_{i+1}"]["estoque"]}',command=lambda i=i: quantidade_produto(i+1,'+'), width=150)
    botoes[i].grid(pady=5, padx=5)
    if i < 2:
       botoes[i].grid(row=0)
    elif i < 4:
        botoes[i].grid(row=1)
    else:
        botoes[i].grid(row=2)
    if i % 2 == 1:
        botoes[i].grid(column=1)
    elif i % 2 == 0:
        botoes[i].grid(column=0)

total = ctk.CTkLabel(janela, text='Total: R$ 0,00', font=('arial', 22, 'bold'))
total.pack()
finalizar = ctk.CTkButton(janela, text='FINALIZAR COMPRA', anchor='center', command=maquina_venda, width=350, height=50, font=('arial', 20, 'bold'))
finalizar.pack()

janela.mainloop()
