class Usuario:
    """
    Classe que representa um usuário com nome, email e senha.
    """
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    @property
    def nome(self):
        """Retorna o nome do usuário."""
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """Define um novo nome para o usuário."""
        self.__nome = nome

    @property
    def email(self):
        """Retorna o email do usuário."""
        return self.__email

    @email.setter
    def email(self, email):
        """Define um novo email para o usuário."""
        self.__email = email

    @property
    def senha(self):
        """Retorna a senha do usuário."""
        return self.__senha

    @senha.setter
    def senha(self, senha):
        """Define uma nova senha para o usuário."""
        self.__senha = senha
