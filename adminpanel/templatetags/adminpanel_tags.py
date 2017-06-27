from django import template


register = template.Library()


def truedate(value):
    return  str(value)