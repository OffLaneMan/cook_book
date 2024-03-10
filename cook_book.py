import os


# from pprint import pprint
def cook_book_func():
    with open(
        os.path.join(os.path.dirname(__file__), "files", "cook_book.txt"),
        encoding="utf-8",
    ) as f:
        cook_book = {}
        for l in f:
            name = l.strip()
            count = int(f.readline().strip())
            ingredients = []
            for i in range(count):
                ingredient_name, quantity, measure = f.readline().split("|")
                ingredients.append(
                    {
                        "ingredient_name": ingredient_name.strip(),
                        "quantity": int(quantity.strip()),
                        "measure": measure.strip(),
                    }
                )
            f.readline()
            cook_book[name] = ingredients
    # pprint(cook_book)
    return cook_book


cook_book = cook_book_func()


def get_shop_list_by_dishes(dishes: list, person_count: int) -> list:
    shop_list = {}
    for dish in dishes:
        for i in cook_book[dish]:
            if not shop_list.get(i["ingredient_name"]):
                shop_list[i["ingredient_name"]] = {
                    "measure": i["measure"],
                    "quantity": i["quantity"] * person_count,
                }
                # shop_list[i["ingredient_name"]]["measure"] = i["measure"]
                # shop_list[i["ingredient_name"]]["quantity"] = i["quantity"] * person_count

            else:
                shop_list[i["ingredient_name"]]["quantity"] += (
                    i["quantity"] * person_count
                )

    # return pprint(shop_list)
    return shop_list


# get_shop_list_by_dishes(["Запеченный картофель", "Омлет", "Фахитос"], 5)
