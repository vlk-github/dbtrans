from googletrans import Translator as BaseTranslator
from googletrans import urls, utils
from googletrans.constants import DEFAULT_USER_AGENT, LANGUAGES, SPECIAL_CASES


class Translalor(BaseTranslator):
    def __init__(self, service_urls=None, user_agent=DEFAULT_USER_AGENT):
        BaseTranslator.__init__(self, service_urls, user_agent)
        pass

    def _translate(self, text:str, dest='en', src='auto'):
        if src != 'auto':
            if src not in LANGUAGES.keys() and src in SPECIAL_CASES.keys():
                src = SPECIAL_CASES[src]
            elif src not in LANGUAGES.keys():
                raise ValueError('invalid source language')

        if dest not in LANGUAGES.keys():
            if dest in SPECIAL_CASES.keys():
                dest = SPECIAL_CASES[dest]
            else:
                raise ValueError('invalid destination language')

        token = self.token_acquirer.do(text)
        params = utils.build_params(query=text, src=src, dest=dest,
                                    token=token)
        q = params.pop('q')
        url = urls.TRANSLATE.format(host=self._pick_service_url())
        c = ''
        for k in params:
            v = params[k]
            if type(v) == list:
                for lv in v:
                    c += k + '=' + lv + '&'
                pass
            elif type(v) != str:
                c += k + '=' + str(v) + '&'
            else:
                c += k + '=' + v + '&'

        url += '?' + c
        r = self.session.post(url, data={'q':q})

        data = utils.format_json(r.text)
        return data