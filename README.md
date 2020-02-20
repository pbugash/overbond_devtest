# Overbond Coding Challenge - Yield Spread Calculator

Given a CSV file, calculate the yield spreads and Reads input from a .csv file to calculate the yield spreads of one or more corporate bonds to either a government bond benchmark or to the government bond curve.

## How to Use?

1. Run file 'main.py'.
2. Input desired CSV file into the terminal
3. Spread to benchmark, and spread to curve can be found in the newly generated spread_to_benchmark and spread_to_curve CSV files.

## Technical Specs/Choices

#### Specs: 
- Python 3.7.4
- csv library
- unittest framework

#### Bond Class

Stores a bond's name, type, term, yield and spread to bench values. Made to simplify accessing data about a particular bond.

#### Approach to Problem
##### Challenge 1
Used csv.reader to read the input from the user's CSV file. If errors arose from invalid bond types, terms, yields, etc., an exception would be raised, informing user of the error.

Data from the CSV file was stored in a Bond objects list, separated into two categories based on their type, "corporate" or "government".

Next, I calculated the benchmarks of each corporation; found the benchmark by calculating the minimum absolute value of a given corporate bond, in comparison to all possible government bonds. Benchmarks were tracked using a dictionary.

Used Benchmarks dictionary to create a new CSV file to output the data

#### Challenge 2

Used the linear interpolation formula to calculate the spread to curve value.

For each corporate bond, I calculated the closest government bonds on the corporate bond's "left" and "right" side in terms of closest terms (ie. Gov bond 1 term < Corp bond term < Gov bond 2 term), by calculating the minimum term difference out of all of the available government bonds.

Once I had the two government bonds, I used their values to use linear interpolation to find the spread to curve for the corporate bond.

Outputted calculated information to another CSV file for easy to read access.

### What I Would Change

If given more time, I would prefer using a binary search on the government bonds to furthur improve the run time of finding the minimum term differences for each corporate bond (currently running in O(n <sup>2</sup> ) time, but using a binary seach would improve to an average case of O(nlogn)).
