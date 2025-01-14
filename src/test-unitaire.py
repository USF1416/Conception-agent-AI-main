from questionnaire import calculateur_reponse_ia

# Tests unitaires
def test_calculateur_reponse_ia_sisr():
    responses = ["virtualisation", "réseau", "maintenance", "serveurs"]
    assert calculateur_reponse_ia(responses) == 'SISR est plus adaptée'

def test_calculateur_reponse_ia_slam():
    responses = ["programmation", "html", "css", "api"]
    assert calculateur_reponse_ia(responses) == 'SLAM est plus adaptée'

def test_calculateur_reponse_ia_equal():
    responses = ["virtualisation", "html"]
    assert calculateur_reponse_ia(responses) == 'Les deux options conviennent'
