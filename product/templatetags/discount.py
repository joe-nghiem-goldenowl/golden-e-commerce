from django import template

register = template.Library()

# @register.filter(name="calculate_discount")
def calculate_discount(price, discount):
    return price - price*discount/100

register.filter("calculate_discount", calculate_discount)
