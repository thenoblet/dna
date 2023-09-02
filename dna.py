import csv
import sys


def main():
    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: python dna.py [databases/database.csv] [sequences/sequence.txt]"
        )

    # Read database file into a variable
    database = sys.argv[1]
    file = open(database, "r")
    reader = csv.DictReader(file)
    new_list = list(reader)

    # Read DNA sequence file into a variable
    sequence = sys.argv[2]
    txt_file = open(sequence, "r")
    data = txt_file.read()

    # Find longest match of each STR in DNA sequence
    STR_count = {}
    for row in new_list:
        for STR in row.keys():
            if STR != "name":
                STR_count[STR] = longest_match(data, STR)

    # Check database for matching profiles
    for row in new_list:
        match = True
        name = row["name"]

        # Iterate over keys in the STR_count dictionary
        for STR in STR_count.keys():
            # row[STR] retrieves the value of the STR in the current row of the database and cast it into an int
            # STR_count[STR] retrieves the value of the corresponding STR in the STR_count dictionary
            if int(row[STR]) != STR_count[STR]:
                match = False
                break
        if match:
            print(name)
            return

    print("No Match")

    # Close files
    file.close()
    txt_file.close()


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
