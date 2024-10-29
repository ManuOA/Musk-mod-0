print('\033[32m')
print('''1...Se ha definido una clase relativa al inventario de un jet imaginario. 
También se ha creado una instancia de esta clase Jet. Imprime el primer atributo de la instancia.
''')
print('\033[37m')

# Definir la clase Jet y crear una instancia
class Jet:

    def __init__(self, name, country):
        self.name = name
        self.origin = country

# Crear una instancia de la clase Jet
jet0 = Jet('F16', 'USA')

# Imprimir el primer atributo de la instancia
print(jet0.name)
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''2...Usando la clase Jet, crea nuevas instancias con los siguientes nombres y origenes:
SU33: Russia
AJS37: Sweden
Mirage2000: France
F14: USA
Mig29: USSR
A10: USA
''')
print('\033[37m')

# Crear nuevas instancias de la clase Jet con los nombres y orígenes proporcionados
jet1 = Jet('SU33', 'Russia')
jet2 = Jet('AJS37', 'Sweden')
jet3 = Jet('Mirage2000', 'France')
jet4 = Jet('F14', 'USA')
jet5 = Jet('Mig29', 'USSR')
jet6 = Jet('A10', 'USA')

# Imprimir el nombre y origen de cada instancia
jets = [jet1, jet2, jet3, jet4, jet5, jet6]

for jet in jets:
    print(f'Name: {jet.name}, Origin: {jet.origin}')

input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''3...Anade otro atributo llamado 'cantidad' a la clase.
El usuario le dara valor pasando un nuevo
parametro por el constructor. A continuaci6on,
Crear 2 instancias para: F14 y Mirage2000 con
las cantidades 87 y 35.
''')
print('\033[37m')

# Definir la clase Jet con el nuevo atributo 'cantidad'
class Jet:

    def __init__(self, name, country, cantidad):
        self.name = name
        self.origin = country
        self.cantidad = cantidad

# Crear instancias de la clase Jet para F14 y Mirage2000 con las cantidades indicadas
jet_f14 = Jet('F14', 'USA', 87)
jet_mirage2000 = Jet('Mirage2000', 'France', 35)

# Imprimir el nombre, origen y cantidad de las dos instancias
print(f'Name: {jet_f14.name}, Origin: {jet_f14.origin}, Quantity: {jet_f14.cantidad}')
print(f'Name: {jet_mirage2000.name}, Origin: {jet_mirage2000.origin}, Quantity: {jet_mirage2000.cantidad}')
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''4...Dada la siguiente instancia y sus atributos, crea una clase que la instancie.
np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)
''')
print('\033[37m')

# Definir la clase Nobel con los atributos indicados
class Nobel:

    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

# Crear la instancia np2005 con los valores proporcionados
np2005 = Nobel("Peace", 2005, "Muhammad Yunus")

# Imprimir los atributos de la instancia
print(np2005.category, np2005.year, np2005.winner)
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''5...Crea una clase con el nombre de Estudiante, e inicialice atributos como:
el nombre, la edad y el grado mientras crea un objeto.
''')
print('\033[37m')

# Definir la clase Estudiante con los atributos indicados
class Estudiante:

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Carlos", 20, "Universitario")

# Imprimir los atributos del objeto
print(f"Nombre: {estudiante1.nombre}, Edad: {estudiante1.edad}, Grado: {estudiante1.grado}")
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''6...Escribe un programa para crear una clase vacia valida con el nombre de Estudiante, sin propiedades.
''')
print('\033[37m')

# Definir una clase vacía llamada Estudiante
class Estudiante:
    pass

# Crear una instancia de la clase Estudiante
estudiante1 = Estudiante()

# Comprobamos que la clase existe e instanciamos el objeto sin errores
print(f"Se ha creado un objeto de la clase: {type(estudiante1)}")
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''7...Añade un método publico en la clase Estudiante que calcule la media de una lista de notas y
actualice el valor del atributo grade.
A continuacion llama a la funcion en tu programa principal e imprime el valor de grade.
''')
print('\033[37m')

