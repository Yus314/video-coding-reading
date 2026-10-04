"""Illustrative local syntax trace, NOT an H.274 parser/conformance test.

The inserted suffix assumes TemporalExtrapolationFlag=1 and no intervening
spatial/tone-mapping fields. Only the first misread field is modeled.
The merged gate trace models design intent, not a valid TuC bitstream:
the inspected TuC also reserves 16..255, conflicting with its 0x10 gate.
"""
import json


def ue(value):
    if value < 0:
        raise ValueError('ue(v) requires a non-negative integer')
    bits = format(value + 1, 'b')
    return '0' * (len(bits) - 1) + bits


def example():
    count = ue(1)  # old proposed num_alt_instances_minus1
    flag = '1'
    component = '1'
    suffix = count + flag + component
    auxiliary = 16
    return {
        'scope': 'synthetic partial syntax trace; not a complete SEI payload',
        'before_relocation': {
            'bits': suffix,
            'extension_aware': {'count_bits': count, 'mult_flag': flag,
                                'component_last_flag': int(component)},
            'v4_first_read': {'field': 'nnpfc_component_last_flag',
                              'value': int(suffix[0]), 'bits_consumed': 1},
        },
        'merged_design_intent': {
            'auxiliary_inp_idc': auxiliary,
            'ue_bits': ue(auxiliary),
            'v4_required_action': 'ignore this NNPFC SEI message',
            'new_syntax_gate': bool(auxiliary & 0x10),
            'new_minus2_value': 0,
            'alternative_versions': 0 + 2,
            'conformance_claim': False,
            'unresolved': 'inspected TuC also reserves 16..255',
        },
    }


if __name__ == '__main__':
    print(json.dumps(example(), ensure_ascii=False, indent=2))
