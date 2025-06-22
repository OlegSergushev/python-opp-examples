import re


class DomainException(Exception):
    pass


class Domain:
    __CORRECT_DOMAIN = r'\w+\.\w+'
    __CORRECT_URL = fr'^https?://(?P<domain>{__CORRECT_DOMAIN})$'
    __CORRECT_EMAIL = fr'\w+@(?P<domain>{__CORRECT_DOMAIN})'

    def __init__(self, domain):
        if not re.fullmatch(self.__CORRECT_DOMAIN, domain):
            raise DomainException('Недопустимый домен, url или email')
        self.domain = domain

    def __str__(self):
        return self.domain

    @classmethod
    def from_url(cls, url):
        url = re.match(cls.__CORRECT_URL, url)
        if not url:
            raise DomainException('Недопустимый домен, url или email')
        return cls(url.group('domain'))

    @classmethod
    def from_email(cls, email):
        email = re.match(cls.__CORRECT_EMAIL, email)
        if not email:
            raise DomainException('Недопустимый домен, url или email')
        return cls(email.group('domain'))


# ======================
# Example usage
# ======================
if __name__ == '__main__':
    emails = ['maksim@hotmail.com', 'pavel@hotmail.com', 'taisija@hotmail.com', 'elizar@mail.ru',
             'olimpiada@mail.ru', 'alla@hotmail.com', 'fomichevagap@gmail.com', 'evseevagalina@rambler.ru',
             'sigizmund@hotmail.com', 'maslovepifan@hotmail.com', 'vikentivasilev@hotmail.com',
             'ermiltrofimov@hotmail.com', 'subbotinnikon@hotmail.com', 'polikarpshirjaev@yahoo.com', 'lukinjakov@mail.ru',
             'czatsev@yandex.ru', 'termakov@rambler.ru', 'valeri@yahoo.com', 'filimon@yandex.ru',
             'kkuznetsova@mail.ru']

    for email in emails:
        domain = Domain.from_email(email)
        print(domain)
    
    print()
    
    urls = ['http://evseeva.info/', 'https:://ip.com/', 'https://www.ao.ru', 'https:///ip.ru', 'https://zao.',
        'https://.edu', 'http://oao.edu/', 'http://www.ip.com/', 'http://.org', 'http://abc.']

    for url in urls:
        try:
            domain = Domain.from_url(url)
        except DomainException as e:
            print(e)
