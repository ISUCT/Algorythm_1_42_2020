def number_of_product_orders(orders):
    length = max(orders)
    counters = [0] * length

    for order in orders:
        counters[order - 1] += 1

    return counters


def enough_products(products, orders):
    order_counters = number_of_product_orders(orders)
    output = []

    for i in range(len(products)):
        is_enough = products[i] >= order_counters[i]
        output.append(is_enough)

    return output


5


def get_input_data():
    length = int(input())
    array = list(map(int, input().split()))

    return array, length


def main():
    '''
    <<< 5
    <<< 1 50 3 4 3
    <<< 16
    <<< 1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5
    >>> main()
    yes
    no
    no
    no
    yes
    '''
    products, kinds_count = get_input_data()
    orders, orders_count = get_input_data()

    results = enough_products(products, orders)

    for result in results:
        print('no' if result else 'yes')


if __name__ == '__main__':
    main()
