#!/usr/bin/env python3

# https://docs.opsgenie.com/docs/api-overview

import argparse
import json
import os
import requests

from entities import entities


BASE_URL_EU = 'https://api.eu.opsgenie.com'
BASE_URL_US = 'https://api.opsgenie.com'
BASE_URL = None


def mkdir(_dir):
    if not os.path.exists(_dir):
        os.mkdir(_dir)


def get_all_data(entity):
    url = '{}/{}?apiKey={}'.format(BASE_URL, entity, args.key)
    r = requests.get(url)

    if r.status_code in [402, 403]:
        return {'status_code': r.status_code, 'body': r.text}

    json_data = r.json()
    if 'data' in json_data:
        return json_data['data']

    return json_data


def entity_to_file(entity, outfile=''):
    print('...', entity)
    if not outfile:
        outfile = entity.replace('/', '_') + '.json'

    all_data = get_all_data(entity)

    f = open('{}/{}'.format(output_dir, outfile), 'w')
    f.write(json.dumps(all_data, indent=2))
    f.close()

    return all_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Dump all available data having Opsgenie API key')
    parser.add_argument('-k', '--key', required=True, help='Opsgenie API key')
    parser.add_argument('-r', '--region', default='eu', choices=['eu', 'us'], help='Region for Opsgenie API')
    parser.add_argument('-o', '--output', default='output', help='Local directory to dump data')
    args = parser.parse_args()

    BASE_URL = BASE_URL_EU
    if args.region == 'us':
        BASE_URL = BASE_URL_US

    output_dir = args.output
    mkdir(output_dir)


    for entity in entities:
        data = entity_to_file(entity)
        if isinstance(entities[entity], list):
            for subentity in entities[entity]:
                if 'status_code' in data:
                    continue  # error happened

                for item in data:
                    entity_id = item['id']
                    entity_to_file(subentity.format(entity=entity, id=entity_id))
