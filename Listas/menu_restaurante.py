opciones = ["Encebollado", "Bowl de Carne", "Bowl de Pollo"]

print(opciones)

print(f"1. Añadir plato al menú.")
nuevo_plato = ["Bowl de Cerdo"]
menu_final = opciones + nuevo_plato
print(menu_final)
print(f"2. Buscar en el menú el indice de Bowl de Carne.")
print(menu_final.index("Bowl de Carne"))
print(f"3. Eliminar plato del menú.")
menu_final.remove("Encebollado")
print(f"4. Mostrar platos del menú.")
print(menu_final)



