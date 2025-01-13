import pytest

def calculateur_reponse(tab_questions):
    """
    Classifie un texte vers SISR ou SLAM en se basant sur la présence de mots-clés.
    """
    sisr_keywords = [
        "os", "windows server", "unix", "linux", "powershell", "bash", "virtualisation", "docker", "kubernetes",
        "infrastructure as code", "ansible", "cloud", "aws", "azure", "gcp", "réseau", "vlan", "tcp/ip",
        "ipv4", "ipv6", "routeur", "commutateur", "switch", "firewall", "pfsense", "iptables", "dns", "dhcp",
        "ftp", "ssh", "vpn", "snmp", "monitoring", "sécurité réseau", "audit", "logs", "nas", "san", "high availability",
        "cluster", "raid", "backup", "drp", "active directory", "gestion des comptes", "iam", "wireshark", "analyse de paquets"
    ]

    slam_keywords = [
        "html", "css", "javascript", "typescript", "frontend", "backend", "node.js", "python", "framework web",
        "api", "rest", "graphql", "crud", "responsive design", "web design", "ui/ux", "react", "angular", "vue.js",
        "symfony", "laravel", "django", "cms", "wordpress", "joomla", "seo"
    ]

    sisr_score = 0
    slam_score = 0

    for question in tab_questions:
        for word in question.split():
            if word.lower() in sisr_keywords:
                sisr_score += 1
            elif word.lower() in slam_keywords:
                slam_score += 1

    if sisr_score > slam_score:
        return 'SISR est plus adaptée'
    elif sisr_score < slam_score:
        return 'SLAM est plus adaptée'
    else:
        return 'Les deux options conviennent'

def questionnaire():
    q1 = input("Aimez-vous travailler sur des serveurs et la virtualisation ? (Oui/Non) ").lower()
    q2 = input("Êtes-vous intéressé(e) par la maintenance et la sécurité réseau ? (Oui/Non) ").lower()
    q3 = input("Souhaitez-vous développer des applications ? (Oui/Non) ").lower()
    q4 = input("Avez-vous de l’appétence pour la programmation ? (Oui/Non) ").lower()

    tab_questions = [q1, q2, q3, q4]
    return calculateur_reponse(tab_questions)

if __name__ == "__main__":
    print(questionnaire())