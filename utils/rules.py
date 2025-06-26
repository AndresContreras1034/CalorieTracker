def regla_calorica(peso_actual, objetivo):
    """
    Define reglas nutricionales básicas según el objetivo del usuario.

    Parámetros:
    - peso_actual (float): Peso actual del usuario.
    - objetivo (str): 'bajar', 'subir' o 'mantener'.

    Retorna:
    - dict: Reglas con calorías objetivo y enfoque recomendado.
    """
    reglas = {
        "bajar": {
            "calorias_objetivo": 1800,
            "enfoque": "déficit calórico, proteína magra, actividad aeróbica"
        },
        "subir": {
            "calorias_objetivo": 2700,
            "enfoque": "superávit calórico, fuerza, proteína y carbohidratos"
        },
        "mantener": {
            "calorias_objetivo": 2200,
            "enfoque": "balance energético, dieta variada, actividad moderada"
        }
    }

    return reglas.get(objetivo.lower(), {
        "calorias_objetivo": None,
        "enfoque": "objetivo no definido"
    })
