import itertools
import string
import threading
import time
import argparse

def thread_function(password, charset, start_length, end_length, result):
    for length in range(start_length, end_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if guess == password:
                result.append(guess)
                return

def multi_threaded_brute_force(password, charset, max_length, num_threads):
    threads = []
    result = []
    chunk_size = max_length // num_threads

    for i in range(num_threads):
        start_length = i * chunk_size + 1
        end_length = (i + 1) * chunk_size if i != num_threads - 1 else max_length
        thread = threading.Thread(target=thread_function, args=(password, charset, start_length, end_length, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result[0] if result else None

def crack_passwords_from_file(password_file, charset, max_length, num_threads):
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()
    
    for password in passwords:
        start_time = time.time()
        print(f"Attempting to crack password: {password}")
        found_password = multi_threaded_brute_force(password, charset, max_length, num_threads)
        elapsed_time = time.time() - start_time
        if found_password:
            print(f"Password found: {found_password} in {elapsed_time:.2f} seconds")
        else:
            print(f"Password not found within the specified length limit in {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute Force Password Cracker")
    parser.add_argument("password_file", help="File containing passwords to crack")
    parser.add_argument("--charset", default=string.ascii_letters + string.digits, help="Character set to use for cracking")
    parser.add_argument("--max_length", type=int, default=8, help="Maximum length of passwords to attempt")
    parser.add_argument("--num_threads", type=int, default=4, help="Number of threads to use")

    args = parser.parse_args()

    crack_passwords_from_file(args.password_file, args.charset, args.max_length, args.num_threads)
