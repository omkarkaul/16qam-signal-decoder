import sys

points = {
            (-3,3): "0000",
            (-3,1): "0001",
            (-3,-3): "0010",
            (-3, -1): "0011",
            (-1,3): "0100",
            (-1,1):"0101",
            (-1,-3):"0110",
            (-1,-1):"0111",
            (3,3):"1000",
            (3,1):"1001",
            (3,-3):"1010",
            (3,-1):"1011",
            (1,3):"1100",
            (1,1):"1101",
            (1,-3):"1110",
            (1,-1):"1111"
        }

def coord_to_nibble(coord):
    """ transform coord to 4 bit binary"""
    return points[coord]

def round_16qam(number):
    """
    performs appropriate rounding for 16qam sig
    """

    # 1 or 3
    if number >= 0:
        if number > 2:
            return 3
        return 1
    # -1 or -3
    else:
        if number < -2:
            return -3
        return -1

def main():
    """
    reads 16qam signal file and decodes it to byte addressable binary (for ASCII)
    """
    binary_message = ""
    output = ""

    for line in sys.stdin:
        coord = eval(line.strip())
        new_x = round_16qam(coord[0])
        new_y = round_16qam(coord[1])

        new_coord = (new_x, new_y)
        binary_message += coord_to_nibble(new_coord)
        print(f"{coord} decodes as {coord_to_nibble(new_coord)}")
    
    count = 0

    while count < len(binary_message):
        byte = binary_message[count:count+8]
        output += chr(int(byte, 2))

        count += 8

    print(output)

if __name__ == "__main__":
    main()

