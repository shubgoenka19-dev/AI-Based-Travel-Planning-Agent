def apply_vit_discount(price, is_vit):
    if is_vit:
        return round(price * 0.85, 2)
    return price
