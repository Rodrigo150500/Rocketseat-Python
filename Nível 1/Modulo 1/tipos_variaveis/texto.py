#Declaração
nome_completo = "Rodrigo Issao Takara"

nome_completo_aspas = """Rodrigo
Issao """

nome_completo_quebra = "Rodrigo\
    Issao"

nome = "Rodrigo"
sobrenome = "Takara"

# Formatação
print("Nome completo (1°Forma): ", nome_completo)
print("Nome completo (1°Forma): ", nome_completo)
print("Nome completo (3°Forma): " + "Rodrigo" + "Takara")
print("Nome completo (4°Forma): " + "Rodrigo", "Takara")
print("Nome completo (5°Forma): ", nome_completo_aspas)
print("Nome completo (6°Forma): ", nome_completo_quebra)
print("Nome completo (7°Forma): %s" %nome_completo)
print("Nome completo (8°Forma): %s %s" %(nome, sobrenome))
print(f"Nome completo (9°Forma): {nome_completo}")
print("Nome completo (10°Forma): {} {}".format(nome, sobrenome))



