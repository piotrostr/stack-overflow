#!/usr/bin/env python


def sum_dicts(*dicts: dict) -> dict:
    out = {}
    for dictionary in dicts:
        for key, value in dictionary.items():
            if key not in out:
                out[key] = value
                continue
            out[key] += value
    return out


if __name__ == '__main__':
    fruit1 = {'apple': 3, 'banana': 1, 'cherry': 1}
    fruit2 = {'apple': 42, 'peach': 1}
    print(sum_dicts(fruit1, fruit2))
