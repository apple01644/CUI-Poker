def m2s(mark_number):
    if mark_number == '♥':
        return 0.25
    elif mark_number == '◆':
        return 0.5
    elif mark_number == '♠':
        return 0.75
    elif mark_number == '♣':
        return 0.0


def valuing(bundle):
    # 0:None, 1:Straight, 2:Back-Straight, 3:Mountain
    line_state = 0
    is_flush = True
    v = 0
    have = []
    for _ in range(0, 14):
        have.append(0)

    for c in bundle:
        have[c.rank] += 1

    if len(bundle) == 5:
        # is straight?
        for s in range(2, 10):
            seq = True
            for d in range(0, 5):
                if have[s + d] == 0:
                    seq = False
                    break
            if seq:
                line_state = 1
        # is back-staringht?
        seq = True
        for d in range(0, 5):
            if have[1 + d] == 0:
                seq = False
                break
        if seq:
            line_state = 2

        # is mountain?
        if have[1] == 1 and have[10] == 1 and have[11] == 1 and have[12] == 1 and have[13] == 1:
            line_state = 3

        s = bundle[0].suit
        for _ in range(1, 5):
            if bundle[_].suit == s:
                s = bundle[_].suit
            else:
                is_flush = False
                break

    pair = 0
    triple = 0
    four = 0
    for _ in range(1, 14):
        if have[_] == 2:
            pair += 1
        elif have[_] == 3:
            triple += 1
        elif have[_] == 4:
            four += 1

    if is_flush:
        if line_state == 3:
            return 12 + m2s(bundle[0].suit)
        elif line_state == 2:
            return 11 + m2s(bundle[0].suit)
        elif line_state == 1:
            for _ in range(1, 14):
                if have[_] > 0:
                    mn = _
                    break
            return 10 + (mn + m2s(bundle[0].suit)) / 14
    if four > 0:
        for _ in range(1, 14):
            if have[_] == 4:
                mn = _
                break
        return 9 + mn / 14
    if triple > 0 and pair > 0:
        for _ in range(1, 14):
            if have[_] == 3:
                mn = _
                break
        return 8 + mn / 14
    if is_flush:
        for _ in range(1, 14):
            if have[_] > 0:
                mn = _
        return 7 + mn / 14
    if line_state == 3:
        return 6 + m2s(bundle[0].suit)
    elif line_state == 2:
        return 5 + m2s(bundle[0].suit)
    elif line_state == 1:
        for _ in range(1, 14):
            if have[_] > 0:
                mn = _
                break
        return 4 + (mn + m2s(bundle[0].suit)) / 14
    if triple > 0:
        for _ in range(1, 14):
            if have[_] == 3:
                mk = 0
                for c in bundle:
                    v = m2s(c.suit)
                    if c.rank == _ and v > mk:
                        mk = v
                mn = _
                break
        return 3 + (mn + mk) / 14
    if pair > 1:
        for _ in range(1, 14):
            if have[_] == 2:
                mk = 0
                for c in bundle:
                    v = m2s(c.suit)
                    if c.rank == _ and v > mk:
                        mk = v
                mn = _
        return 2 + (mn + mk) / 14
    if pair > 0:
        for _ in range(1, 14):
            if have[_] == 2:
                mk = 0
                for c in bundle:
                    v = m2s(c.suit)
                    if c.rank == _ and v > mk:
                        mk = v
                mn = _
        return 1 + (mn + mk) / 14
    mk = 0
    for c in bundle:
        v = m2s(c.suit)
        if c.rank == _ and v > mk:
            mk = v
    for _ in range(1, 14):
        if have[_] == 1:
            mn = _
    return (mn + mk) / 14


def v2w(v):
    if v >= 13:
        return 'Overflow'
    if v >= 12:
        return 'Loyal Strainght FLush'
    if v >= 11:
        return 'Back-Straight Flush'
    if v >= 10:
        return 'Straight Flush'
    if v >= 9:
        return 'Four cards'
    if v >= 8:
        return 'Full house'
    if v >= 7:
        return 'Flush'
    if v >= 6:
        return 'Mountain'
    if v >= 5:
        return 'Back-Straight'
    if v >= 4:
        return 'Straight'
    if v >= 3:
        return 'Triple'
    if v >= 2:
        return 'Two pair'
    if v >= 1:
        return 'A pair'
    elif v >= 0:
        return 'Top'
    else:
        return 'Underflow'
