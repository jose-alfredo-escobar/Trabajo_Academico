import json

class ConjuntoEstatico:
    """Representa un conjunto estático (no cambia)."""

    def __init__(self, elementos):
        # Guardamos los elementos como tupla para que sean inmutables
        self.elementos = tuple(elementos)

    def mostrar(self):
        print("Conjunto estático:", self.elementos)


class ConjuntoDinamico:
    """Representa un conjunto dinámico (se puede modificar)."""

    def __init__(self):
        self.elementos = set()

    def agregar(self, elemento):
        self.elementos.add(elemento)

    def eliminar(self, elemento):
        self.elementos.discard(elemento)

    def mostrar(self):
        print("Conjunto dinámico:", self.elementos)


class ConjuntoPersistente:
    """Representa un conjunto persistente (se guarda en archivo)."""

    def __init__(self, archivo):
        self.archivo = archivo
        self.elementos = set()

    def agregar(self, elemento):
        self.elementos.add(elemento)

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(list(self.elementos), f)

    def cargar(self):
        with open(self.archivo, "r", encoding="utf-8") as f:
            self.elementos = set(json.load(f))

    def mostrar(self):
        print("Conjunto persistente:", self.elementos)


# Ejemplo de uso
if __name__ == "__main__":
    # Estático
    vocales = ConjuntoEstatico(["a", "e", "i", "o", "u"])
    vocales.mostrar()

    # Dinámico
    usuarios = ConjuntoDinamico()
    usuarios.agregar("José")
    usuarios.agregar("María")
    usuarios.mostrar()
    usuarios.eliminar("José")
    usuarios.mostrar()

    # Persistente
    datos = ConjuntoPersistente("usuarios.json")
    datos.agregar("Ana")
    datos.agregar("Luis")
    datos.guardar()
    datos.cargar()
    datos.mostrar()
