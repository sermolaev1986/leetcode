# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=problem-list-v2&envId=topological-sort
from collections import defaultdict, deque
from typing import List


class Kahn:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_to_recipes = defaultdict(list)
        in_degree = defaultdict(int)

        for recipy, ingredients in zip(recipes, ingredients):
            for ingredient in ingredients:
                ingredient_to_recipes[ingredient].append(recipy)
            in_degree[recipy] = len(ingredients)

        result = []
        queue = deque(supplies)
        while queue:
            supply = queue.popleft()
            if supply in ingredient_to_recipes:
                for recipe in ingredient_to_recipes[supply]:
                    in_degree[recipe] -= 1
                    if in_degree[recipe] == 0:
                        result.append(recipe)
                        queue.append(recipe)

        return result

class DFS:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe_to_ingredients = defaultdict(list)
        for recipe, ingredients in zip(recipes, ingredients):
            recipe_to_ingredients[recipe] = ingredients
        supplies_set = set(supplies)
        visited = set()
        result = []

        def dfs(recipe):
            if recipe in visited:
                return
            visited.add(recipe)

            for ing in recipe_to_ingredients.get(recipe, []):
                if ing not in supplies_set and ing in recipe_to_ingredients:
                    dfs(ing)

            if all(ing in supplies_set for ing in recipe_to_ingredients.get(recipe, [])):
                supplies_set.add(recipe)
                result.append(recipe)

        for recipe in recipes:
            dfs(recipe)

        return result


if __name__ == '__main__':
    recipes = ["bread", "sandwich"]
    ingredients = [["yeast", "flour"], ["bread", "meat"]]
    supplies = ["yeast", "flour", "meat"]

    print(Kahn().findAllRecipes(recipes, ingredients, supplies))  # Output: ['bread', 'sandwich']
    print(DFS().findAllRecipes(recipes, ingredients, supplies))  # Output: ['bread', 'sandwich']