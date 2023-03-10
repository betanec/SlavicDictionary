import os
import json
from pprint import pprint
import re
from super_d import d_for_merge
from jinja2 import Template

file = "ana_out.json"
net_f_path = r"Enums/Thesaurus"

class MainReader:

    def __init__(self, json_f: str, net_f_path: str) -> None:
        self.json_f = json_f
        self.json_d = self.json_to_dict()
        self.net_f_path = net_f_path
        self.net_str = self.net_class_reader()

    def json_to_dict(self):
        return json.load(open(self.json_f, encoding='utf-8'))

    def net_class_reader(self) -> dict:
        aggregation = dict()
        for folder in os.listdir(path=self.net_f_path):
            for file in os.listdir(path=self.net_f_path + f"/{folder}"):
                for line in open(self.net_f_path + f"/{folder}/{file}", 'r', encoding="UTF-8"):
                    if file not in aggregation:
                        aggregation[file] = line
                    else:
                        aggregation[file] += line
        return aggregation


class TestDictionary(MainReader):
    # не для мэтча
    # unique_fields = ["lemma", "word", "Форма наст. вр.", "Комментарий", "gramm", "grdic", "tag_str",
    #                  "tags", "manual", "Ошибка", "Тип склонения", "Возвратность"]
    unique_fields = ["lemma", "word", "Комментарий", "gramm", "grdic", "Форма наст. вр.", "tags"]
    # Форма наст. вр. !!!спросить

    def __init__(self, json_f: str, net_f_path: str) -> None:
        super().__init__(json_f, net_f_path)
        self.json_f_filing = self.fields_filling()

    def fields_filling(self) -> dict:
        res = dict()
        for k, v in self.json_d.items():
            for v_l in v:
                for k_v_l, v_v_l in v_l.items():
                    if k_v_l not in self.unique_fields:
                        if k_v_l not in res:
                            res[k_v_l] = [v_v_l]
                        else:
                            if v_v_l not in res[k_v_l]:
                                res[k_v_l].append(v_v_l)
                            else:
                                continue
                    else:
                        continue
        return res

    def merge_json_keys_with_main_net_class(self, file: str = "LinguisticForm.cs") -> dict():
        nfile = open(file, 'r', encoding="UTF-8").read()
        n_class_d = dict()
        for k in self.json_f_filing.keys():
            p = nfile.find(k)
            if p > -1:
                found = nfile[p:p + len(k)]
                # print()
                print(k, found, k == found)
                pattern = f"\/\/\/\s({k}[\s\/А-я][^\n]+)\n*\s*\/\/\/\s*?<\/summary\>\s*\n*public\s([A-z]+)"
                net_class = re.search(pattern, string=nfile)
                n_class_d[k] = net_class.group(2)
            else:
                continue
                # print("Lost:", k)
        return n_class_d


    def create_match_d(self, gr: int = 1) -> dict:
        matched_d = dict()
        n_class_d = self.merge_json_keys_with_main_net_class()
        pprint(self.json_f_filing)
        for k, v in self.json_f_filing.items():
            for lv in v:
                clean_ss = lv.replace(".", "")
                p = f'({clean_ss}[a-я\s]+)\"\)\]\n*?\s*?([a-z]+)|({clean_ss})\"\)\]\n*?\s*?([a-z]+)'
                # for kn, vn in self.net_str.items():
                if k in n_class_d:
                    file = n_class_d[k]+".cs"
                    vn = self.net_str[file]
                    res = re.search(pattern=p, string=vn.lower())
                    print(res)
                    if res is not None:
                        # print(res.groups(), lv, kn)
                        cleaned_from_none = [i for i in res.groups() if i]
                        if k not in matched_d:
                            matched_d[k] = {"NF": file.replace(".cs", ""), "match_t": {lv: cleaned_from_none[gr].title()}}
                        else:
                            matched_d[k]["match_t"][lv] = cleaned_from_none[gr].title()
                    else:
                        if k not in matched_d:
                            matched_d[k] = {"NF": file.replace(".cs", ""), "match_t": {lv: ''}}
                        else:
                            matched_d[k]["match_t"][lv] = ''
                else:
                    print(k)
                    continue

        return matched_d

pprint(TestDictionary(json_f=file, net_f_path=net_f_path).fields_filling())
# pprint(TestDictionary(json_f=file, net_f_path=net_f_path).create_match_d())


class ConversionDictionary(TestDictionary):

    ServiceComment = ["grdic", "Форма наст. вр.", "gramm"]

    must_have_w = {"Lemma": "lemma", "Word": "word", "Comment": "Комментарий"}

    def __init__(self, json_f: str, net_f_path: str) -> None:
        super().__init__(json_f, net_f_path)
        self.conv = self.get_conversion()


    def get_conversion(self) -> dict:
        answer = dict()
        for key, val in self.json_d.items():
            answer[key] = list()
            for temp in val:
                trash = list()
                # pep = list()
                # answer[key] += [f'{k} = "{y}"' for k, v in self.must_have_w.items() if (y := temp.get(v))]
                pep = [f'{k} = "{y}"' for k, v in self.must_have_w.items() if (y := temp.get(v))]
                for ke, va in temp.items():
                    if ke not in self.unique_fields:
                        clast = d_for_merge[ke]
                        cls = clast["NF"]
                        cls_fillness = clast["match_t"]
                        va = va.lower()
                        if va in cls_fillness:
                            net_v = cls_fillness[va]
                            # answer[key].append(f"{cls} = {cls}.{net_v}")
                            pep.append(f"{cls} = {cls}.{net_v}")
                        else:
                            continue
                    elif ke in self.ServiceComment:
                        trash.append(f"{ke} : {va}")
                # answer[key].append(f'ServiceComment = "' + ";".join([i for i in trash]) + '"')
                pep.append(f'ServiceComment = "' + ";".join([i for i in trash]) + '"')
            answer[key].append(pep)
        return answer


# cls = ConversionDictionary(json_f=file, net_f_path=net_f_path)
# main_dict = cls.get_conversion()
#
# st = """public List<LinguisticForm> GetWords()
#     {
#         return new List<LinguisticForm> {
#             {% for word, l in main_dict.items() -%}
#                 {% for arr in l -%}
#                     new LinguisticForm{ {{', '.join(arr)}} },
#                 {% endfor -%}
#             {% endfor -%}
#         };
#     }"""
#
# tm = Template(st)
# msg = tm.render(main_dict=main_dict)
# with open("net_result", "w", encoding='utf-8') as fh:
#     fh.write(msg)