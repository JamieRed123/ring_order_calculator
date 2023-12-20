'''The purpose of this code is to determine how many of each sized rings to order when
ordering or stocking inventory for a store or ecommerce business.
Original ring size popularity data from:  https://www.teeda.com/blogs/articles/how-many-of-each-ring-size-should-i-stock
Note: This program always rounds to the nearest whole number of rings per size so 'amount' not always = to 'total_quantity'.'''

women_sizes = {
    '5': 0.08,
    '6': 0.2,
    '7': 0.35,
    '8': 0.2,
    '9': 0.12,
    '10': 0.05,
}
men_sizes = {
    '9': 0.25,
    '10': 0.25,
    '11': 0.25,
    '12': 0.15,
    '13': 0.1,
}

# User inputs
while True:
    try:
        amount = int(input('Enter total order quantity: '))
    except ValueError:
        print('Error: Invalid entry. Please try again.')
    else:
        break

while True:
    try:
        women_pct = float(input('Enter estimated percentage of women customers (ex. enter 50% as 0.5): '))
    except ValueError:
        print('Error: Invalid entry. Please try again.')
    else:
        break

# Data Entry Correction
if women_pct >= 1: # this assumes an entry of 1 = 100% and not 1%
    women_pct /= 100


# Calculate order number for each size
women_order = {}
for size in women_sizes:
    order_amount = round(women_sizes[size]*women_pct*amount)
    women_order[size] = order_amount
men_pct = 1 - women_pct
men_order = {}
for size in men_sizes:
    order_amount = round(men_sizes[size]*men_pct*amount)
    men_order[size] = order_amount


# Combine men and women orders
total_order = women_order.copy()
for size in men_order:
    if size in total_order:
        total_order[size] = total_order[size] + men_order[size]
    else:
        total_order[size] = men_order[size]


# Output
total_quantity = 0
for size in total_order:
    if total_order[size] > 0:
        print(f'Ring Size {size} --> Order Quantity: {total_order[size]}')
    total_quantity += total_order[size]
print(f'The total order quantity is {total_quantity}')