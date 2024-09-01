from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica


pessoa = Pessoa("Maria", "123456", "2023-01-01", True)
print("Informações da Pessoa:")
pessoa.imprimir_informacoes()
print()


pessoa_fisica = PessoaFisica("João", "789101", "2022-05-05", False, "2000-01-01", "123.456.789-00", "987654321")
print("Informações da Pessoa Física:")
pessoa_fisica.imprimir_informacoes()
print()


pessoa_juridica = PessoaJuridica("Empresa X", "112233", "2021-10-10", True, "2010-03-15", "12.345.678/0001-99")
print("Informações da Pessoa Jurídica:")
pessoa_juridica.imprimir_informacoes()
print()

# Alterando valores
print("Alterando valores...")
pessoa.nome = "Carlos"
pessoa_fisica.cpf = "321.654.987-01"
try:
    pessoa_juridica.cnpj = "123456789012345"  
except ValueError as e:
    print(f"Erro ao alterar CNPJ: {e}")
pessoa_juridica.cnpj = "98.765.432/0001-22"

print("\nInformações atualizadas da Pessoa:")
pessoa.imprimir_informacoes()
print()

print("Informações atualizadas da Pessoa Física:")
pessoa_fisica.imprimir_informacoes()
print()

print("Informações atualizadas da Pessoa Jurídica:")
pessoa_juridica.imprimir_informacoes()
