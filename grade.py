def read_grades(gradefile):
    ''' (file open for reading) -> list of float

    Read and return the list of grades in gradefile.

    Precondition: gradefilestarts with a header that
    contains no blank lines, then has a blank line,
    and then lines containing a student number and
    a grade.
    '''

    # Skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
        
    # Read the grades, accumulating them into a list.
    
    grades = []
    
    line = gradefile.readline()
    while line != '':
        # Now we have a string containing the info for
        # a single student.
        # Find the last space and take everything after
        # that space.
        grade = line[line.rfind(' ') + 1:]
        grades.append(float(grade))
        line = gradefile.readline()

    return grades

def count_grade_ranges(grades):
    ''' (list of float) -> list of int

    Return a list of int where each index indicates how
    many grades were in these ranges:

    0-9:   index 0
    10-19: index 1
    20-29: index 2
      :
    90-99: index 9
    100:   index 10

    >>> count_grade_ranges([39.7, 84.2, 42.6, 89.1, 66.8, 89.7, 54.0, 80.8, 77.1, 41.2, 98.1])
    [0, 0, 0, 1, 2, 1, 1, 1, 4, 1, 0]
    '''

    range_counts = [0] * 11
    
    for grade in grades:
        which_range = int(grade // 10)
        range_counts[which_range] += 1

    return range_counts


def write_histogram(range_counts, histfile):
    ''' (list of int, file open for writing) -> NoneType

    Write a histogram of asterisks based on the number of
    grades in each range.

    The output format:
    0-9:   *
    10-19: **
    20-29: ******
      :
    90-99: **
    100:   *

    '''

    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    # Write the 2-digit ranges.
    for i in range(1, 10):
        low = i * 10
        high = i * 10 + 9
        histfile.write( str(low) + '-' + str(high) + ': ' )
        histfile.write( '*' * range_counts[i] )
        histfile.write('\n')
        
    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')
