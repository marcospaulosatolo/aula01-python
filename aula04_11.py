horas_pedreiro = float(input("Digite as horas trabalhadas pelo pedreiro: "))
horas_pintor = float(input("Digite as horas trabahadas pelo pintor: "))
custo_pedreiro = horas_pedreiro * 10
custo_pintor = horas_pintor * 8
custo_total = custo_pedreiro + custo_pintor
print("Custo total da mão de obra: R$ ", custo_total)