class RomanNumbers:
    @staticmethod
    def get_number_from_roman(n):
        n=str(n)
        caract_valido = 0
        for caract in list(n):
            if caract not in ("I","V","X","L","C","D","M"):
                return("entrada inválida")
        return("entrada válida");
