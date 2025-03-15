class Pelicula:
    def __init__(self, nombre, generos, actores):
        self.nombre = nombre
        self.generos = generos
        self.actores = actores

    def __str__(self):
        generos_str = ", ".join(self.generos)
        actores_str = ", ".join(self.actores)
        return f"Nombre: {self.nombre}\nGéneros: {generos_str}\nActores: {actores_str}"

class CatalogoPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def mostrar_peliculas(self):
        if not self.peliculas:
            print("No hay películas en el catálogo.")
        else:
            for idx, pelicula in enumerate(self.peliculas, 1):
                print(f"Pelicula {idx}:\n{pelicula}\n")

def menu():
    catalogo = CatalogoPeliculas()

    while True:
        print("\n1. Agregar película")
        print("2. Mostrar películas")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la película: ")
            generos = input("Géneros (separados por comas): ").split(",")
            actores = input("Actores principales (separados por comas): ").split(",")
            nueva_pelicula = Pelicula(nombre, [g.strip() for g in generos], [a.strip() for a in actores])
            catalogo.agregar_pelicula(nueva_pelicula)
        elif opcion == "2":
            catalogo.mostrar_peliculas()
        elif opcion == "3":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
