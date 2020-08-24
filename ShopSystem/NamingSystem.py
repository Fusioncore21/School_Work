import string

def number_to_reference(order_number):
    """Take an order number and convert it into a unique order id."""
    if order_number >= 26 * 26 * 10000:
        print("Number too large! Cannot generate Product_ID.")
        return False
        # NB: You could also do the following instead:
        # raise ValueError('Number too large! Cannot generate Product_ID')
    high_part = order_number // 10000
    low_part = order_number % 10000
    letter1 = string.ascii_uppercase[high_part // 26]
    letter2 = string.ascii_uppercase[high_part % 26]
    return '#%s%s%04d' % (letter1, letter2, low_part)
print(number_to_reference(100000000))