import pymorphy3
from pyphrasy.inflect import PhraseInflector


class Inflect:

    def __init__(self, court):
        self.court = court
        self.inflect = "nomn"

        self.INFLECTS_RUS = {
            "именительный": "nomn",
            "родительный": "gent",
            "дательный": "datv",
            "винительный": "accs",
            "творительный": "ablt",
            "предложный": "loct"
        }

        self.REDUCTIONS = ["ВАС РФ", "ВС РФ", "ЕСПЧ", "КС РФ", "МКАС", "ФАС", "СУ", "ЗВО", "ВВО"]

    def inflect_to(self, inflect):
        try:
            self.inflect = self.INFLECTS_RUS[inflect.lower()]
            morph = pymorphy3.MorphAnalyzer()
            inflector = PhraseInflector(morph)
            inflected_court_list = []
            for word in self.court.split():
                if word.lower().startswith("г."):
                    city = word
                    city_index = self.court.index(word)
                    inflected_court_list.insert(city_index, city)
                elif word.find(".") == -1 and word.find("№") == -1 and word.lower().find("р-на") == -1:
                    inflection = inflector.inflect(self.court, self.inflect)
                    if inflection is None:
                        none_symbol = word
                        none_index = self.court.index(word)
                        inflected_court_list.insert(none_index, none_symbol)
                    else:
                        return inflection.upper()
                else:
                    dotted_symbol = word
                    dotted_index = self.court.index(word)
                    inflected_court_list.insert(dotted_index, dotted_symbol)
            inflected_court = ' '.join(inflected_court_list)
            return inflected_court.upper()
        except (KeyError, ValueError):
            print("Падеж был введён с ошибкой")
            # raise Exception("Падеж введён с ошибкой")


while True:
    c = input("Введите название учреждения: ")
    i = input("Введите падеж: ")
    inf = Inflect(c)
    answer = inf.inflect_to(i)
    if answer:
        print(f'Ответ: {answer}')
    print("=" * 40)
