import os
import json
from pprint import pprint


class MainReader:

    def __init__(self, json_f: str, net_f_path: str) -> None:
        self.json_f = json_f
        self.json_d = self.json_to_dict()
        self.net_f_path = net_f_path
        self.net_str = self.net_class_reader()

    def json_to_dict(self):
        return json.load(open(self.json_f))

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

    # те поля в которых только словоформы
    unique_fields = ["lemma", "word", "Форма наст. вр.", "Комментарий", "gramm"]

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



file = "ana_out.json"
net_f_path = r"Enums/Thesaurus"
cls = TestDictionary(json_f=file, net_f_path=net_f_path)
json_d = cls.fields_filling()
pprint(json_d)
print(json_d.keys())
