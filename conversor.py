recibido = int(input("Introduzca un numero: "))


def unidad(num_unidad):
    if num_unidad is 0:
        return ""
    if num_unidad is 9:
        return "nueve"
    if num_unidad is 8:
        return "ocho"
    if num_unidad is 7:
        return "siete"
    if num_unidad is 6:
        return "seis"
    if num_unidad is 5:
        return "cinco"
    if num_unidad is 4:
        return "cuatro"
    if num_unidad is 3:
        return "tres"
    if num_unidad is 2:
        return "dos"
    if num_unidad is 1:
        return "uno"


def decena(num_decena, num_unidad):
    numero = ""
    if num_decena is 0:
        pass
    if num_decena is 9:
        numero = "noventa"
    if num_decena is 8:
        numero = "ochenta"
    if num_decena is 7:
        numero = "setenta"
    if num_decena is 6:
        numero = "sesenta"
    if num_decena is 5:
        numero = "cincuenta"
    if num_decena is 4:
        numero = "cuarenta"
    if num_decena is 3:
        numero = "treinta"
    if num_decena is 2:
        numero = "veinte"
    if num_decena is 1 and num_unidad is 5:
        return "quince"
    if num_decena is 1 and num_unidad is 4:
        return "catorce"
    if num_decena is 1 and num_unidad is 3:
        return "trece"
    if num_decena is 1 and num_unidad is 2:
        return "doce"
    if num_decena is 1 and num_unidad is 1:
        return "once"
    if num_decena is 1 and num_unidad is 0:
        return "diez"
    if num_unidad > 1 and num_decena is not 0:
        return numero + " y " + unidad(num_unidad)
    return numero + " " + unidad(num_unidad)


def centena(num_centena, num_decena, num_unidad):
    numero = ""
    if num_centena is 0:
        pass
    if num_centena is 9:
        numero = "novecientos"
    if num_centena is 8:
        numero = "ochocientos"
    if num_centena is 7:
        numero = "setecientos"
    if num_centena is 6:
        numero = "seiscientos"
    if num_centena is 5:
        numero = "quinientos"
    if num_centena is 4:
        numero = "cuatrocientos"
    if num_centena is 3:
        numero = "trescientos"
    if num_centena is 2:
        numero = "doscientos"
    if num_centena is 1 and num_decena is 0 and num_unidad is 0:
        numero = "cien"
    elif num_centena is 1:
        numero = "ciento"
    return numero + " " + decena(num_decena, num_unidad)


def conversor(numero_completo):
    numero = ""
    if numero_completo > 999999999999999999:
        print("un trillon o mas (no se lee arriba de eso)")
    if numero_completo > 999999999999999:
        numero = numero + " " + centena(int((numero_completo % 1000000000000000000) / 100000000000000000),
                                        int((numero_completo % 100000000000000000) / 10000000000000000),
                                        int((numero_completo % 10000000000000000) / 1000000000000000)) + " mil"
    if numero_completo > 999999999999:
        numero = numero + " " + centena(int((numero_completo % 1000000000000000) / 100000000000000),
                                        int((numero_completo % 100000000000000) / 10000000000000),
                                        int((numero_completo % 10000000000000) / 1000000000000)) + " Billones"
    if numero_completo > 999999999:
        numero = numero + " " + centena(int((numero_completo % 1000000000000) / 100000000000),
                                        int((numero_completo % 100000000000) / 10000000000),
                                        int((numero_completo % 10000000000) / 1000000000)) + " mil"
    if numero_completo > 999999:
        numero = numero + " " + centena(int((numero_completo % 1000000000) / 100000000),
                                        int((numero_completo % 100000000) / 10000000),
                                        int((numero_completo % 10000000) / 1000000)) + " Millones"
    if numero_completo > 999:
        numero = numero + " " + centena(int((numero_completo % 1000000) / 100000),
                                        int((numero_completo % 100000) / 10000),
                                        int((numero_completo % 10000) / 1000)) + " mil"

    numero = numero + " " + centena(int((numero_completo % 1000) / 100),
                                    int((numero_completo % 100) / 10),
                                    int((numero_completo % 10) / 1))
    print(numero)


def cifrar(numero_completo):
    contador = 0
    cifra = ""
    while numero_completo > 0:
        if contador is 3 or contador is 9 or contador is 15:
            cifra = "," + cifra
        if contador is 6 or contador is 12 or contador is 18:
            cifra = "'" + cifra
        cifra = str(numero_completo % 10) + cifra
        contador += 1
        numero_completo = int(numero_completo / 10)
    print(cifra)


cifrar(recibido)
conversor(recibido)
