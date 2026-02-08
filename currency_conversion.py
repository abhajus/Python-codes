fee = "None"
pound_input = float(input("input amount of gbp: "))
currency_rates = {"1" : 1.40, "2" : 1.14, "3" : 4.77, "4" : 151.05, "5" : 5.68}
rate_prefix = {"1" : "Usd", "2" : "Eur", "3" : "Brl", "4" : "Jpy", "5" : "Try"}
# information pirnt
print("Currency conversion: \n 1. American Dollars (USD) \n 2. Euros (EUR) \n 3. Brazilian Real (BRL) \n 4. Japanese Yen (JPY) \n 5. Turkish Lira (TRY)")
choose_currency = str(input("input number 1 to 5: "))
for k, v in currency_rates.items():
    if k == choose_currency:
        converted = f"{pound_input * v:.2f}"
        print("Converted amount:",converted, rate_prefix.get(k))
        if pound_input <= 300:
            fee = pound_input / 100 * 3.5
        elif pound_input > 300 and pound_input <= 750:
            fee = pound_input / 100 * 3.0
        elif pound_input > 750 and pound_input <= 1000:
            fee = pound_input / 100 * 2.5
        elif pound_input > 1000 and pound_input <= 2000:
            fee = pound_input / 100 * 2.0
        else:
            fee = pound_input / 100 * 1.5
        fee_ = f"{fee:.2f}"
        print("Transaction Fee: ", fee_)
        is_employee = str(input("Is customer a staff member? true/false "))
        if is_employee == "True" or is_employee == "true":
            print("Total transaction amount for conversion with 5% discount applied: ", pound_input - (pound_input / 100 * 5) + float(fee_), "GBP") 
        else:
            print("Discount was not applied because the member is not a staff member")
            print("Total transaction amount to pay for conversion:", float(fee_) + pound_input)