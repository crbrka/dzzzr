from django import template


register = template.Library()


def show_element(value, arg): # show list element in template
    try:
        return value[arg]
    except IndexError:
        return 'нет кода'


def times(number):
    return range(number)


def div(value, arg):
    return int(value / arg)


def ins_code(value,arg):
    x=len(value)
    try:
        y=value[0]
        value.pop(0)

    except IndexError:
        return 'Ошибка Индекса'
    try:
        return y
    except IndexError:
        return 'Ошибка'



register.filter('ins_code',ins_code)
register.filter('div',div)
register.filter('times',times)
register.filter('show_element',show_element)
