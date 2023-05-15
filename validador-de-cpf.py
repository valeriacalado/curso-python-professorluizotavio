
cpf = input("Digite o seu CPF (apenas números): ")\
    .replace(".", "")\
    .replace("-", "")

nove_digitos = cpf[:9]
contagem_regressiva1 = 10

calculo1 = 0
for digito1 in nove_digitos:
    calculo1 += int(digito1) * contagem_regressiva1
    contagem_regressiva1 -= 1
primeiro_digito = (calculo1 * 10) % 11
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0
    
dez_digitos = cpf[:10]
contagem_regressiva2 = 11

calculo2 = 0
for digito2 in dez_digitos:
    calculo2 += int(digito2) * contagem_regressiva2
    contagem_regressiva2 -= 1
segundo_digito = (calculo2 * 10) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0

cpf_calculado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
if cpf == cpf[0] * len(cpf):
    print("== CPF inválido ==")
elif cpf == cpf_calculado:
    print("== CPF válido! ==")
else:
    print("== CPF inválido! ==")