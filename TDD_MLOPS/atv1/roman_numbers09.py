class RomanNumbers:
    @staticmethod
    def get_number_from_roman(n):
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
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
        translated_caract = [*map(roman_numerals.get, list(n))]
        if len(list(n))==1:
            return(roman_numerals[n])
        else:
            if list(n)[0]>=list(n)[1]:
                return(translated_caract[0]+translated_caract[1])
            elif list(n)[0]<list(n)[1]:
                return(translated_caract[1]-translated_caract[0]);
