def get_columns_count(codes, divider):  # считаем кол-во колонок
    codes_count = len(codes)
    delitel = 1
    counter = 1
    while not codes_count < delitel*divider:
        delitel *= divider
        counter += 1
    return counter


def get_ranges(codes, divider):  # считаем кол-во диапазонов
    codes_count = len(codes)
    delitel = counter = 1
    ranges = [range(1)]
    while not codes_count < delitel*divider:
        delitel *= divider
        counter += 1
        ranges.append(range(delitel))
    return ranges


def get_rows_count(codes, divider):
    codes_count = len(codes)
    row_count = 1
    while True:
        row_count *= divider
        if row_count > codes_count:
            break
    row_count /= divider
    return int(row_count)
