###########################
# Day 16 - Packet Decoder #
# Part 2                  #
###########################


# Imports
from math import prod


# Get value of packet
def get_value(data, pos):
    type_id = int(data[pos + 3:pos + 6], 2)

    if type_id == 4:
        literal_value = ""
        final_group = False

        for i, bit in enumerate(data[pos + 6:]):
            if i % 5:
                literal_value += bit
            elif final_group:
                break
            elif bit == "0":
                final_group = True

        pos_change = i + 6

        return int(literal_value, 2), pos_change
    else:
        length_id = data[pos + 6]

        if length_id == "0":
            length_check = ["bit", int(data[pos + 7:pos + 22], 2)]
            pos_change = 22
        elif length_id == "1":
            length_check = ["packet", int(data[pos + 7:pos + 18], 2)]
            pos_change = 18

        sub_packets = []

        while length_check[1] > 0:
            new_packet = get_value(data, pos + pos_change)

            sub_packets.append(new_packet)
            pos_change += new_packet[1]

            if length_check[0] == "bit":
                length_check[1] -= new_packet[1]
            elif length_check[0] == "packet":
                length_check[1] -= 1

        sub_packets = [packet[0] for packet in sub_packets]

        if type_id == 0:
            return sum(sub_packets), pos_change
        elif type_id == 1:
            return prod(sub_packets), pos_change
        elif type_id == 2:
            return min(sub_packets), pos_change
        elif type_id == 3:
            return max(sub_packets), pos_change
        elif type_id == 5:
            return int(sub_packets[0] > sub_packets[1]), pos_change
        elif type_id == 6:
            return int(sub_packets[0] < sub_packets[1]), pos_change
        elif type_id == 7:
            return int(sub_packets[0] == sub_packets[1]), pos_change


def main():
    # Load input
    with open("inputs/day_16.txt") as file:
        data = "".join(bin(int(c, 16))[2:].zfill(4) for c in file.read())

    # Parse packets
    evaluated = get_value(data, 0)

    # Output results
    print(f"Evaluated value: {evaluated[0]}")


# Run script
if __name__ == "__main__":
    main()
