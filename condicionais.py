#if elif else

#Exemplo de IF

idade = int(input("Digite a idade: "))

if idade < 17:
    print("Você é menor de idade.")
elif idade <= 18:
    print("Você é maior de idade")
else:
    print("Você é idoso.")

if idade == 18:
    print("Vode tem 18 anos")

if idade != 10:
    print('Você não tem 10 anos')

mensagem = "Você pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"

print(mensagem)

