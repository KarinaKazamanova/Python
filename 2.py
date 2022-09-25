# Напишите программу для проверки истинности утверждения ¬(X ⋁(или) Y ⋁ Z) = ¬X ⋀ (и) ¬Y ⋀ ¬Z для всех значений предикат.

for a in range (2):
    for b in range (2):
        for c in range (2):
            print(f"for X = {a}, Y = {b} and Z = {c} ¬(X ⋁(или) Y ⋁ Z) = ¬X ⋀ (и) ¬Y ⋀ ¬Z {not (a or b or c)==(not a and not b and not c)}")