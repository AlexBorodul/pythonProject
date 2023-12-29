from flask import Flask, render_template, request, jsonify
import pymorphy3

app = Flask(__name__)

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

    def inflect_to(self, inflect):
        try:
            self.inflect = self.INFLECTS_RUS[inflect.lower()]
            morph = pymorphy3.MorphAnalyzer()
            inflected_court_list = []
            for word in self.court.split():
                if word.lower().startswith("г."):
                    city = word
                    city_index = self.court.index(word)
                    inflected_court_list.insert(city_index, city)
                elif word.find(".") == -1 and word.find("№") == -1 and word.lower().find("р-на") == -1:
                    inflected_court_list.append(morph.parse(word)[0].inflect({self.inflect}).word)
                else:
                    dotted_symbol = word
                    dotted_index = self.court.index(word)
                    inflected_court_list.insert(dotted_index, dotted_symbol)
            inflected_court = ' '.join(inflected_court_list)
            return inflected_court.upper()
        except (KeyError, ValueError):
            raise Exception("Падеж введён с ошибкой")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/inflect', methods=['POST'])
def inflect():
    data = request.get_json()
    court = data['court']
    inflection_case = data['case']
    inflector = Inflect(court)
    inflected_court = inflector.inflect_to(inflection_case)
    return jsonify({'result': inflected_court})

if __name__ == '__main__':
    app.run(debug=True)