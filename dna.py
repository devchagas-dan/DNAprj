import csv
import sys


# CODIGO FINALIZADO MAS ANTES DE ENVIAR FAZER CHECK50. E VERIFICAR OUTRAS POSSIBILIDADES DE FAZER AS MESMAS COISAS TBM
def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit()

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as database_file:
        reader = csv.DictReader(database_file)
        database = [row for row in reader]

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence_file:
        sequence = sequence_file.read()

    # TODO: Find longest match of each STR in DNA sequence
    str_dict = {}
    for str in database[0].keys():
        if str == "name":
            continue
        str_dict[str] = longest_match(sequence, str)

    # TODO: Check database for matching profiles
    for row in database:
        dna_match = True
        for str in row.keys():
            if str == "name":
                continue
            if int(row[str]) != str_dict[str]:
                dna_match = False
                break
        if dna_match:
            print(row["name"])
            return
    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
