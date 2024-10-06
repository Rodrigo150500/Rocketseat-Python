nome = "Rodrigo"
sobrenome = "Takara"
nome_completo = "Rodrigo Takara"

# Upper
print("Function: upper()")
print(f"Upper: {nome_completo.upper()}")

# Lower
print("\nFunction: lower()")
print(f"Lower: {nome_completo.lower()}")

# Count
print("\nFunction: count()")
print(f"Count 'R': {nome_completo.count('R')}")

# Find
print("\nFunction: find()")
print(f"Find 'g': {nome_completo.find('g')}")

# Replace
print("\nFunction: replace()")
print(f"Replace 'R' with 'X': {nome_completo.replace('R', 'X')}")

# Join
print("\nFunction: join()")
print(f"Join with '-': {'-'.join(nome_completo)}")

# Split
print("\nFunction: split()")
print(f"Split: {nome_completo.split()}")

# Strip
print("\nFunction: strip()")
print(f"Strip 'R': {nome_completo.strip('R')}")

# RStrip
print("\nFunction: rstrip()")
print(f"RStrip 'a': {nome_completo.rstrip('a')}")

# Startswith
print("\nFunction: startswith()")
print(f"Startswith 'R': {nome_completo.startswith('R')}")

# In
print("\nFunction: in")
print(f"Is 'Rpd' in nome_completo?: {'Rpd' in nome_completo}")

# NotIn
print("\nFunction: not in")
print(f"Is 'Rpd' not in nome_completo?: {'Rpd' not in nome_completo}")
