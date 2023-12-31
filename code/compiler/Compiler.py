from compiler.dependencies.FileSystem import File as File
from compiler.dependencies.Debugger import logE, logW, logI, logD, logV
import os

def generateHexadecimalIfNecessary() -> int:
    ''' Assembly to MIPS'''
    assemblyDir = r"assembly"
    hexaDir = r"hexadecimal"
    assemblyFileNames = getListOfFiles(assemblyDir)
    hexFileNames = getListOfFiles(hexaDir)
    count = 0
    for AFileName in assemblyFileNames:
        if AFileName[:-4] not in hexFileNames[:-3]: #TODO retirar tipo de arquivo do nome
            newHexFile = File(AFileName, 'a2h')
            newHexFile.saveHexFile()
            count += 1
    return count

def generateAssemblyIfNecessary() -> int:
    ''' MIPS to Assembly '''
    assemblyDir = r"assembly"
    hexaDir = r"hexadecimal"
    assemblyFileNames = getListOfFiles(assemblyDir)
    hexFileNames = getListOfFiles(hexaDir)

    count = 0
    for hexFileName in hexFileNames:
        if hexFileName[:-3] not in assemblyFileNames[:-4]: #TODO retirar tipo de arquivo do nome
            newAssemblyFile = File(hexFileName, 'h2a')
            newAssemblyFile.saveAssemblyFile()
            count += 1
    return count

def getListOfFiles(path: str) -> list:
    return os.listdir(path)

def printLogInformationOnTerminal(countHexa: int, countAssembly: int) -> None:
    if (not countAssembly and not countHexa):
        logW(
            "Não foi gerado nenhum arquivo. Verifique se você adicionou o arquivo no local correto.")
        logW(
            "Verifique se o arquivo está no formato correto ou no repositório adequado.")
    else:
        logI("Por favor, cheque as pastas para acessar os arquivos gerados!")
    if (countHexa):
        logI(f"{countHexa} arquivo(s) hexa gerado(s).")
    if (countAssembly):
        logI(f"{countAssembly} arquivo(s) assembly gerado(s).")
    return None