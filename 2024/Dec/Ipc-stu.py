"""
进程间通信 Inter-Process Communication, IPC)
1.管道(Pipes) 2.
"""
import multiprocessing

def worker(q):
    q.put("Hello from the child process")
    
if __name__ == "__main__":
    # 父进程创建一个队列
    q = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()

    message = q.get()
    print("Received from child:", message)