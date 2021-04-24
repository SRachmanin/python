import json

with open('firm.json', 'w') as f:
    with open('firm.txt', encoding='utf-8') as f1:
        prof = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f1}
        result = [prof, {'profit': round(sum([int(i) for i in prof.values() if int(i) > 0]) /
                                             len([int(i) for i in prof.values() if int(i) > 0]))}]

    json.dump(result, f, ensure_ascii=False, indent=4)