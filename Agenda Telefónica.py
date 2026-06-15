class Contacto:
    # Combinación explícita de tipos de datos primitivos (str, int, bool) como registro
    def __init__(self, nombre: str, telefono: str, correo: str, edad: int, favorito: bool):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.edad = edad
        self.favorito = favorito

    def mostrar(self):
        estado_favorito = "Sí" if self.favorito else "No"
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Edad: {self.edad} años")
        print(f"¿Contacto Favorito?: {estado_favorito}")
        print("-" * 30)


class AgendaTelefonica:
    def __init__(self):
        # VECTOR (Lista dinámica lineal de objetos/registros)
        self.contactos = []

        # MATRIZ (Estructura bidimensional estática solicitada en la Unidad I)
        self.matriz_categorias = [
            ["Personal-Alta", "Personal-Media", "Personal-Baja"],
            ["Laboral-Alta", "Laboral-Media", "Laboral-Baja"],
            ["Comercial-Alta", "Comercial-Media", "Comercial-Baja"]
        ]

    def agregar_contacto(self):
        print("\n--- REGISTRAR NUEVO CONTACTO ---")
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el teléfono: ")
        correo = input("Ingrese el correo: ")

        try:
            edad = int(input("Ingrese la edad (Número entero): "))
        except ValueError:
            print("Edad inválida. Se registrará 0 por defecto.")
            edad = 0

        fav_input = input("¿Marcar como contacto favorito? (S/N): ").strip().lower()
        favorito = True if fav_input == 's' else False

        contacto = Contacto(nombre, telefono, correo, edad, favorito)
        self.contactos.append(contacto)
        print("Contacto agregado correctamente.")

    def mostrar_contactos(self):
        if len(self.contactos) == 0:
            print("No existen contactos registrados.")
        else:
            print("\nLISTA DE CONTACTOS (REPORTERÍA)")
            for contacto in self.contactos:
                contacto.mostrar()

    def buscar_contacto(self):
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        encontrado = False

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_buscar.lower():
                print("\nCONTACTO ENCONTRADO")
                contacto.mostrar()
                encontrado = True

        if not encontrado:
            print("Contacto no encontrado.")

    def eliminar_contacto(self):
        nombre_eliminar = input("Ingrese el nombre a eliminar: ")

        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre_eliminar.lower():
                self.contactos.remove(contacto)
                print("Contacto eliminado correctamente.")
                return

        print("Contacto no encontrado.")

    def mostrar_matriz(self):
        print("\n=== MATRIZ DE CLASIFICACIÓN (ÁMBITO VS PRIORIDAD) ===")
        for fila in self.matriz_categorias:
            for elemento in fila:
                print(f"[{elemento}]", end="\t")
            print()

        # Bloque de ejecución principal


agenda = AgendaTelefonica()

while True:
    print("\n========== AGENDA TELEFÓNICA (UEA) ==========")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar matriz de clasificación")
    print("6. Salir")
    print("=============================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agenda.agregar_contacto()

    elif opcion == "2":
        agenda.mostrar_contactos()

    elif opcion == "3":
        agenda.buscar_contacto()

    elif opcion == "4":
        agenda.eliminar_contacto()

    elif opcion == "5":
        agenda.mostrar_matriz()

    elif opcion == "6":
        print("Programa finalizado correctamente.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")