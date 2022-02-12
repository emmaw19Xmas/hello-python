import sys
import re
import json


def load_json(file_name):
    """
    load json file from command line
    @param:
        file_name: json file path
    @example:
        json_obj = load_json('json_case.txt')
            json_obj: python object
    """
    # Opening JSON file
    with open(file_name) as cases:
        orig_cases = json.load(cases)
    return orig_cases


def load_case_by_gpu(orig_cases):
    """
    parse the cases from load_json, and return new cases object with index by GPU number
    Note:
        1. GPU number is int number from 1 to 8, your code should ignore other invalid scenario
        2. those commands have some redundant space, your code should format them to single space in new json file.
    GPU index:
       From case exe: "exe": "test_bin -a -b -gpu 3 -d -e", match '-gpu ?', then get the index '3'
    @param:
        orig_cases: python object which is return from load_json()
    @example:
        new_cases = load_case_by_gpu(orig_cases)
            new_cases: python object
    """

    # for i in orig_cases['cases']:
    #     j = i['exe']
        #Remove all spaces between strings
        # x=j.split()
        # #print(x)
        # #Capture -gpu
        # gpu_index =x.index('-gpu')
        # #print(gpu_index)
        # gpu_number_address = gpu_index+1
        # gpu = x[gpu_number_address]
        # #filter out valid gpu numbers
        # if re.match('^\d+$', gpu) and int(gpu) >= 1 and int(gpu) <=8:
        #     list.append(x)
        # print(list)
        # return list
    obj = dict()
    for case in orig_cases["cases"]:
        log = case["exe"]
        match = re.match(r".*-gpu\s*(\d+)\s*-d.*",log)
        if match:
            gpu = match.groups()[0]
            if 1 <= int(gpu) <= 8:
                if gpu not in obj.keys():
                    obj[gpu] = []
                obj[gpu].append(case)
    print(obj)
    return obj





def save_json(json_obj, file):
    """
    save the new cases object to json file
    @param:
        json_obj: new case object which is return from load_case_by_gpu()
        file: target json file name, the json_obj would be serialized to json file
    @example:
        status = save_json(new_cases, output_file)
            status: True if saved successfully; False if any exception
    """
    with open(file, 'w') as f:
        json.dump(json_obj, f)

if __name__ == '__main__':
    #orig_cases = load_json(sys.argv[1] if len(sys.argv) > 1 else None)  # please pass command line argument 'json_case.txt' when run this script
    orig_cases = load_json('load_json.txt')
    new_cases = load_case_by_gpu(orig_cases)
    save_json(new_cases, 'new.json')  # hard code, and save to 'new_json.txt' in this script
