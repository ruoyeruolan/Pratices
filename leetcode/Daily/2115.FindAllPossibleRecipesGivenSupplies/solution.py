# -*- encoding: utf-8 -*-
# @Introduce  : 
# @File       : solution.py
# @Author     : ryrl
# @Email      : ryrl970311@gmail.com
# @Time       : 2025/03/21 18:33
# @Description: 

from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(
            self, 
            recipes: List[str], 
            ingredients: List[List[str]], 
            supplies: List[str]
    ) -> List[str]:
        
        avilable = set(supplies)

        recip_queue = deque(range(len(recipes)))
        created_recipes = []
        last_size = -1

        while len(avilable) > last_size:

            last_size = len(avilable)
            queue_size = len(recip_queue)

            while queue_size > 0:

                queue_size -= 1
                recipe_idx = recip_queue.popleft()

                if all(
                    ingredient in avilable for ingredient in ingredients[recipe_idx]
                ):
                    avilable.add(recipes[recipe_idx])
                    created_recipes.append(recipes[recipe_idx])
                else:
                    recip_queue.append(recipe_idx)
        return created_recipes

    def findAllRecipes_dfs(
            self, 
            recipes: List[str], 
            ingredients: List[List[str]], 
            supplies: List[str]
    ) -> List[str]:
        
        can_make = dict.fromkeys(supplies, True)
        recipes2idx = {recipe: idx for idx, recipe in enumerate(recipes)}  

        def check_recipe(recipe: str, visited:set):

            if can_make.get(recipe, False):
                return True
            
            if recipe not in recipes2idx or recipe in visited:
                return False
            
            visited.add(recipe)

            can_make[recipe] = all(
                check_recipe(ingredient, visited) 
                for ingredient in ingredients[recipes2idx[recipe]]
            )
            return can_make[recipe]
        return [recipe for recipe in recipes if check_recipe(recipe, set())]
