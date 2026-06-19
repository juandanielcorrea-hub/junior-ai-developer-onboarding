from pymongo import MongoClient

# 1. CONEXIÓN 
URI = "mongodb+srv://juandanielcorrea_db_user:<Contraseña>@cluster0.tnr6vax.mongodb.net/?appName=Cluster0"

# Conectamos al cliente
client = MongoClient(URI)

db = client['gamer_lobby_db']
coleccion_jugadores = db['Jugadores']

print("Conexión exitosa a la base de datos!\n")
print("-" * 40)

# C - CREATE (Insertar un nuevo documento)

nuevo_jugador = {
    "nombre_completo": "Erik",
    "correo": "erik@ejemplo.com",
    "nickname": "ErikPro",
    "plataforma_preferida": "PC",
    "juegos_activos": ["War Thunder", "ARK: Survival Evolved"]
}

# Insertamos en la BD
resultado_insert = coleccion_jugadores.insert_one(nuevo_jugador)
print(f"✅ JUGADOR CREADO: ID asignado -> {resultado_insert.inserted_id}")

# R - READ (Leer un documento)

jugador_encontrado = coleccion_jugadores.find_one({"nickname": "ErikPro"})
print(f"\n✅ JUGADOR ENCONTRADO:\n {jugador_encontrado}")

# U - UPDATE (Actualizar un documento)

filtro = {"nickname": "ErikPro"}
actualizacion = {"$push": {"juegos_activos": "Plague Inc."}}

coleccion_jugadores.update_one(filtro, actualizacion)
print("\n✅ JUGADOR ACTUALIZADO: Se agregó Plague Inc. a su lista.")

# Volvemos a leer para ver el cambio
print(coleccion_jugadores.find_one({"nickname": "ErikPro"}))

# D - DELETE (Eliminar un documento)

coleccion_jugadores.delete_one({"nickname": "ErikPro"})
print("\n✅ JUGADOR ELIMINADO de la base de datos.")