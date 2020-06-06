from translate import Translator
#Übersetzer
class Übersetzer():
    def übersetzen_deutsch_in_englisch(self,wort:str):
        return Translator(from_lang="de",to_lang="en").translate(wort)
    def übersetzen_englisch_in_deutsch(self,wort:str):
        return Translator(from_lang="en",to_lang="de").translate(wort)