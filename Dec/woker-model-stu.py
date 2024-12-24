"""
工作者模式
并发设计模式
"""

import multiprocessing
import time
def worker(task_queue):
    while True:
        task = task_queue.get()
        if task is None:
            break
        print(f"Processing taks: {task}")
        time.sleep(2)
        print(f"Task {task} completed")

def main():
    task_queue = multiprocessing.Queue()
    workers = []
    
    # 启动工作者进程
    for _ in range(3): # 启动3个工作者进程
        p = multiprocessing.Process(target = worker, args = (task_queue,))
        p.start()
        workers.append(p)
        
    # 向队列添加任务
    tasks = ['task1', 'task2',' task3', 'task4', 'task5']
    for task in tasks:
        task_queue.put(task)
        
    # 向队列添加退出信号
    for _ in workers:
        task_queue.put(None)
        
    # 等待所有工作者进程完成
    for p in workers:
        p.join()

if __name__ == '__main__':
    main()