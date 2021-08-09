class Funcionario:
    """Essa classe representa um funcionário."""

    def __init__(self, nome: str, sobrenome: str, sal_anual: float):
        """
        -> Aceita o nome, sobrenome e o salário anual do funcionário
        e inicializa os atributos da classe.

        :param nome: Nome do funcionário.
        :param sobrenome: Sobrenome do funcionário.
        :param sal_anual: Valor real do salário anual do funcionário.
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.sal_anual = float(sal_anual)
        # Atributos sem parâmetros.
        self.nome_completo = f'{nome} {sobrenome}'.title()

    def dar_aumento(self, valor: float = 5000) -> None:
        """
        -> Aumenta o valor do salário anual do funcionário
        com o valor especificado. Aumenta 5000 por padrão.

        :param valor: (Default=5000) Valor real do aumento.
        """
        self.sal_anual += valor

    def mostrar_sal_anual(self, formatar: bool = False):
        """
        -> Mostra o salário anual do funcionário.
        Se o valor formatar for passado, formata o
        salário com R$, vírgula no lugar do ponto e
        duas casas decimais.
        Se não, mostra o valor normalmente.

        :param formatar: (Opcional) Formata o salário
        anual com R$, vírgula no lugar do ponto e duas
        casas decimais.
        """
        if formatar:
            sal_formatado = f'R${self.sal_anual:.2f}'.replace('.', ',')
        else:
            sal_formatado = f'{self.sal_anual}'

        print(f'Salário anual de {self.nome_completo}: {sal_formatado}')
