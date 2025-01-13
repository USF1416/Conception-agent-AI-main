from questionnaire import calculateur_reponse

# Tests unitaires
def test_calculateur_reponse_sisr():
    responses = ["virtualisation", "réseau", "maintenance", "serveurs"]
    assert calculateur_reponse(responses) == 'SISR est plus adaptée'

def test_calculateur_reponse_slam():
    responses = ["programmation", "html", "css", "api"]
    assert calculateur_reponse(responses) == 'SLAM est plus adaptée'

def test_calculateur_reponse_equal():
    responses = ["virtualisation", "html"]
    assert calculateur_reponse(responses) == 'Les deux options conviennent'