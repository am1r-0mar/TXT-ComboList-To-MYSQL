import time
print("=====================================================");
print("TXT ComboList To MYSQL");
print("Ver: 2.5");
print("Discord: AugustoDoidin#2326");
print("Estado: Funcionando");
print("=====================================================");
db = input("Digite a Database do MYSQL: ")
tabela = input("Digite a Tabela que deve ser usada: ")
coluna = input("Digite a Coluna que deve ser usada: ")
sql = input("Digite o nome do arquivo SQL em que a conversão será salva: ")
print("=====================================================");
print("Digite as contas abaixo ou cole todo seu txt com quebra de linha.");
print("Para sair digite: sair");
print("=====================================================");
conta = ""
contador = 0
arq = open(sql + ".sql", "w")
while(conta != "sair"):
    conta = input()
    if(conta != "sair"):
        arq.write("INSERT INTO `" + db + "`.`"+ tabela + "` (`" + coluna + "`) VALUES ('" + conta +"');")
        arq.write("\n")
        contador = contador + 1
arq.close()
if(contador != 1):
    print(contador, "contas foram convertidas e salvas no arquivo: " + sql + ".sql")
else:
    print(contador, "conta foi convertida e salva no arquivo: " + sql + ".sql")
time.sleep(5)
    
