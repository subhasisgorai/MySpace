

def restore_ip_addresses(s):

    def is_valid_ip_part(part):
            return (len(part) == 1 or 
                        (part[0] != '0' and int(part) < 256))

    if s and len(s) > 3:
        result, parts = list(), [''] * 4            
        for i in range(1, 4):
            parts[0] = s[:i]
            if is_valid_ip_part(parts[0]):
                for j in range(1, min(4, len(s) - i)):
                    parts[1] = s[i:i + j]
                    if is_valid_ip_part(parts[1]):
                        for k in range(1, min(4, len(s) - i - j)):
                            parts[2], parts[3] = s[i + j: i + j + k], s[i + j + k:]
                            if (is_valid_ip_part(parts[2]) and
                                    is_valid_ip_part(parts[3])):
                                result.append('.'.join(parts))
        return result
    return None
