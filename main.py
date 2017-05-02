from googletrans import Translator

translator = Translator(['translate.google.cn'])
aa = translator.translate('안녕하세요.')

print(aa)