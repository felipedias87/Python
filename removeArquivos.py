import os
import shutil
src = str(input("Digite o diretório de onde deseja deletar os arquivos:\n"))
trg = str(input("Digite o diretório para onde deseja mover os arquivos:\n"))
extensao = str(input("Qual a extensão de arquios que deseja remover?\n"))
ext = "." + extensao
ext.lstrip()
guardaNum = []
files = os.listdir(src)
for fname in files:
    extensao = os.path.splitext(fname)
    numArquivos = 0
    if extensao[1] == ext:
        numArquivos = numArquivos + 1
        guardaNum.append(numArquivos)
        print(fname," - Arquivo movido")
        shutil.copy2(os.path.join(src, fname), trg)
        arquivoTotal = src+fname
        os.remove(arquivoTotal)
print (f"\nO diretório ({src}) não contem arquivos com a extensão ({ext}) para apagar!! \n" if not guardaNum else f"Total de {len(guardaNum)} arquivos foram apagados e movidos para a pasta {trg}")
os.system("pause")
