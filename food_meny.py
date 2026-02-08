# variables
total_outcome = 0
counter = 0
max_items = 5
# stored data
outcomes = {}
items_list = []
items_prices = {"1" : 3.00, "2" : 4.00, "3" : 2.00, "4" : 3.00, "5" : 4.00, "6" : 6.00, "7" : 3.00}
items = {"1" : "Beef burger", "2" : "Chicken fillet burger", "3" : "Fries", "4" : "2 pieces chicken", "5" : "4 pieces chicken", "6" : "6 pieces chicken", "7" : "5 chicken wings"}
# information pirnt
print("today's menu: \n 1. Beef burger - £3.00 \n 2. Chicken fillet burger - £4.00 \n 3. Fries - £2.00 \n 4. 2 pieces chicken - £3.00 \n 5. 4 pieces chicken - £4.00 \n 6. 6 pieces chicken - £6.00 \n 7. 5 chicken wings - £3.00 ")
 
# main code
while counter < max_items:
    counter = counter + 1
    item_input = str(input("what would you like to eat?: "))
    items_list.append(item_input)
    if counter == max_items:
        for x in items_list: 
            if x in items_prices:
                total_count = items_list.count(x) 
                vat = total_count * items_prices[x] / 100 * 20
                outcome = total_count * items_prices[x] + vat
                outcomes[x] = outcome
        for k, v in outcomes.items():
            print(str(items_list.count(k)) + " piece", "total price for", items[k], "with vat:", f"£{v:.2f}")
            total_outcome = total_outcome + v  
        print("total outcome with vat:", f"£{total_outcome:.2f}")