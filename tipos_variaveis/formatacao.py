nome = "Rodrigo"
sobrenome = "Takara"
nome_completo = "Rodrigo Takara"

# Upper
print(f"Upper: {nome_completo.upper()}")

# Lower
print(f"Lower: {nome_completo.lower()}")

# Count
print(f"Count 'R': {nome_completo.count('R')}")

# Find
print(f"Find 'g': {nome_completo.find('g')}")

# Replace
print(f"Replace 'R' with 'X': {nome_completo.replace('R', 'X')}")

# Join
print(f"Join with '-': {'-'.join(nome_completo)}")

# Split
print(f"Split: {nome_completo.split()}")

# Strip
print(f"Strip 'R': {nome_completo.strip('R')}")

# RStrip
print(f"RStrip 'a': {nome_completo.rstrip('a')}")

# Startswith
print(f"Startswith 'R': {nome_completo.startswith('R')}")

# In
print(f"Is 'Rpd' in nome_completo?: {'Rpd' in nome_completo}")

# NotIn
print(f"Is 'Rpd' not in nome_completo?: {'Rpd' not in nome_completo}")
