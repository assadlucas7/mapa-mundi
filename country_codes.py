from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Devolve o codigo de duas letras do pygal para um país, dado o seu nome."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #se o pais não foi encontrado, devolve None
    return None








