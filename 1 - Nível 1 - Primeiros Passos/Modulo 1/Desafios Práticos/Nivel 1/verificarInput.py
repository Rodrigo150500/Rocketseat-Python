def verificarInput(msg, numeroInteiro=False):
    while True:
        try:
            if numeroInteiro:
                valor = int(input(msg))
                return valor
            else:
                valor = input(msg)
                
                while valor == "":
                    print("\nDigite um valor válido!")
                    valor = input(msg)
                    if valor!= "":
                        return valor  
                return valor

        except Exception as e:
            print("Digite um valor válido!")
