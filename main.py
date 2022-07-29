cook_book = {}
dishes_names = []
ingredients_list = []
dict_for_2nd_task = {}


def recipes(file_name):
    with open(file_name, encoding="utf_8") as file_obj:
        for i in file_obj:
            if i == "\n":
                continue
            else:
                dishes = i.strip()
                dishes_names.append(dishes)
                x = file_obj.readline()
                z = int(x.strip())
                ingredients_list = []
                for item in range(z):
                    ingredients, quantity, measure = file_obj.readline().strip().split(" | ")
                    ingr_dict = dict({"ingredient_name": ingredients, "quantity": quantity, "measure": measure})
                    ingredients_list.append(ingr_dict)
                    cook_book[dishes] = ingredients_list
    print(cook_book)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for key, value in cook_book.items():
            if dish == key:
                for ingredient in value:
                    ingredient['quantity'] = int(ingredient['quantity']) * person_count
                    ingredients_list.append(ingredient['ingredient_name'])
                    ingredient.pop('ingredient_name')
                    dict_for_2nd_task[ingredients_list[-1]] = ingredient
    print(dict_for_2nd_task)
    return dict_for_2nd_task


recipes('recipes.txt')
get_shop_list_by_dishes(dishes_names, 3)
