from googletrans import Translator

#translator = Translator(['translate.google.cn'])
#aa = translator.translate('안녕하세요.')

#print(aa)


def test(**connect_kwargs):
    print(connect_kwargs['a'])
    print(connect_kwargs)

config = {
    'aaa': {
        'a': 1,
        'b': 2,
        'c':3
    }
}

test(**config['aaa'])

