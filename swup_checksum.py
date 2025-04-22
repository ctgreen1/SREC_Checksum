def calculate_checksum(hex_string):
    # Convert hex string to list of integers (bytes)
    byte_values = [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

    # Step 1: Sum all bytes
    total = sum(byte_values)

    # Step 2: Take only the least significant byte (LSB)
    lsb = total & 0xFF

    # Step 3: One's complement of LSB
    checksum = (~lsb) & 0xFF

    return f"Checksum: 0x{checksum:02X} ({checksum})"

# Example usage:
hex_input = "14012210003093E53C3083E20020A0E3002083E5"
print(calculate_checksum(hex_input))






