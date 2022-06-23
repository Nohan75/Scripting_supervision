import sys
import time
import supervision

functions = supervision.functions


def execute_log(interval, log_functions):
    while True:
        for log_function in log_functions:
            log_function()
        time.sleep(interval)
        print("\n")
        print(" --- END OF THIS LOG --- ")
        print("\n")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            print('Use: python main.py -f [<functions>] or -f all to use all functions')
            print('Use: "python main.py -fl" to see all functions')
        if sys.argv[1] == "-fl":
            for i in range(len(functions)):
                print(functions[i].__name__.replace('log_', '') + ":", functions[i].__name__)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f":
            if sys.argv[2] == "all":
                log_functions = functions
                execute_log(5, log_functions)
    else:
        sys.exit(1)
