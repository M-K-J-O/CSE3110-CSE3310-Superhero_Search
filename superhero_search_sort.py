# superhero_search_sort.py
"""
title: Superhero search and sort
author: Marco Ou
date: feb 26th 2024
"""


def getRawData(fileName: str) -> vars:
    """
    Gets the raw file data from a csv file source
    :param fileName: [str]
    :return: templi, [var]
    """
    import csv
    tempLi = []
    fil = open(fileName)
    text = csv.reader(fil)
    for line in text:
        tempLi.append(line)
    var = tempLi.pop(0)
    return tempLi, var


def bubbleSort(LIST: list[int]) -> None:
    """
    compares two adjacent values and moves the highest one to the end of the list.
    :param LIST:  List[int]
    :return: None (lists persist inside and outside of a function)
    """
    for i in range(len(LIST) - 1, 0, -1):  # traversing backwards from the end of the list to index 1
        for j in range(i):
            # traversing forward in the unsorted section of the list
            if LIST[j] > LIST[i]:  # if the left number is larger than the right number
                TEMP = LIST[j]
                LIST[j] = LIST[j + 1]
                LIST[j + 1] = TEMP


def sortIndex(LIST: list, OUTLIST: list[int]) -> None:
    """
    Creates a list
    :param LIST: int
    :param SORT_INDEX: int
    :return: None
    """

    for i in range(len(rawArr)):
        TEMP = LIST[i][0]
        OUTLIST.append(TEMP)


def linearSearch(LIST: list[int], VALUE: str) -> bool:
    """
    Searchs the list for the value and prints it
    :param LIST: list[int]
    :param VALUE: str
    :return: Bool
    """
    for i in range(len(LIST) - 1):
        if LIST[i] == VALUE:
            print(f"Superhero ID - {SORTEDLIST[i][0]}")
            print(f"Name - {SORTEDLIST[i][1]}")
            print(f"ID - {SORTEDLIST[i][2]}")
            print(f"Align - {SORTEDLIST[i][3]}")
            print(f"Eye - {SORTEDLIST[i][4]}")
            print(f"Hair - {SORTEDLIST[i][5]}")
            print(f"Alive - {SORTEDLIST[i][6]}")
            print(f"Appearances - {SORTEDLIST[i][7]}")
            print(f"First Appearance - {SORTEDLIST[i][8]}")
            print(f"Year - {SORTEDLIST[i][9]}")
            print(f"Brand - {SORTEDLIST[i][10]}")
            return True
    return False


def finalSortedList(LIST: list[int]):
    """
    Creates Final List for the data sorted by ID
    :param LIST: list[int]
    :return: None
    """
    for i in range(len(LIST)):
        for j in range(len(rawArr)):
            if rawArr[j][0] == LIST[i]:
                SORTEDLIST.append(rawArr[j])


def search() -> None:
    """
    Searches the list for user input
    :return: None
    """
    print(" - Search ID - ")
    SEARCH = input("> ")
    BOOL = linearSearch(PSORTED_LIST, SEARCH)
    if BOOL == False:
        print(f" ID {SEARCH} is not found in this Database")


if __name__ == "__main__":
    from my_functions import *
    import string

    SORTEDLIST = []
    PSORTED_LIST = []
    rawArr, headers = getRawData('comicBookCharData_mixed.csv')

    # rawArr is a 2D arrays holding all the Superhero data
    # headers is a variable that holds the List of all the column headers.

    sortIndex(rawArr, PSORTED_LIST)
    bubbleSort(PSORTED_LIST)
    finalSortedList(PSORTED_LIST)
    while True:
        search()

