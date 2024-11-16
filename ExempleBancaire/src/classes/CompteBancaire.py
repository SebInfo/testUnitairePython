class CompteBancaire:
    def __init__(self, montant_initial=0):
        self.solde = montant_initial

    def depot(self, montant):
        if montant <= 0:
            raise ValueError("Le montant doit être positif.")
        self.solde += montant

    def retrait(self, montant):
        if montant > self.balance:
            raise ValueError("Impossible de retirer cette somme les fonds sont insuffisants.")
        self.solde -= montant
