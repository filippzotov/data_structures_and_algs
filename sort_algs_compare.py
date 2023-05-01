import sort_algs as sa
import time
import random
import matplotlib.pyplot as plt


if __name__ == "__main__":
    results = {}
    num_of_elems = [i for i in range(0, 3000, 100)]
    sort_algs = [sa.bubbleSort, sa.insertionSort, sa.selectionSort, sa.quickSort]

    for elems in num_of_elems:
        test_list = random.sample(range(elems), elems)
        for sort_alg in sort_algs:
            tic = time.perf_counter()
            sort_alg(test_list)
            toc = time.perf_counter()

            if sort_alg.__name__ not in results:
                results[sort_alg.__name__] = []
            results[sort_alg.__name__].append(toc - tic)

    for key in results:
        plt.plot(num_of_elems, results[key], label=key)
    plt.legend()
    plt.show()
