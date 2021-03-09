import csv


def organized_list(read_orders):
    order_list = {}
    products = set()
    days_of_week = set()

    for name, item, day in read_orders:
        products.add(item)
        days_of_week.add(day)
        if name not in order_list:
            order_list[name] = [
                {"product": item, "days_of_week": day}
            ]
        else:
            order_list[name].append(
                {"product": item, "days_of_week": day}
            )

    return order_list, products, days_of_week


def read_files_csv(path_to_file):
    with open(path_to_file) as file:
        reader_csv = csv.reader(file, delimiter=',', quotechar='"')
        orders_list = organized_list(reader_csv)
    return orders_list


def most_request(orders_list, client):
    requested = ""
    count = {}
    for order in orders_list:
        if order == client:
            if order not in count:
                count[order] = 1
            else:
                count[order] += 1
            if count[order] > count[requested]:
                requested = count[order]
    return request


def count_asked(order_list, client, food):
    count = 0
    for order in order_list[client]:
        if order == item:
            count += 1

    return count


never_ordered(order_list, client, list_of, term):
    dishes = set()
    client_orders = set(list_of)

    for order in orders[client]:
        dishes.add(order[term])
    return (set_list.difference(products))


def analyze_log(path_to_file):
    order_list, products, days = read_csv(path_to_file)

    with open("data/mkt_campaing.txt", mode="w") as file:
        file.write(f"{most_request(order_list, 'maria')}\n")
        file.write(f"{count_asked(order_list, 'arnaldo', 'hamburger')}\n")
        file.write(
            f"{never_ordered(order_list, 'joao', products, 'product')}\n")
        file.write(
            f"{never_ordered(order_list, 'joao', days, 'days_of_week')}")
