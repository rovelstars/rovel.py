THOUSAND = 1000
TEN_THOUSAND = 10000
MILLION = 1e6
BILLION = 1e9
TRILLION = 1e12

def _add_commas(num, opts):
    separator = opts.get("separator", False)

    if not separator or num < 1000:
        return str(num)

    separator = separator if isinstance(separator, str) else ","

    out = []
    digits = str(round(num)).split("")

    for i, digit in enumerate(digits[::-1]):
        if i % 3 == 0:
            out.append(separator)
        out.append(digit)

    return "".join(out[::-1])

def _format_dec(num, base, opts):
    working_num = num / base
    decimal = opts.get("decimal", False)

    if decimal:
        return str(round(working_num))

    num = str(round(working_num * 10) // 10 if working_num < 10 else round(working_num))
    if isinstance(decimal, str):
        num = num.replace(".", decimal)

    return num

def approximate_number(num, opts=None):
    if opts == None:
        opts = {}

    capital = opts.get("capital", False)
    prefix = opts.get("prefix", False)
    suffix = opts.get("suffix", False)
    min10k = opts.get("min10k", False)

    num_string = ""
    num = abs(num)

    thousands_break = TEN_THOUSAND if min10k else THOUSAND

    if num < thousands_break:
        num_string = _add_commas(_format_dec(num, 1, opts), opts)
    elif num < MILLION:
        num_string = _format_dec(num, THOUSAND, opts) + "k"
    elif num < BILLION:
        num_string = _format_dec(num, MILLION, opts) + "m"
    elif num < TRILLION:
        num_string = _add_commas(_format_dec(num, BILLION, opts)) + "b"
    else:
        num_string = _add_commas(_format_dec(num, TRILLION, opts), opts) + "t"

    if num < 0:
        num_string = "-" + num_string

    if capital:
        num_string = num_string.upper()

    if prefix:
        num_string = prefix + num_string

    if suffix:
        num_string += suffix

    return num_string