class BondTypeError(Exception):
    pass

class BondTermError(Exception):
    pass

class BondYieldError(Exception):
    pass

class Bond():
    
    def __init__(self, name, type, term, yld):

        # check for csv errors
        if type != "corporate" and type != "government":
            raise BondTypeError('ERROR IN CSV FILE: type is not corporate nor government')

        if float(term) < 0:
            raise BondTermError('Invalid term duration')
        
        if float(yld) < 0:
            raise BondYieldError('Invalid yield percent')

        self.name = name
        self.type = type
        self.term = round(float(term), 2)
        self.yld = round(float(yld), 2)
        self.spread_bench = 0.0

    def __str__(self):
        return "Name: %s Type: %s Term: %f Yield: %f Bench: %f" % (self.name, self.type, self.term, self.yld, self.spread_bench)

    def diff_term(self, gov):
        return abs(float(self.term) - float(gov.term))

def make_bond_list(filename):

    import csv
    corp_list = []
    gov_list = []
    # create the corporate and government bond lists
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        line_count = 0

        # create corporate and government bonds
        for row in csv_reader:
            # get the data field names
            if line_count != 0:
                if row[1] == "corporate":
                    temp_term = row[2].replace(" years", "")
                    temp_yield = row[3].replace("%", "")
                    new = Bond(row[0], row[1], float(temp_term), float(temp_yield))
                    corp_list.append(new)
                elif row[1] == "government":
                    temp_term = row[2].replace(" years", "")
                    temp_yield = row[3].replace("%", "")
                    new = Bond(row[0], row[1], float(temp_term), float(temp_yield))
                    gov_list.append(new)
                # raise error if there are types are not valid
                else:
                    raise SyntaxError('ERROR IN CSV FILE: type is not corporate nor government')
            line_count += 1

    return corp_list, gov_list
        