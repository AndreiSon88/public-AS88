from pets import Cat
cats = [
        {
            "name": "Барон",
            "gender": "мальчик",
            "age": 2
        },

        {
            "name": "Сэм",
            "gender": "мальчик",
            "age": 2
        }

        ]
for cat_ in cats:
    find = Cat( name = cat_.get("name"),
                gender =cat_.get("gender"),
                age = cat_.get("age"))
    print(f"Кот {find.getName()}, пол {find.getGender()},возраст {find.getAge()} года")

