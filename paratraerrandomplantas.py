import random

nombres = ["Rosa", "Orquídea", "Cactus", "Lavanda", "Tomillo", "Bambú", "Girasol", "Suculenta", "Helecho", "Clavel"]
nombres_cientificos = ["Rosa sp.", "Orchidaceae", "Cactaceae", "Lavandula angustifolia", "Thymus vulgaris", 
                       "Bambusoideae", "Helianthus annuus", "Echeveria", "Pteridophyta", "Dianthus caryophyllus"]
luces = ["Pleno sol", "Luz indirecta", "Sombra", "Pleno sol", "Luz indirecta", "Sombra", "Pleno sol", "Luz indirecta", "Sombra", "Pleno sol"]
riegos = ["Moderado", "Escaso", "Abundante", "Moderado", "Escaso", "Abundante", "Moderado", "Escaso", "Abundante", "Moderado"]
suelos = ["Bien drenado", "Arena gruesa", "Arcilloso", "Bien drenado", "Arena gruesa", "Arcilloso", "Bien drenado", "Arena gruesa", "Arcilloso", "Bien drenado"]
ubicaciones = ["Jardín", "Interior", "Exterior", "Jardín", "Interior", "Exterior", "Jardín", "Interior", "Exterior", "Jardín"]
interior_exterior = ["Exterior", "Interior", "Exterior", "Exterior", "Interior", "Exterior", "Exterior", "Interior", "Exterior", "Exterior"]

registros_plantas = []

for _ in range(30):
    nombre = random.choice(nombres)
    nombre_cientifico = random.choice(nombres_cientificos)
    luz = random.choice(luces)
    riego = random.choice(riegos)
    suelo = random.choice(suelos)
    ubicacion = random.choice(ubicaciones)
    interior_ext = random.choice(interior_exterior)

    planta = {
        "nombre": nombre,
        "nombre_cientifico": nombre_cientifico,
        "luz": luz,
        "riego": riego,
        "suelo": suelo,
        "ubicacion": ubicacion,
        "interior_o_exterior": interior_ext
    }

    registros_plantas.append(planta)

# Imprimir los registros generados
for i, planta in enumerate(registros_plantas, start=1):
    print(f"Planta {i}: {planta}")