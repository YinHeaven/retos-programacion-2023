import random
import string

def generar_contrasena(numero=True, letras=False, simbolos=False, longitud=16):
    caracteres = ""
    
    if numero == True:
        caracteres += string.digits 
    
    if letras == True:
        caracteres += string.ascii_letters
    
    if simbolos == True:
        caracteres += string.punctuation
    
    # Verifica qsi hay al menos un tipo de carácter seleccionado
    if not caracteres:
        return "Error: Debes seleccionar al menos un tipo de carácter."
    
    longitud = random.randint(8, 16)
    if longitud < 8 or longitud > 16:
        return "Error: La longitud de la contraseña debe estar entre 8 y 16."
        
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

print(generar_contrasena(numero=True, letras=True, simbolos=True, longitud=12))
printe(generar_contrasena(numero=True, letras=False, simbolos=True, longitud=16))
