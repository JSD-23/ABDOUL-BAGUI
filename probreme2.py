def maxProfit(prix):
    profit_max = 0
    prix_min = prix[0]

    for i in range(1, len(prix)):

        # on cherche le prix minimal courant
        if prix[i] < prix_min:
            prix_min = prix[i]

        # calcul du profit
        profit_obtenu = prix[i] - prix_min

        # si le profit courant est meilleur que notre profit_max alors il devient le profit max
        if profit_obtenu > profit_max:
            profit_max = profit_obtenu

    if profit_max == 0:
        return 0
    else:
        return profit_max
