# ============================================================
# UNIRUY WYDEN
# Disciplina: Lógica de Programação
# Professor: Welliton Sousa da Cunha
#
# ATIVIDADE: Desafio Final - Cadastro Acadêmico
# Aluno: Breno Muller Lisboa Santos
# Data de entrega: 29/10/2026
#
# DESCRIÇÃO:
# Programa para cadastrar os dados de um aluno,
# calcular sua média e verificar sua aprovação.
# ============================================================

# 1. APRESENTAÇÃO DO PROGRAMA
print('=' * 50)
print('          SISTEMA DE CADASTRO ACADÊMICO')
print('=' * 50)

# 2. ENTRADA DE DADOS
nome = input('\nDigite o nome do aluno: ')
idade = int(input('Digite a idade do aluno: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# 3. CÁLCULO DA MÉDIA
media = (nota1 + nota2) / 2

# 4. VERIFICAÇÃO DA APROVAÇÃO
if media >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'

# 5. EXIBIÇÃO DOS RESULTADOS
print('\n' + '=' * 50)
print('              DADOS DO ALUNO')
print('=' * 50)
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Primeira nota: {nota1:.2f}')
print(f'Segunda nota: {nota2:.2f}')
print(f'Média final: {media:.2f}')
print(f'Situação: {situacao}')
print('=' * 50)
print('          CADASTRO FINALIZADO!')
print('=' * 50)

# 6. COMENTÁRIOS E OBSERVAÇÕES
# Observação 1:
# Observação 2:
# Observação 3:

# FIM DO PROGRAMA