# Definir la clase Estudiante con un método para calcular la media de notas
class Estudiante:

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Método público para calcular la media de una lista de notas
    def calcular_media(self, notas):
        if notas:  # Comprobar si la variable(futura lista) no está vacía
            self.grado = sum(notas) / len(notas)  # Actualizamos el atributo "grado"
        else:
            self.grado = 0

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Carlos", 20, "Universitario")

# Lista de notas
notas = [85, 90, 78, 92, 88]

# Imprimir los atributos del objeto
print(f"Nombre: {estudiante1.nombre}, Edad: {estudiante1.edad}, Grado: {estudiante1.grado}")

# Llamar al método para calcular la media de las notas
estudiante1.calcular_media(notas)

# Imprimir el valor actualizado de grado (grado)
print(f"El estudiante {estudiante1.nombre} tiene una media de notas de: {estudiante1.grado}")
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''8...Añade a la clase anterior, un método estatico que dada una lista de notas y sus asignaturas, 
asociadas como diccionario, imprima aquellas asignaturas que han recibido una nota inferior a 5.
''')
print('\033[37m')

# Definir la clase Estudiante con un método estático para revisar notas por asignatura
class Estudiante:

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Método público para calcular la media de una lista de notas
    def calcular_media(self, notas):
        if notas:
            self.grado = sum(notas) / len(notas)
        else:
            self.grado = 0

    # Método estático para imprimir asignaturas con notas menores a 5
    @staticmethod
    def asignaturas_bajas(notas_por_asignatura):
        print("Asignaturas con nota inferior a 5:")
        for asignatura, nota in notas_por_asignatura.items():
            if nota < 5:
                print(f"{asignatura}: {nota}")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Carlos", 20, "Universitario")

# Lista de notas
notas = [85, 90, 78, 92, 88]

# Diccionario de asignaturas con sus notas
notas_por_asignatura = {
    "Matemáticas": 8,
    "Historia": 4,
    "Ciencias": 6,
    "Literatura": 3,
    "Educación Física": 7
}

# Imprimir los atributos del objeto
print(f"Nombre: {estudiante1.nombre}, Edad: {estudiante1.edad}, Grado: {estudiante1.grado}")

# Llamar al método para calcular la media de las notas
estudiante1.calcular_media(notas)

# Imprimir el valor actualizado de grado (grado)
print(f"El estudiante {estudiante1.nombre} tiene una media de notas de: {estudiante1.grado}")

# Llamar al método estático para mostrar asignaturas con notas inferiores a 5
Estudiante.asignaturas_bajas(notas_por_asignatura)
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''9...Añade un atributo de clase llamado escuela a la clase Estudiante y dale un valor predeterminado.
A continuacion, añade un método de clase que dado el nombre de otra escuela actualice el valor de ese atributo.
Llama a tu metodo en el programa principal y asegurate de que funciona.
''')
print('\033[37m')

# Definir la clase Estudiante con un atributo de clase y un método de clase
class Estudiante:

    # Atributo de clase
    escuela = "Escuela Primaria Internacional"

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Método público para calcular la media de una lista de notas
    def calcular_media(self, notas):
        if notas:
            self.grado = sum(notas) / len(notas)
        else:
            self.grado = 0

    # Método estático para imprimir asignaturas con notas menores a 5
    @staticmethod
    def asignaturas_bajas(notas_por_asignatura):
        print("Asignaturas con nota inferior a 5:")
        for asignatura, nota in notas_por_asignatura.items():
            if nota < 5:
                print(f"{asignatura}: {nota}")

    # Método de clase para actualizar el valor del atributo de clase "escuela"
    @classmethod
    def actualizar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Carlos", 20, "Universitario")

# Lista de notas
notas = [85, 90, 78, 92, 88]

# Diccionario de asignaturas con sus notas
notas_por_asignatura = {
    "Matemáticas": 8,
    "Historia": 4,
    "Ciencias": 6,
    "Literatura": 3,
    "Educación Física": 7
}

# Imprimir los atributos del objeto
print(f"Nombre: {estudiante1.nombre}, Edad: {estudiante1.edad}, Grado: {estudiante1.grado}")

