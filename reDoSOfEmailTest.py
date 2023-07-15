import time
import re

def check_regex(input_string):
    start_time = time.time()
    regex = r"[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,255}\.[a-zA-Z]{2,6}"
    print(input_string[0:100])
    match = re.search(regex, input_string)
    if match:
        print(f"Match the regex: {match.group()}")
    else:
        print("Not match the regex")
    # print(f"Text: {input_string}, Execution time: {time.time() - start_time:.10f} seconds")
    print(f"Execution time: {time.time() - start_time:.10f} seconds")


def main():
    check_regex("This is a test text with email .test@example.com inside.")
    # check_regex('A.'*1311111 + '-.'*13111)

if (__name__ == "__main__"):
    main()
