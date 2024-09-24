cart = {'phone':2000,'lamp':2345.345,'doll':236.45,"sofa":7878788}
get_cart = {k[0]:round(val) for (k,val) in cart.items()}
print(get_cart)
cart2 = {k[0]:f"{val*.9:.2f}" if val>1000 else val for k,val in cart.items()}
print(cart2)
def funct_dis(k,v):
    if k=='cot' or k=='sofa':
        v=round(v*.29)
    return v
cart3 = {k:funct_dis(k,v) for k,v in cart.items()}
print(cart3)
