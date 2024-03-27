import random

aleatorio_pais = random.randint(1,3)
aleatorio_zona = random.randint(1,3)
aleatorio_velocidad = random.randint(10,120)

print (f"aleatorio pais {aleatorio_pais}")
print (f"aleatorio zona {aleatorio_zona}")
print (f"aleatorio velocidad {aleatorio_velocidad}")

if aleatorio_pais == 1 and aleatorio_zona == 1 and aleatorio_velocidad>=10 and aleatorio_velocidad<=50:
    print(f"Ecuador, Zona Urbana, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 1 and aleatorio_zona == 1 and aleatorio_velocidad<=9 or aleatorio_velocidad>=51:
    print(f"Ecuador, Zona Urbana, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 1 and aleatorio_zona == 2 and aleatorio_velocidad>=51 and aleatorio_velocidad<=70:
    print(f"Ecuador, Zona Rural, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 1 and aleatorio_zona == 2 and aleatorio_velocidad<=50 or aleatorio_velocidad>=71:
    print(f"Ecuador, Zona Rural, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 1 and aleatorio_zona == 3 and aleatorio_velocidad>=71 and aleatorio_velocidad<=90:
    print(f"Ecuador, Zona Perimetral, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 1 and aleatorio_zona == 3 and aleatorio_velocidad<=70 or aleatorio_velocidad>=91:
    print(f"Ecuador, Zona Perimetral, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 2 and aleatorio_zona == 1 and aleatorio_velocidad>=10 and aleatorio_velocidad<=30:
    print(f"Colombia, Zona Urbana, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 2 and aleatorio_zona == 1 and aleatorio_velocidad<=9 or aleatorio_velocidad>=31:
    print(f"Colombia, Zona Urbana, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 2 and aleatorio_zona == 2 and aleatorio_velocidad>=31 and aleatorio_velocidad<=80:
    print(f"Colombia, Zona Rural, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 2 and aleatorio_zona == 2 and aleatorio_velocidad<=30 or aleatorio_velocidad>=81:
    print(f"Colombia, Zona Rural, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 2 and aleatorio_zona == 3 and aleatorio_velocidad>=81 and aleatorio_velocidad<=100:
    print(f"Colombia, Zona Perimetral, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 2 and aleatorio_zona == 3 and aleatorio_velocidad<=80 or aleatorio_velocidad>=101:
    print(f"Colombia, Zona Perimetral, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 3 and aleatorio_zona == 1 and aleatorio_velocidad>=10 and aleatorio_velocidad<=30:
    print(f"Peru, Zona Urbana, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 3 and aleatorio_zona == 1 and aleatorio_velocidad<=9 or aleatorio_velocidad>=31:
    print(f"Peru, Zona Urbana, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 3 and aleatorio_zona == 2 and aleatorio_velocidad>=31 and aleatorio_velocidad<=80:
    print(f"Peru, Zona Rural, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 3 and aleatorio_zona == 2 and aleatorio_velocidad<=30 or aleatorio_velocidad>=81:
    print(f"Peru, Zona Rural, limite de velocidad inadecuado {aleatorio_velocidad}")
elif aleatorio_pais == 3 and aleatorio_zona == 3 and aleatorio_velocidad>=81 and aleatorio_velocidad<=100:
    print(f"Peru, Zona Perimetral, limite de velocidad adecuado {aleatorio_velocidad}")
elif aleatorio_pais == 3 and aleatorio_zona == 3 and aleatorio_velocidad<=80 or aleatorio_velocidad>=101:
    print(f"Peru, Zona Perimetral, limite de velocidad inadecuado {aleatorio_velocidad}")