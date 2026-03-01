# Programa para gestionar y mostrar las notas de varios alumnos. 
# Calcula la media de las notas, evalúa si aprueban o suspenden, 
# y determina la calificación cualitativa de cada alumno. 
# Adrián Yepez Villa, 01/03/2026. 
def calcular_media(nota1, nota2, nota3): 
    """ 
    Calcula la media aritmética de tres notas. 

    Args: 
        nota1 (float): Primera nota del alumno. 
        nota2 (float): Segunda nota del alumno. 
        nota3 (float): Tercera nota del alumno. 

    Returns: 
        float: La media de las tres notas. 
    """ 
    return (nota1 + nota2 + nota3) / 3 

 
def evaluar_aprobacion(media): 
    """ 
    Evalúa si la media obtenida corresponde a aprobado o suspenso. 
     
    Args: 
        media (float): Media de las notas del alumno. 

    Returns: 
        bool: True si aprobado (media >=5), False si suspendido. 
    """ 
    if media >= 5: 
        print("aprobado") 
        return True 

    else: 
        print("suspendido") 
        return False 

 
def calificacion_cualitativa(media): 
    """ 
    Determina la calificación cualitativa en función de la media. 

    Args: 
        media (float): Media de las notas del alumno. 

    Returns: 
        str: Calificación cualitativa ("Sobresaliente", "Notable", "Aprobado", "Suspenso"). 
    """ 
     # Condicionales reorganizados para que sea más eficiente. 
    if media >= 9: 
        return "Sobresaliente" 

    elif media >= 7: 
        return "Notable" 

    elif media >= 5: 
        return "Aprobado" 

    else: 
        return "Suspenso" 
    

def mostrar_alumno(nombre, nota1, nota2, nota3): 
    """ 
    Muestra en pantalla la información completa del alumno: nombre, notas, 
    media y calificación cualitativa. 

    Args: 
        nombre (str): Nombre completo del alumno. 
        nota1 (float): Primera nota. 
        nota2 (float): Segunda nota. 
        nota3 (float): Tercera nota. 
    """ 
    print("Alumno: " + nombre) 
    print("Nota 1: " + str(nota1)) 
    print("Nota 2: " + str(nota2)) 
    print("Nota 3: " + str(nota3)) 

     
    media = calcular_media(nota1, nota2, nota3) 

    print("Media: " + str(media)) 

     # Mostrar la calificación cualitativa basada en la media. 
    print(calificacion_cualitativa(media)) 

    print("----------------------") 


def main(): 
    """Función principal que ejecuta el programa con varios alumnos de ejemplo.""" 

    mostrar_alumno("Ana García", 8, 7, 9) 
    mostrar_alumno("Luis Pérez", 4, 5, 3) 
    mostrar_alumno("Marta Gómez", 6, 7, 5) 

 
main() 