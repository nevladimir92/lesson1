price = 100
discount = 5 
price_with_disc = price - price *discount / 100


def discounted(price, discount, max_discaunt=50):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discaunt = abs(float(max_discaunt))
    if max_discaunt > 99:
        raise ValueError("Оч большая скидка")
    if discount > max_discaunt:
        price_with_disc = price
    else:
        price_with_disc = price - price *discount / 100
    return price_with_disc

discounted(100,50,100)