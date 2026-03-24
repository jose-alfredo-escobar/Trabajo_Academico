"""Calculadora básica en Python siguiendo PEP 8."""

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicar(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b


def dividir(a, b):
    """Devuelve la división de dos números. 
    Lanza un error si b es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b


def main():
    """Función principal para ejecutar la calculadora."""
    print("Calculadora básica")
    print("Operaciones disponibles: sumar, restar, multiplicar, dividir")

    operacion = input("Elige una operación: ").strip().lower()
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    if operacion == "sumar":
        resultado = sumar(numero1, numero2)
    elif operacion == "restar":
        resultado = restar(numero1, numero2)
    elif operacion == "multiplicar":
        resultado = multiplicar(numero1, numero2)
    elif operacion == "dividir":
        resultado = dividir(numero1, numero2)
    else:
        print("Operación no válida.")
        return

    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    main()
