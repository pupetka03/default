import sys
from core.executor import executor 


#return list code [example: ['q = Ihor', 'print "Sohodni vana krasavcik"', 'print {q}', 'print hi  {q}']]
def open_fail(fail):
    code = []
    fail_open = fail
    with open(f"{fail_open}", "r") as f:
        for line in f:
            lines = line.strip()
            if lines:
                code.append(lines)
    
    return code 


def main(fail):
    fail_code = open_fail(fail)
    executor(fail_code, fail) #start executor


#start compilator
if __name__ == "__main__":
    main('test.txt')  #start from vs code
    #if len(sys.argv) > 1:    # if you have app
        #file_path = sys.argv[1]
        #main(file_path)


