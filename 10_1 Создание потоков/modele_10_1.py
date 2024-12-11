import time
import threading

def wite_words(word_count, file_name):
    with open(f'{file_name}', "w") as file:
        for i in range(1,word_count + 1):
            time.sleep(0.1)
            file.write(f"Какое-то слово № {i} \n")
        print(f"Завершилась запись в файл {file_name}")

start_time = time.time()
variables_func = ([10, "example1.txt"], [30, "example2.txt"], [200, "example3.txt"], [100, "example4.txt"])
for i in variables_func:
    threading.Thread(target=wite_words(i[0],i[1]))
and_time = time.time()
print(f'Работа потоков{and_time - start_time}.')

start_time = time.time()
variables_flow = ([10, "example5.txt"], [30, "example6.txt"], [200, "example7.txt"], [100, "example8.txt"])
thread_list=[]
for i in variables_flow:
    flow = threading.Thread(target=wite_words, args = (i[0],i[1]))
    thread_list.append(flow)
    flow.start()
for j in thread_list:
    j.join()
and_time = time.time()
print(f'Работа потоков{and_time - start_time}.')