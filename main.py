#!/usr/bin/env python

from bond import *
from benchmarks import *
from curve import *

import csv

def main():

    filename = input("Choose CSV file to import bond data: ")

    benchmarks = {}

    corp_list, gov_list = make_bond_list(filename)

    benchmarks = get_benchmarks(corp_list, gov_list)

    # CHALLENGE 1
    with open("spread_to_benchmark.csv", "w+", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["bond", "benchmark", "spread_to_benchmark"])

        for bond in benchmarks.keys():
            writer.writerow([bond.name, benchmarks[bond][0].name, "{0:.2f}%".format(benchmarks[bond][1])])


    # CHALLENGE 2
    with open("spread_to_curve.csv", "w+", newline="") as csvfile:

        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["bond", "spread_to_curve"])

        for corp in corp_list:
            writer.writerow([corp.name, "{0:.2f}%".format(get_curve(corp, gov_list))])


if __name__ == "__main__":
    main()