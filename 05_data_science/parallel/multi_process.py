from multiprocessing import Process
import os
import pandas as pd


def info(title):
    print(title)
    print('module name:', __name__)
    if hasattr(os, 'getppid'):  # only available on Unix
        print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(sub_array):
    info('function f')
    # print('array', sub_array)


if __name__ == '__main__':
    info('main line')
    number_of_parallel = 30

    # array = np.arange(100)
    # l = len(array)
    # for i in range(10):
    #     begin = int(l/10*i)
    #     end = int(l/10*(i+1))
    #     p = Process(target=f, args=(array[begin:end],))
    #     p.start()
    #     p.join()

    df = pd.DataFrame({'A': range(0, 126, 1)})
    count_row = df.shape[0]

    jobs = []
    print(df)
    for i in range(number_of_parallel):
        begin = int(count_row/number_of_parallel*i) if i == 0 else int(count_row/number_of_parallel*i) + 1
        end = int(count_row/number_of_parallel*(i+1))
        print(i, begin, end)
        process = Process(target=f, args=(df.iloc[begin:end],))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)
    for j in jobs:
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        j.join()

    print('List processing complete.')
