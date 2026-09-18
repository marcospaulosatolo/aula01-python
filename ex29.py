valor = float(input("Digite o valor da cmpra:"))
cliente_vip = input("Cliente VIP? ") == "sim"
if valor >=200 or cliente_vip:
    print("Frete grátis") 
else:
    print("Frete cobrado")      