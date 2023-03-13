# from read_json import TestDictionary
# from pprint import pprint

file = "ana_out.json"
net_f_path = r"Enums/Thesaurus"

# pprint(TestDictionary(json_f=file, net_f_path=net_f_path).fields_filling())
dfj = {'NER': ['личн.', 'геогр.', 'патроним', 'этноним'],
 'Возвратность': ['возвр.'],
 'Время': ['аор.', 'наст.', 'имперф.', 'буд.'],
 'Залог': ['страдат.', 'действит.'],
 'Лицо': ['3-е', '2-е', '1-е'],
 'Наклонение': ['изъяв.', 'повелит.'],
 'Падеж': ['вин.',
           'им.',
           'род.',
           'зват.',
           'тв.',
           'дат.',
           'местн.',
           'вин.-род.'],
 'Полнота / краткость': ['полное', 'краткое'],
 'Разряд числительного': ['число', 'кол.', 'пор.', 'собир.'],
 'Репрезентация глагола': ['личн.ф.', 'прич.', 'инф.', 'супин'],
 'Род': ['ср.', 'м.', 'ж.', 'б/р', 'м. или ж.'],
 'Степень сравнения': ['сравн.'],
 'Тип причастия': ['прош.', 'наст.', 'перф.'],
 'Тип склонения': ['Fixed'],
 'Часть речи': ['предлог',
                'прил.',
                'сущ.',
                'гл.',
                'числит.',
                'союз',
                'нар.',
                'част.',
                'мест.',
                'пред.',
                'межд.',
                'вв.сл.'],
 'Число': ['ед.', 'мн.', 'дв.']}



# pprint(TestDictionary(json_f=file, net_f_path=net_f_path).create_match_d())
d_for_merge = {
 'NER': {'NF': 'PersonalityCategory', 'match_t': {'личн.': 'Personal'}},

 'Время': {'NF': 'Tense',
           'match_t': {'аор.': 'Aorist',
                       'буд.': 'Future',
                       'имперф.': 'Imperfect',  # датакласс не предусматривает # надо добавить вместо сов
                       'наст.': 'Present'}},

 'Залог': {'NF': 'Voice',
           'match_t': {'действит.': 'Active', 'страдат.': 'Passive'}},

 'Лицо': {'NF': 'GrammaticalPerson',
          'match_t': {'1-е': 'First', '2-е': 'Second', '3-е': 'Third'}},

 'Наклонение': {'NF': 'GrammaticalMood',
                'match_t': {'изъяв.': 'Realismood',
                            'повелит.': 'Imperativemood'}},

 'Падеж': {'NF': 'GrammaticalCase',
           'match_t': {'вин.': 'Accusative',
                       'вин.-род.': 'Accusative',  # датакласс не предусматривает == винительный
                       'дат.': 'Dative',
                       'зват.': 'Vocative',
                       'им.': 'Nominative',
                       'местн.': 'Locative',
                       'род.': 'Genitive',
                       'тв.': 'Instrumental'}},

 'Полнота / краткость': {'NF': 'CompletenessConcisenessCategory',
                         'match_t': {'краткое': 'Full', 'полное': 'Short'}},

 'Разряд числительного': {'NF': 'NumeralType',
                          'match_t': {'кол.': 'Cardinal',
                                      'пор.': 'Ordinal',
                                      'собир.': 'Collective'
                                      # 'число': '' датакласс не предусматривает
                                      }},

 'Репрезентация глагола': {'NF': 'VerbRepresentation',
                           'match_t': {'инф.': 'Infinitive',
                                       'личн.ф.': 'PersonalForm', # added
                                       'прич.': 'Participle',
                                       'супин': 'Supine'}},

 'Род': {'NF': 'GrammaticalGender',
         'match_t': {'б/р': 'No',  # added
                     'ж.': 'Feminine',
                     'м.': 'Masculine',
                     'м. или ж.': 'Common',  #датакласс не предусматривает
                     'ср.': 'Neuter'}},

 'Степень сравнения': {'NF': 'DegreeOfComparison', 'match_t': {
     'сравн.': 'Comparative' #датакласс не
                    }
               },

 'Тип причастия': {'NF': 'ParticipleType',
                   'match_t': {'наст.': 'Present',
                               'перф.': 'Perfect',
                               'прош.': 'Past'}
                   },

 'Часть речи': {'NF': 'PartOfSpeech',
                'match_t': {
                            # 'вв.сл.': '', датакласс не предусматривает предполагаю что это вводное слово, но это не часть речи
                            'гл.': 'Verb',
                            'межд.': 'Interjection',
                            'мест.': 'Pronoun',
                            'нар.': 'Adverb',
                            'пред.': 'Predicative',
                            'предлог': 'Preposition',
                            'прил.': 'Adjective',
                            'союз': 'Conjunction',
                            'сущ.': 'Noun',
                            'част.': 'Particle',
                            'числит.': 'Numeral'}
                },

 'Число': {'NF': 'GrammaticalNumber',
           'match_t': {'дв.': 'Dual', 'ед.': 'Singular', 'мн.': 'Plural'}},
 'Возвратность': {'NF': 'Recurrence', 'match_t': {'возвр.': 'Returnable'}},
 'Тип склонения': {'NF': 'DeclensionType', 'match_t': {'Fixed': 'Fixed'}}
}


# не затронутые файлы
not_found_f_net = ['PronounType.cs']

not_found_kjs = ['Возвратность']