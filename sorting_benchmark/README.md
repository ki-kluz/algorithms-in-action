# Sorting Benchmark

Модуль для реализации и сравнительного анализа скорости алгоритмов сортировки. Демонстрирует поведение алгоритмов на случайных и почти отсортированных данных.

## Запуск проекта

Убедитесь, что вы находитесь в корне репозитория и установили зависимости, после чего выполните команду:

```bash
python 01_sorting_benchmark/src/benchmark.py
```

## Поддерживаемые алгоритмы

| Алгоритм | Сложность | Особенности |
| :--- | :--- | :--- |
| **Bubble Sort** | $O(n^2)$ | Много обменов, неэффективен на больших данных |
| **Insertion Sort** | $O(n^2) \rightarrow O(n)$ | Показывает лучшую скорость на почти отсортированных массивах |
| **Selection Sort (In-Place)** | $O(n^2)$ | Экономен по памяти, делает фиксированное число обменов |
| **Selection Sort (With-Copy)** | $O(n^2)$ | Создает копию массива, требует $O(n)$ дополнительной памяти |

## Тестирование производительности

Скрипт генерирует два типа массивов (размером 10 000 элементов):
1. **Random array** — равномерное распределение (худший случай для большинства).
2. **Nearly sorted** — массив с небольшим количеством случайных перестановок (идеально для Insertion Sort).

### Пример результатов бенчмарка

```text
=== Algorithms Benchmark ===

--- Random arrays ---
Array size: 10000
Range: 1 - 10000

Bubble Sort: 2.613 sec
Insertion Sort: 1.849 sec
Selection Sort (In-Place): 1.089 sec
Selection Sort (With-Copy): 0.916 sec

Winner: Selection Sort (With-Copy) (0.916)

--- Nearly arrays ---
Bubble Sort: 1.517 sec
Insertion Sort: 0.051 sec
Selection Sort (In-Place): 1.080 sec
Selection Sort (With-Copy): 0.910 sec

Winner: Insertion Sort (0.051)
```

## TODO

- [ ] Добавить реализацию QuickSort ($O(n \log n)$)
- [ ] Интегрировать визуализацию графиков времени через `matplotlib`
