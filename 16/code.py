# Advent of code Year 2021 Day 16 solution
# Author = Shane Coufreur
# Date = December 2021
import math

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()[0].strip()
    bitstring = ""

def parse_package(n, versions):
    #add version of subpacket to versions
    versions.append( int(bitstring[n:n+3], 2))
    packet_type = int(bitstring[n+3:n+6], 2)
    length_type_id = int(bitstring[n+6], 2)
    
    if packet_type == 4:        # packet is a literal    
        ret = []
        j = n+6

        while True:
            v = bitstring[j:j+5]
            ret.append(v[1:])
            j += 5
            if v[0] == '0':
                break
        ret = int("".join(ret), 2)
        return j, ret
    else:
        values = []
        if length_type_id == 0:
            # index of the first subpack
            pack_start = n + 22
            pack_len = int(bitstring[n + 7:n + 22], 2)
            pack_end = pack_start + pack_len
            # proces each subpack
            while pack_start < pack_end:
                pack_start, s = parse_package(pack_start, versions)
                values.append(s)
            return pack_start, calc(packet_type, values)
        else:
            num_packs = int(bitstring[n+7:n+18], 2)
            pack_start = n + 18

            for _ in range(num_packs):
                pack_start, s = parse_package(pack_start, versions)
                values.append(s)
            return pack_start, calc(packet_type, values)

def calc( calc_type, values ):
    if calc_type == 0:
        return sum(values)
    elif calc_type == 1:
        return math.prod(values)
    elif calc_type == 2:
        return min(values)
    elif calc_type == 3:
        return max(values)
    elif calc_type == 5:
        if values[0] > values[1]:
            return 1
        return 0
    elif calc_type == 6:
        if values[0] < values[1]:
            return 1
        return 0
    elif calc_type == 7:
        if values[0] == values[1]:
            return 1
        return 0

def solve1(hex):
    print("Solving for:", hex)

    global bitstring
    bitstring = ""
    for c in hex:
        bitstring += "{0:04b}".format(int(c, 16))
        
    versions = []
    parse_package(0, versions)
    return sum(versions)

def solve2(hex):
    print("Solving for:", hex)

    global bitstring
    bitstring = ""
    for c in hex:
        bitstring += "{0:04b}".format(int(c, 16))
        
    versions = []
    v = parse_package(0, versions)
    return v[1]

PREFIX_1 = "Part One : "

t1 = solve1("D2FE28")
print(PREFIX_1+ str(t1))
assert t1 == 6
t1 = solve1("38006F45291200")
print(PREFIX_1+ str(t1))
assert t1 == 9
t1 = solve1("EE00D40C823060")
print(PREFIX_1+ str(t1))
assert t1 == 14
t1 = solve1("8A004A801A8002F478")
print(PREFIX_1+ str(t1))
assert t1 == 16
t1 = solve1("620080001611562C8802118E34")
print(PREFIX_1+ str(t1))
assert t1 == 12
t1 = solve1("C0015000016115A2E0802F182340")
print(PREFIX_1+ str(t1))
assert t1 == 23
t1 = solve1("A0016C880162017C3686B18A3D4780")
print(PREFIX_1+ str(t1))
assert t1 == 31
print("Part One : "+ str(solve1(input)))

PREFIX_2 = "Part Two : "
t2 = solve2("C200B40A82")
print(PREFIX_2+ str(t2))
assert t2 == 3
t2 = solve2("04005AC33890")
print(PREFIX_2+ str(t2))
assert t2 == 54
t2 = solve2("880086C3E88112")
print(PREFIX_2+ str(t2))
assert t2 == 7
t2 = solve2("CE00C43D881120")
print(PREFIX_2+ str(t2))
assert t2 == 9
t2 = solve2("D8005AC2A8F0")
print(PREFIX_2+ str(t2))
assert t2 == 1
t2 = solve2("F600BC2D8F")
print(PREFIX_2+ str(t2))
assert t2 == 0
t2 = solve2("9C005AC2F8F0")
print(PREFIX_2+ str(t2))
assert t2 == 0
t2 = solve2("9C0141080250320F1802104A08")
print(PREFIX_2+ str(t2))
assert t2 == 1
print("Part Two : "+ str(solve2(input)))