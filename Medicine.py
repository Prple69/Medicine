import random

class RecipeMain:
    medication_list = ['Ибупрофен', 'Леводопа', 'Амоксициллин', 'Эритромицин', 'Тамоксифен','Варфарин']
    recipe_templates = []

    def __init__(self, disease, prescribed_medicine):
        self.disease = disease
        self.prescribed_medicine = prescribed_medicine
        self.generateRecipe()

    def generateRecipe(self):
        if self.prescribed_medicine not in self.medication_list:
            recipe_id = random.randint(1000, 9999)

            self.recipe = {
                "Болезнь": self.disease,
                "Лекарство": self.prescribed_medicine,
                "Идентификатор рецепта": recipe_id
            }

            self.medication_list.append(self.prescribed_medicine)
            self.recipe_templates.append(self.recipe)

            return self.recipe

    def getRecipe():
        for recipe in RecipeMain.recipe_templates:
            print(recipe, '\n')

# Пример использования класса
print('Список лекарств:\n', RecipeMain.medication_list, '\n') # Начальный список лекарств
rec1 = RecipeMain('Грип', 'Амоксициллин')
print('Первый рецепт:\n', RecipeMain.recipe_templates, '\n') # Не добавлен, т.к. лекарство - в списке
rec2 = RecipeMain('Грип', 'Ацикловир')
print('Второй рецепт:\n', RecipeMain.recipe_templates, '\n') # Добавлен, т.к. лекарства нет в списке
rec3 = RecipeMain('Волчанка', 'Азатиоприн')
print('Третий рецепт:\n', RecipeMain.recipe_templates, '\n') # Добавлен, т.к. лекарства нет в списке
rec4 = RecipeMain('Имунодифицит', 'Азатиоприн')
print('Четвертый рецепт:\n', RecipeMain.recipe_templates, '\n') # Не добавлен, т.к. лекарство - в списке
print('Список лекарств:\n', RecipeMain.medication_list, '\n') # Конечный список лекарств
RecipeMain.getRecipe() # Записанные рецепты