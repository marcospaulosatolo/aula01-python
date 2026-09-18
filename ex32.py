produto = input("Produto:")
preco = float(input("Preço:"))
quantidade = int(input("Quantidade:"))
cliente_vip = input("Cliente vip?") == "sim"
total = preco * quantidade
print ("Produto:", produto)
print ("Total da compra:", total)
if total >= 200 or cliente_vip:
    print("Frete grátis")
else:
    print("Frete cobrado")    