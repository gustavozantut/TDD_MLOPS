class RomanNumbers:
    @staticmethod
    def get_number_from_roman(n):
        n=str(n)
        caract_valido = 0
        caract_in_seq = 0
        caract_anterior = ''
        for caract in list(n):
            if caract == caract_anterior:
                caract_in_seq += 1
                #MAXIMO 3 CARACTERES REPETIDOS
                if caract_in_seq >=3:
                    return("entrada inválida")
            else:
                caract_in_seq = 0
            #SOMENTE CARACTERES VALIDOS
            if caract not in ("I","V","X","L","C","D","M"):
                return("entrada inválida")
            caract_anterior = caract
        return(6);
