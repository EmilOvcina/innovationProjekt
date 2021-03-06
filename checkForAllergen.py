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


def checkForAllergy(ingredients, allergens):
    tmp = ingredients.lower().split(",")
    tmp[0] = tmp[0].split('-')[1]
    out = []
    if "gluten" in allergens:
        allergens += glutenIngredients
    if "laktose" in allergens:
        allergens += milkIngredients
    for i in range(len(tmp)):
        for j in range(len(allergens)):
            if re.search(allergens[j], tmp[i]):
                item = tmp[i]
                item = re.sub("[0-9]*", "", item)
                item = re.sub("%", "", item)
                item = re.sub("\(.*", "", item)
                item = re.sub(" ", "", item)
                item = re.sub("\.", "", item)
                item = item.capitalize()
                out.append(item)
    return out, (len(out) > 0)
