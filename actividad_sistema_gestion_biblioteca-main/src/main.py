"""Archivo principal del Sistema de Gestión de Biblioteca"""
from data.biblioteca import libros, categorias
from utils.operaciones import (
    promedio_paginas,
    contar_libros,
    mostrar_disponibles,
    buscar_por_paginas,
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Llama a mostrar_disponibles()
        mostrar_disponibles(libros)
    elif opcion == "2":
        # Llama a buscar_por_paginas() con el límite de 400 páginas
        buscar_por_paginas(libros, 400)
    elif opcion == "3":
        # Llama contar_libros() y promedio_paginas()
        print(f"\nCantidad total de libros: {contar_libros(libros)}")
        print(f"Promedio de páginas: {promedio_paginas(libros):.2f}")
    elif opcion == "4":
        # Agregar categoría
        nueva = input("Ingresa el nombre de la nueva categoría: ")
        agregar_categoria(categorias, nueva)
    elif opcion == "5":
        print("¡Gracias por usar el sistema de biblioteca! Hasta luego.")
        break
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 5.")