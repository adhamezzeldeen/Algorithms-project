def my_len(s):
    count = 0
    for _ in s:
        count = count + 1
    return count


def longest_balanced(s):
    n = my_len(s)
    max_len = 0

    i = 0

    while i < n:

        freq = {}

        j = i

        while j < n:

            c = s[j]

            if c in freq:
                freq[c] = freq[c] + 1
            else:
                freq[c] = 1

            key_count = 0

            for _ in freq:
                key_count = key_count + 1

            if key_count > 2:
                break

            if key_count == 2:

                val1 = 0
                val2 = 0
                first = True

                for k in freq:

                    if first:
                        val1 = freq[k]
                        first = False
                    else:
                        val2 = freq[k]

                if val1 == val2:

                    length = j - i + 1

                    if length > max_len:
                        max_len = length

            j = j + 1

        i = i + 1

    return max_len



s = "aabbcc"

result = longest_balanced(s)

print(result)