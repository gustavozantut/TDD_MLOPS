class RomanNumbers:
    @staticmethod
    def get_number_from_roman(n):
        n=str(n)

        #checando se todos os caracteres são válidos e se nao ha mais de 3 caracteres repetidos em sequencia 
        caract_in_seq = 0
        ultimo_caract = ''
        for caract in list(n): 
            if caract not in ("I","V","X","L","C","D","M"):
                return("entrada inválida")
            if caract == ultimo_caract:
                caract_in_seq += 1
                if caract_in_seq >=3:
                    return("entrada inválida")
            else:
                caract_in_seq = 0
            ultimo_caract = caract

        #traduzindo cada caracter recebido
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        translated_list = [*map(roman_numerals.get, list(n))]

        if len(translated_list)==1:
                return(translated_list[0])

        sum=0
        for i in range (0, len(translated_list)):
            num = translated_list[i]
            if i+1 < len(translated_list) and translated_list[i+1] > num:
                sum -= num
            else: 
                sum += num
        return sum;
