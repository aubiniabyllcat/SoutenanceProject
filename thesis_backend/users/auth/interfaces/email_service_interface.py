from abc import ABC, abstractmethod

class EmailServiceInterface(ABC):
    @abstractmethod
    async def send_password_reset_email(self, email: str, reset_link: str):
        """
        Méthode abstraite pour envoyer un e-mail de réinitialisation de mot de passe.

        Args:
            email (str): L'adresse e-mail du destinataire.
            reset_link (str): Le lien de réinitialisation du mot de passe à inclure dans l'e-mail.

        Returns:
            dict: Un dictionnaire contenant un message indiquant si l'e-mail a été envoyé avec succès.
        """
        pass
