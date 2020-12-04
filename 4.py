# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

valid = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

hcl_valid = "1 2 3 4 5 6 7 8 9 0 a b c d e f".split(" ")

f = open("4.txt", 'r')
passports = f.read().strip().split("\n\n")

count = 0

for p in passports:
    p = p.replace(" ", "\n")

    keys = dict()
    for line in p.split("\n"):
        key,value = line.split(":")
        keys[key] = value
    if len(keys.keys()) == 8 or (len(keys.keys()) == 7 and 'cid' not in keys):
        valid = True

        if not (1920 <= int(keys['byr']) <= 2002):
            print('byr')
            valid = False

        if not (2010 <= int(keys['iyr']) <= 2020):
            print('iyr')
            valid = False

        if not (2020 <= int(keys['eyr']) <= 2030):
            print('eyr')
            valid = False

        if keys['hgt'][-2:] not in ['in', 'cm']:
            print('hgt')
            valid = False
        elif 'in' == keys['hgt'][-2:] and not (59 <= int(keys['hgt'][:-2]) <= 76):
            print('hgt')
            valid = False
        elif 'cm' == keys['hgt'][-2:] and not (150 <= int(keys['hgt'][:-2]) <= 193):
            print('hgt')
            valid = False

        if len(keys['hcl']) != 7:
            print('hcl')
            valid = False
        else:
            if keys['hcl'][0] != '#':
                print('hcl')
                valid = False
            else:
                for c in keys['hcl'][1:].lower():
                    if c not in hcl_valid:
                        print('hcl')
                        valid = False
                        break

        if keys['ecl'] not in 'amb blu brn gry grn hzl oth'.split(" "):
            print('ecl')
            valid = False


        if len(keys['pid']) != 9:
            print('pid')
            valid = False
        else:
            for c in keys['pid']:
                if c not in '0 1 2 3 4 5 6 7 8 9'.split(" "):
                    print('pid')
                    valid = False
                    break

        if valid:
            count += 1
        else:
            print(p, "\n")

    # print(p, "\n")

print(count)
