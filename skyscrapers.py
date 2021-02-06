'''
Module for setup of Skyscraper game!
Github :
https://github.com/glibesyck/Skyscrapper.git
'''

def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.
    """
    list_of_lines = []
    with open (path, 'r', encoding='utf-8') as file :
        for line in file :
            line = line.strip()
            list_of_lines.append(line)
    return list_of_lines

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    max_height = 0
    buildings = 0
    result = False
    for i in range (1, len(input_line)-1) :
        if int(input_line[i]) > max_height :
            buildings += 1
            max_height = int(input_line[i])
    if buildings == pivot :
        result = True
    return result


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5',\
         '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*5?3215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = True
    for line in board :
        if "?" in line :
            result = False
    return result


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215',\
 '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = True
    for line in board :
        if line[0] != "*" or line[-1] != '*' :
            list_of_values = []
            for i in range(1, len(line)-1) :
                if line[i]!="*" :
                    if line[i] in list_of_values :
                        result = False
                    else :
                        list_of_values.append(line[i])
    return result

def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215',\
         '*35214*', '*41532*', '*2*1***'])
    False
    """
    result = False
    if check_not_finished_board(board) :
        result = True
        for line in board :
            if line[0] != '*' :
                if not left_to_right_check(line, int(line[0])) :
                    result = False
                if line[-1] != '*' :
                    if not left_to_right_check(line[::-1], int(line[-1])) :
                        result = False
            elif line[0] == '*' and line[-1] != '*' :
                if not left_to_right_check(line[::-1], int(line[-1])) :
                    result = False
    return result

def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique
     height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*',\
         '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*',\
         '*41532*', '*2*1***'])
    False
    """
    new_board = []
    result = False
    for i in range(len(board)) :
        new_line = ''
        for j in range(len(board)) :
            new_line = new_line + board[j][i]
        new_board.append(new_line)
    if check_horizontal_visibility(new_board) and check_uniqueness_in_rows(new_board) :
        result = True
    return result

def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    result = False
    board = read_input(input_path)
    if check_columns(board) and check_horizontal_visibility(board) and\
         check_uniqueness_in_rows(board) and check_not_finished_board(board) :
        result = True
    return result
