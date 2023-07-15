import time
import re

# This function that receives text and check it with regex that might be a vulnerability of ReDoS
def check_regex(input_string):
    start_time = time.time()
    regex = r"^(([a-zA-Z0-9])+)+$"
    if re.match(regex, input_string):
        print("Match the regex")
    else:
        print("Not match the regex")
    print(f"Text: {input_string}, Execution time: {time.time() - start_time:.10f} seconds")


def main():
    check_regex("abcdefghij")
    check_regex("abcdefghijklmnopqrstuvwxyz")
    check_regex("abcdefghijklmnopqrstuvwxyzABC")
    check_regex("abcdefghij@")
    check_regex("abcdefghijklmnopqrstuvwxyz@")
    check_regex("abcdefghijklmnopqrstuvwxyzA@")
    check_regex("@abcdefghijklmnopqrstuvwxyzA")
    check_regex("abcdefghijklmnopqrstuvwxyzA@B")

if (__name__ == "__main__"):
    main()
