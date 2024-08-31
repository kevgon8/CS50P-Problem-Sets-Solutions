list = []
check_list = []

while True:
    try:
        item = input().upper()
        list.append(item)
    except EOFError:
        break
good_list = sorted(list)

for i in range(len(good_list)):
    nmbr_of_item = good_list.count(good_list[i])
    if good_list[i] not in check_list:
        check_list.append(good_list[i])
        print(f"{nmbr_of_item} {good_list[i]}")
    else:
        pass
