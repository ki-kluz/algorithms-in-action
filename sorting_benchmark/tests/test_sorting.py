import src.algorithms_sort as aSort
import src.random_generation as rGen


"""Проверяем, что все сортировки дают тот же результат, что и Python sorted()"""
def test_bubble_sort():
    original = rGen.generate_random_array(50, 1, 100)
    expected = sorted(original)
    assert aSort.bubble_sort(original.copy()) == expected, "Bubble Sort failed"

def test_insertion_sort():
    original = rGen.generate_random_array(50, 1, 100)
    expected = sorted(original)
    assert aSort.insertion_sort(original.copy()) == expected, "Insertion Sort failed"

def test_selection_sort_with_copy():
    original = rGen.generate_random_array(50, 1, 100)
    expected = sorted(original)
    assert aSort.selection_sort_with_copy(original.copy()) == expected, "Selection Sort (With-Copy) failed"

def test_selection_sort():
    original = rGen.generate_random_array(50, 1, 100)
    expected = sorted(original)
    assert aSort.selection_sort(original.copy()) == expected, "Selection Sort (In-Place) failed"