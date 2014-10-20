import json
import sys
import unicodecsv

from ftfy import fix_text


def csv_to_json(rows):
    json_dict = {}
    for row in rows:
        keys = row['key'].split('/')[:-1]
        leaf = row['key'].split('/')[-1]
        root = json_dict
        for part in keys:
            try:
                root = root[part]
            except KeyError:
                root[part] = {}
                root = root[part]
        root[leaf] = fix_text(row['spanish'].strip())
    print json.dumps(json_dict, indent=4, encoding='utf-8')


if __name__ == '__main__':
    csv_to_json(unicodecsv.DictReader(open(sys.argv[1], 'r'), encoding='latin-1'))