# Llamar al método para calcular la media de las notas
estudiante1.calcular_media(notas)

# Imprimir el valor actualizado de grado (grado)
print(f"El estudiante {estudiante1.nombre} tiene una media de notas de: {estudiante1.grado}")

# Llamar al método estático para mostrar asignaturas con notas inferiores a 5
Estudiante.asignaturas_bajas(notas_por_asignatura)

# Llamar al método de clase para actualizar el valor de la escuela
Estudiante.actualizar_escuela("Escuela Secundaria Nacional")

# Imprimir el nuevo valor de escuela para comprobar que se ha actualizado
print(f"Escuela: {Estudiante.escuela}")
input('\nPulsa Enter para continuar...')


print('\033[32m')
print('''10...Añade un método privado en la clase anterior, que dado un diccionario mes-numero de asistencias:
devuelva 1 si algun mes tiene unaasistencia < 4, 
devuelva 2 si algun mes tiene alguna asistencia entre [4, 8)
o bien devuelva 3 en caso contrario.
Para probar el método privado, encapsulalo con una funci6n publica que devuelva su resultado.
''')
print('\033[37m')

# Definir la clase Estudiante con un atributo de clase y un método privado para evaluar asistencias
class Estudiante:

    # Atributo de clase
    escuela = "Escuela Primaria Internacional"

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    # Método público para calcular la media de una lista de notas
    def calcular_media(self, notas):
        if notas:
            self.grado = sum(notas) / len(notas)
        else:
            self.grado = 0

    # Método estático para imprimir asignaturas con notas menores a 5
    @staticmethod
    def asignaturas_bajas(notas_por_asignatura):
        print("Asignaturas con nota inferior a 5:")
        for asignatura, nota in notas_por_asignatura.items():
            if nota < 5:
                print(f"{asignatura}: {nota}")

    # Método de clase para actualizar el valor del atributo de clase "escuela"
    @classmethod
    def actualizar_escuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela

    # Método privado para evaluar las asistencias
    def __evaluar_asistencias(self, asistencias_por_mes):
        for mes, asistencias in asistencias_por_mes.items():
            if asistencias < 4:
                return 1
            elif 4 <= asistencias < 8:
                return 2
        return 3

    # Método público para encapsular el método privado y devolver su resultado
    def revisar_asistencias(self, asistencias_por_mes):
        return self.__evaluar_asistencias(asistencias_por_mes)

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Carlos", 20, "Universitario")

# Diccionario de asignaturas con sus notas
notas_por_asignatura = {
    "Matemáticas": 8,
    "Historia": 4,
    "Ciencias": 6,
    "Literatura": 3,
    "Educación Física": 7
}

# Diccionario de mes y número de asistencias
asistencias_por_mes = {
    "Enero": 3,
    "Febrero": 7,
    "Marzo": 9,
    "Abril": 8
}

# Imprimir los atributos del objeto
print(f"Nombre: {estudiante1.nombre}, Edad: {estudiante1.edad}, Grado: {estudiante1.grado}")

# Llamar al método para calcular la media de las notas
estudiante1.calcular_media(notas)

# Imprimir el valor actualizado de grado (grado)
print(f"El estudiante {estudiante1.nombre} tiene una media de notas de: {estudiante1.grado}")

# Llamar al método estático para mostrar asignaturas con notas inferiores a 5
Estudiante.asignaturas_bajas(notas_por_asignatura)

# Llamar al método de clase para actualizar el valor de la escuela
Estudiante.actualizar_escuela("Escuela Secundaria Nacional")

# Imprimir el nuevo valor de escuela para comprobar que se ha actualizado
print(f"Escuela: {Estudiante.escuela}")

# Llamar al método público que encapsula el privado y probar el resultado
resultado_asistencia = estudiante1.revisar_asistencias(asistencias_por_mes)

# Imprimir el resultado de la evaluación de asistencias
print(f"Resultado de la evaluación de asistencias: {resultado_asistencia}")
input('\nPulsa Enter para terminar...')