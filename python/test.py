from multiprocessing import Process
import os

def foo():
    print("foo : current process : ", os.getpid())
    print("foo : parent process : ", os.getppid())

if __name__ == "__main__":
    print("process : ", os.getpid())
    # foo()
    child = Process(target=foo).start()