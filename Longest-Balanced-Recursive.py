def my_len(s):
    count = 0
    for _ in s:
        count = count + 1
    return count


def longest_balanced_recursive(s, start=0, best=0):

    n = my_len(s)

    if start >= n - 1:
        return best

    freq = {}

    end = start

    while end < n:

        c = s[end]

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

                length = end - start + 1

                if length > best:
                    best = length

        end = end + 1

    return longest_balanced_recursive(s, start + 1, best)



s = "aabbcc"

result = longest_balanced_recursive(s)

print(result)