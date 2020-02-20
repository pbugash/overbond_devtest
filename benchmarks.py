def get_benchmarks(corp_list, gov_list):

    benchmarks = {}

    for corp in corp_list:
        min = float("inf")
        current_bench = gov_list[0]
        for gov in gov_list:
            if corp.diff_term(gov) < min:
                current_bench = gov
                min = corp.diff_term(gov)
                bench = abs(float(corp.yld) - float(gov.yld))
        setattr(corp, 'spread_bench', min)
        benchmarks[corp] = [current_bench, bench]
    
    return benchmarks