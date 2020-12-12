import sallingUtils as salling
import checkForAllergen as check
import sys

ingredients = salling.find_ingredients(sys.argv[1])
allergens = sys.argv[2].split(",")
print(check.checkForAllergy(ingredients, allergens))