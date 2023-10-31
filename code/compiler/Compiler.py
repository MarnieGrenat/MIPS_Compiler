from code.compiler.dependencies.AssemblyFile import Assembly
from code.compiler.dependencies.HexFile import Hex
from dependencies.Debugger import logE, logW, logI, logD, logV
from os import listdir

commandsAssembly = ['or', 'and', 'sub', 'sltiu', 'lw', 'sw', 'beq', 'j']
commandsHex = []


def getListOfFiles(path:str) -> list:
    return listdir(path)

def generateHexadecimalIfNecessary() -> int:
    assemblyFileNames = getListOfFiles(r"../../assembly")
    hexFileNames = getListOfFiles(r"../../hexadecimal")

    count = 0
    for fileName in assemblyFileNames:
        if fileName not in hexFileNames:
            newHexFile = Assembly(fileName)
            newHexFile.generateHexadecimal()
            newHexFile.saveFile()
            count+=1

    return int(count)

def generateAssemblyIfNecessary() -> int:
    hexFileNames = getListOfFiles(r"../../hexadecimal")
    assemblyFileNames = getListOfFiles(r"../../assembly")
    count = 0

    for fileName in hexFileNames:
        if fileName not in assemblyFileNames:
            newAssemblyFile = Hex(fileName)
            newAssemblyFile.generateAssembly()
            newAssemblyFile.saveFile()
            count+=1
    return int(count)


def printLogInformationOnTerminal(countHexa:int, countAssembly:int) -> int:
	if	(not countAssembly and not countHexa):
		logW("Não foi gerado nenhum arquivo. Verifique se você adicionou o arquivo no local correto.")
		logW("Verifique se o arquivo está no formato correto ou no repositório adequado.")
	else:
		logI("Por favor, cheque as pastas para acessar os arquivos gerados!")
	if (countHexa):
		logI(f"{countHexa} arquivo(s) hexa gerado(s).")
	if (countAssembly):
		logI(f"{countAssembly} arquivo(s) assembly gerado(s).")
	return 0