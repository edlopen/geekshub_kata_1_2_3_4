password = "contraseña"

user_password = input("Introduce la contraseña: ").lower()

if password == user_password:
    print("El password es correcto")
else:
    print("El password no coincide")
