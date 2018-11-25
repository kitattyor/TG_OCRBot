import requests

class OCR_Supported_Languages:
    Arabic = 'ara'
    Bulgarian = 'bul'
    Chinese_Simplified = 'chs'
    Chinese_Traditional = 'cht'
    Croatian = 'hrv'
    Danish = 'dan'
    Dutch = 'dut'
    English = 'eng'
    Finnish = 'fin'
    French = 'fre'
    German = 'ger'
    Greek = 'gre'
    Hungarian = 'hun'
    Italian = 'ita'
    Japanese = 'jpn'
    Korean = 'kor'
    Norwegian = 'nor'
    Polish = 'pol'
    Portuguese = 'por'
    Russian = 'rus'
    Slovenian = 'slv'
    Spanish = 'spa'
    Swedish = 'swe'
    Turkish = 'tur'

    ExpandedLang = {
        Arabic:'Arabic',
        Bulgarian:'Bulgarian',
        Chinese_Simplified:'Chinese (Simplified)',
        Chinese_Traditional:'Chinese (Traditional)',
        Croatian:'Croatian',
        Danish:'Danish',
        Dutch:'Dutch',
        English:'English',
        Finnish:'Finnish',
        French:'French',
        German:'German',
        Greek:'Greek',
        Hungarian:'Hungarian',
        Italian:'Italian',
        Japanese:'Japanese',
        Korean:'Korean',
        Norwegian:'Norwegian',
        Polish:'Polish',
        Portuguese:'Portuguese',
        Russian:'Russian',
        Slovenian:'Slovenian',
        Spanish:'Spanish',
        Swedish:'Swedish',
        Turkish:'Turkish',
        'num':'Numbers'
    }

    SelectedLang = English
    

class OCRSpace(object):

    def __init__(self, api_key, language = OCR_Supported_Languages.English):
        """ ocr.space API wrapper
        :param api_key: API key string
        :param language: document language
        """
        print(language)
        self.api_key = api_key
        self.language = language
        self.payload = {
            'isOverlayRequired': False,
            'apikey': self.api_key,
            'language': self.language,
        }

    def ocr_space_url(self, url):
        """ OCR.space API request with remote file
        :param url: Image url
        :return: Result in JSON format.
        """
        data = self.payload
        data['url'] = url
        r = requests.post(
            'https://api.ocr.space/parse/image',
            data=data,
        )
        return r.json()