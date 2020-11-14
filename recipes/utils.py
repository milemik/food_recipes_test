def is_recipe_owner(data):
    recipe = data.get("recipe")
    if recipe.author == data.get("user"):
        return True
    return False
