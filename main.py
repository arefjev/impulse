def get_random_secret():
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())


if __name__ == '__main__':
    get_random_secret()
