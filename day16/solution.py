# Day 16: Packet Decoder
# https://adventofcode.com/2021/day/16

from itertools import chain, islice
from dataclasses import dataclass
from typing import List, Union
from functools import reduce

# OPCODES
OP_SUM = 0
OP_PRODUCT = 1
OP_MINIMUM = 2
OP_MAXIMUM = 3
OP_LITERAL = 4
OP_GT = 5
OP_LT = 6
OP_EQ = 7


@dataclass
class Packet:
    version: int
    type: int
    value: Union[int, List["Packet"]]
    size: int

    def __call__(self) -> int:
        if self.type == OP_SUM:
            return sum(p() for p in self.value)
        if self.type == OP_PRODUCT:
            return reduce(lambda a, b: a * b, (p() for p in self.value))
        if self.type == OP_MINIMUM:
            return reduce(min, (p() for p in self.value))
        if self.type == OP_MAXIMUM:
            return reduce(max, (p() for p in self.value))
        if self.type == OP_LITERAL:
            return self.value
        if self.type == OP_GT:
            return 1 if (self.value[0]() > self.value[1]()) else 0
        if self.type == OP_LT:
            return 1 if (self.value[0]() < self.value[1]()) else 0
        if self.type == OP_EQ:
            return 1 if (self.value[0]() == self.value[1]()) else 0

        raise KeyError("invalid opcode")

    def __len__(self):
        return self.size


FILENAME = "input.txt"


with open(FILENAME) as f:
    stream = f.read().rstrip("\n")


def parse(bits, has_padding=True):
    version = int("".join(islice(bits, 3)), 2)
    type = int("".join(islice(bits, 3)), 2)

    if type == OP_LITERAL:  # literal value
        value = ""

        prefix = None
        while prefix is None or prefix == "1":
            prefix, group = next(bits), "".join(islice(bits, 4))
            value = value + group

        # compute the size of the padding
        packet_size = 3 + 3 + (len(value) // 4) * 5

        value = int(value, 2)
    else:
        # operation
        I = next(bits)
        if I == "0":
            total_length_bits = int("".join(islice(bits, 15)), 2)
            value = []
            packet_size = 3 + 3 + 1 + 15 + total_length_bits
            while total_length_bits > 4:
                packet = parse(bits, has_padding=False)
                value.append(packet)
                total_length_bits = total_length_bits - len(packet)
        else:
            num_subpackets = int("".join(islice(bits, 11)), 2)
            value = []
            packet_size = 3 + 3 + 1 + 11
            for _ in range(num_subpackets):
                packet = parse(bits, has_padding=False)
                value.append(packet)
                packet_size += len(packet)

    pad_size = 0
    if has_padding and packet_size % 4 > 0:
        pad_size = 4 - packet_size % 4
        _ = [next(bits) for _ in range(pad_size)]

    packet_size = packet_size + pad_size
    return Packet(version, type, value, packet_size)


def get_bits(stream):
    return chain(bit for ch in stream for bit in bin(int(ch, 16))[2:].zfill(4))


def sum_versions(packet: Packet):
    return packet.version + (
        0 if packet.type == OP_LITERAL else sum(sum_versions(p) for p in packet.value)
    )


test_cases = [
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31),
]
for sequence, expected_value in test_cases:
    assert expected_value == sum_versions(parse(get_bits(sequence)))


packet = parse(get_bits(stream))
print("Solution to part 1:", sum_versions(packet))  # 925

print("Solution to part 2:", packet())  # 342997120375
