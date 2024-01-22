"""
Melhor biblioteca para gerar dados falsos de forma simples
Names:
    fake.name() - Gera nome de pessoa aleatório
    fake.first_name() - Gera primeiros nomes
    fake.last_name() - Gera sobrenomes
    fake.name_male() - Nomes masculinos
    fake.name_female() - Nomes femininos


textos e palavras:
    fake.text() - Gera texto aleatório
    fake.word() - Gera uma palavara aleatória
    fake.words(num) - Gera num palavras aletórias

Outros dados:
    fake.address() - Gera endereço aleatório
    fake.job() - Emprego falso
    fake.phone_number() - Retorna número falso
    fake.email() - Gera email aleatório
    fake.safe_email() - Gera email aleatório confiavel
    fake.company_email() - Gera email de empresa aleatória
    fake.date_of_birth() - Gera data de aniversário falsa
    
    
fake.currency() - Gera uma tupla com abbr e nome de moeda aleatória 
fake.currency_name - Gera nome de moeda aleatória
fake.currency_code - Gera abbr de moeda aleatória



"""
import faker, locale
print(locale.getlocale())

fk:faker.Faker = faker.Faker(locale="pt_BR")

print(fk.name())
print(fk.first_name())
print(fk.last_name())
print(fk.address())
print(fk.phone_number())
print(fk.currency())
print(fk.currency_name())
print(fk.currency_code())
print(fk.name_male())
print(fk.words(6))
print(fk.date_of_birth())
print(fk.safe_email())