def get_curve(corp, gov_list):

    """
    C1.spread_to_curve = A - B

    A = C1.yield
    B = yield at C1_term between gov1 and gov2

    """
    gov1 = None
    gov2 = None

    a = float("inf")
    b = float("inf")

    for gov in gov_list:
        diff = corp.diff_term(gov)

        # get the 2 gov bonds that corp is in between
        if gov.term > corp.term:
            if a > diff:
                gov1 = gov
                a = diff
        elif gov.term < corp.term:
            if b > diff:
                gov2 = gov
                b = diff

    x1 = float(gov1.term)
    y1 = float(gov1.yld)
    x2 = float(gov2.term)
    y2 = float(gov2.yld)
    x_corp = float(corp.term)

    # linear interpolation formula
    yld = (((x_corp-x1) * (y2-y1))/(x2-x1)) + y1

    curve = abs(round(yld - corp.yld, 2))

    return curve



