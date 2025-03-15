paises = {
    "México": {
        "nombre": "México",
        "ciudades_importantes": ["Ciudad de México", "Guadalajara", "Monterrey"],
        "coordenadas": [
            {"latitud": 19.4326, "longitud": -99.1332}, 
            {"latitud": 20.6597, "longitud": -103.3496}, 
            {"latitud": 25.6866, "longitud": -100.3161}   
        ]
    },
    "Japón": {
        "nombre": "Japón",
        "ciudades_importantes": ["Tokio", "Osaka", "Kioto"],
        "coordenadas": [
            {"latitud": 35.6895, "longitud": 139.6917}, 
            {"latitud": 34.6937, "longitud": 135.5023},  
            {"latitud": 35.0116, "longitud": 135.7681}   
        ]
    },
    "España": {
        "nombre": "España",
        "ciudades_importantes": ["Madrid", "Barcelona", "Valencia"],
        "coordenadas": [
            {"latitud": 40.4168, "longitud": -3.7038},   
            {"latitud": 41.3851, "longitud": 2.1734},    
            {"latitud": 39.4699, "longitud": -0.3763}   
        ]
    }
}


for pais, info in paises.items():
    print(f"País: {info['nombre']}")
    print("Ciudades importantes:", ", ".join(info["ciudades_importantes"]))
    print("Coordenadas:")
    for coord in info["coordenadas"]:
        print(f"  Latitud: {coord['latitud']}, Longitud: {coord['longitud']}")
    print()
