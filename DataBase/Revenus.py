import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


class Revenus:
    def __init__(self):
        a=0

    # Modèle exponentiel
    def calcul_exp(self,rev_fin, rev_init, seuil, dist):
        """
        Calcule le revenu fiscal moyen des foyers
        param rev_fin : revenu fiscal moyen limite quand la distance tant vers l'infini
        type rev_fin : float
        param rev_init : revenu fiscal moyen des familles habitant sur le lieu d'étude
        type rev_init : float
        param seuil : distance type (convergence plus ou moins rapide de la fonction exponentielle)
        type seuil : float
        param dist : tableau des distances dont on souhaite connaître le revenu fiscal moyen
        type dist : array
        return : tableau des revenus fiscaux moyens
        rtype : array
        """
        revenus = (rev_fin - rev_init) * (1 - np.exp(-dist / seuil)) + rev_init
        return revenus

    def estime_revenu(self,rev_moyen=17000, ecart_type=2000):
        """
        Calcule le revenu fiscal à l'aide d'une loi normale

        param rev_moyen : revenu fiscal moyen (moyenne de la loi normale)
        type rev_fin : float (par défaut l'étudiant est boursier le revenu moyen est de 17000€)
        param ecart_type : écart type de la loi normale
        type ecart_type : float (par défaut pour les boursiers l'écart type des revenus est de 2000€)

        return : revenu fiscal estimé selon les paramètres de la loi normale
        """

        revenu = (np.random.randn(1) * ecart_type + rev_moyen)[0]

        # Revenu maximal autorisé
        revenu_max = rev_moyen + 3 * ecart_type

        # Revenu minimal autorisé
        revenu_min = rev_moyen - 1.5 * ecart_type

        # Si le revenu généré est trop faible
        if revenu < revenu_min:
            revenu = revenu_min

        # Si le revenu généré est trop élevé
        elif revenu > revenu_max:
            revenu = revenu_max
        return revenu

    def plot(self, rev_fin, rev_init, seuil, abscisse):
        """
        Affichage de la courbe des revenus fiscaux moyens en fonction de la distance

        param rev_fin : revenu fiscal moyen limite quand la distance tant vers l'infini
        type rev_fin : float
        param rev_init : revenu fiscal moyen des familles habitant sur le lieu d'étude
        type rev_init : float
        param seuil : distance type (convergence plus ou moins rapide de la fonction exponentielle)
        type seuil : float
        param abscisse : tableau des distances dont on souhaite connaître le revenu fiscal moyen
        type abscisse : array

        return : tableau des revenus fiscaux moyens
        rtype : array
        """
        # Tableaux des abscisses (distances entre le domicile parental et le lieu d'étude)
        abscisse = np.linspace(0, 1000, 1000)

        # Revenu fiscal moyen lorsque l'étudiant  étudie à côté de chez ses parents
        rev_init = 23000

        # Revenu fiscal moyen lorsque la distance tend vers l'infini
        rev_fin = 40000

        # Paramètre qui fait converger plus ou moins vite la fonction exponentielle
        seuil = 300

        # Affichage de la courbe du revenu fiscal moyen en fonction de la distance
        ordonnee = calcul_exp(rev_fin, rev_init, seuil, abscisse)

        plt.figure()
        plt.plot(abscisse, ordonnee)
        plt.title("Revenu fiscal moyen par foyer en fonction de la distance")
        plt.xlabel("Distance en km")
        plt.ylabel("Revenu fiscal moyen par foyer en €")
        plt.grid()
        plt.show()
