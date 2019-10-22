
import json


class ResultsSet:
    def __init__(self, full_sql='', rows=None, status=None,
                 effect_row=0, column_list=None, **kwargs):
        self.full_sql = full_sql
        self.error = None
        self.rows = rows or []
        self.column_list = column_list if column_list else []
        self.status = status
        self.effect_row = effect_row

    def to_json(self):
        tmp_list = []
        for r in self.rows:
            tmp_list += [dict(zip(self.column_list, r))]
        return json.dumps(tmp_list)

    def to_dict(self):
        # tmp_list = []
        # for r in self.rows:
        #     tmp_list += [dict(zip(column_list, r))]
        # return tmp_list

        dict_data = [dict(zip(self.column_list, row)) for row in self.rows]
        return dict_data