from typing import List


class EmailParser:
    def __init__(self, email):
        self.email = email
        username, data = self.email.split("@")
        mail, domain = data.split(".")
        self.__username = username
        self.__mail = mail
        self.__domain = domain

    @property
    def username(self):
        return self.__username

    @property
    def mail(self):
        return self.__mail

    @property
    def domain(self):
        return self.__domain


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails: List = mails
        self.domains: List = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        parsed_email = EmailParser(email)

        return self.__is_name_valid(parsed_email.username) and self.__is_mail_valid(parsed_email.mail)\
               and self.__is_domain_valid(parsed_email.domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))





