def to_decimal(value, base):
    try:
        return int(value, base)
    except ValueError:
        return None

def from_decimal(decimal_value, target_base):
    if target_base == 'binary':
        return bin(decimal_value)[2:]
    elif target_base == 'octal':
        return oct(decimal_value)[2:]
    elif target_base == 'hex':
        return hex(decimal_value)[2:].upper()
    elif target_base == 'decimal':
        return str(decimal_value)
    else:
        return None

def get_base(system_name):
    bases = {
        'binary': 2,
        'octal': 8,
        'decimal': 10,
        'hex': 16
    }
    return bases.get(system_name.lower(), None)

def main():
    print("🔁 Universal Number System Converter")
    from_system = input("From (binary/octal/decimal/hex): ").strip().lower()
    value = input(f"Enter the value in {from_system}: ").strip()
    to_system = input("To (binary/octal/decimal/hex): ").strip().lower()

    from_base = get_base(from_system)
    to_base = get_base(to_system)

    if from_base is None or to_base is None:
        print("❌ Unsupported number system. Please choose from binary, octal, decimal, or hex.")
        return

    decimal_value = to_decimal(value, from_base)
    if decimal_value is None:
        print("❌ Invalid number for the selected 'from' system.")
        return

    result = from_decimal(decimal_value, to_system)
    print(f"✅ {value} ({from_system}) → {result} ({to_system})")

if __name__ == "__main__":
    main()
