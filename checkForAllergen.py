import re

milkIngredients = [
    "mælk",
    "smør",
    "ost",
    "yoghurt",
    "ymer",
    "ylette",
    "fløde",
    "milkshake",
    "bagermargarine",
    "margarine",
    "minarine",
]

glutenIngredients = [
    "hvede",
    "rug",
    "byg",
    "bulgur",
    "couscous",
    "emmer",
    "mannagryn",
    "semolina",
    "semulje",
    "spelt"
]

nutIngredients = [
    "mandel",
    "hasselnød",
    "valnød",
    "cashewnød",
    "pekannød",
    "paranød",
    "pistacienød",
    "queenslandnød",
    "macadamianød"
]

def checkForMilkAllergy(ingredients):
    tmp = ingredients.lower().split(",")
    tmp[0] = tmp[0].split()[-1]
    out = []
    for i in range(len(tmp)):
        for j in range(len(milkIngredients)):
            if re.search(milkIngredients[j], tmp[i]):
                out.append(tmp[i])
    return (out, (len(out) > 0))

def checkForGlutenAllergy(ingredients):
    tmp = ingredients.lower().split(",")
    tmp[0] = tmp[0].split()[-1]
    out = []
    for i in range(len(tmp)):
        for j in range(len(glutenIngredients)):
            if re.search(glutenIngredients[j], tmp[i]):
                out.append(tmp[i])
    return (out, (len(out) > 0))

def checkForNutAllergy(ingredients):
    tmp = ingredients.lower().split(",")
    tmp[0] = tmp[0].split()[-1]
    out = []
    for i in range(len(tmp)):
        for j in range(len(nutIngredients)):
            if re.search(nutIngredients[j], tmp[i]):
                out.append(tmp[i])
    return (out, (len(out) > 0))

def checkForAllergy(ingredients, allergens):
    tmp = ingredients.lower().split(",")
    tmp[0] = tmp[0].split('-')[1]
    out = []
    for i in range(len(tmp)):
        for j in range(len(allergens)):
            if re.search(allergens[j], tmp[i]):
                out.append(tmp[i])
    return (out, (len(out) > 0))