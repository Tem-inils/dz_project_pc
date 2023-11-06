all_pr = {'Весь склад': {'Яблоко': 10, 'Апельсин': 10, 'Бананы': 10}}
cart = {}

while True:
    menu = input('1) Show all_pr\n2) Add to cart\n3) Remove from cart\n4) Exit\nChoose an option: ')

    if menu == '1':
        print("Содержимое склада:")
        for product, quantity in all_pr['Весь склад'].items():
            print(f"{product}: {quantity}")
    elif menu == '2':
        product = input("Введите товар для добавления в корзину: ")
        if product in all_pr['Весь склад']:
            quantity = int(input("Введите количество: "))
            if all_pr['Весь склад'][product] >= quantity:
                if product in cart:
                    cart[product] += quantity
                else:
                    cart[product] = quantity
                all_pr['Весь склад'][product] -= quantity
            else:
                print(f"Недостаточное количество товара '{product}' на складе.")
        else:
            print(f"Товар '{product}' отсутствует на складе.")
    elif menu == '3':
        product = input("Введите товар для удаления из корзины: ")
        if product in cart:
            quantity = int(input("Введите количество: "))
            if cart[product] >= quantity:
                cart[product] -= quantity
                if cart[product] == 0:
                    del cart[product]
                all_pr['Весь склад'][product] += quantity
            else:
                print(f"Недостаточное количество товара '{product}' в корзине.")
        else:
            print(f"Товар '{product}' отсутствует в корзине.")
    elif menu == '4':
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите корректную опцию.")
