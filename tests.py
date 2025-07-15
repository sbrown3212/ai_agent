# from functions.get_file_info import get_files_info
# from functions.get_file_content import get_file_content
# from config import MAX_CHARS
from functions.write_file import write_file


def tests():
    # --- Tests for 'write_file' ---
    print("lorem.txt:")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    print("\nmorelorem.txt:")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    print("\ntemp.txt (expecting error):")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

    # # --- Tests for 'get_file_content' ---
    # # main.py
    # print("Result for 'main.py':")
    # result = get_file_content("calculator", "main.py")
    # print(result)
    #
    # # pkg/calculator.py
    # print("Result for 'pkg/calculator.py':")
    # result = get_file_content("calculator", "pkg/calculator.py")
    # print(result)
    #
    # # /bin/cat
    # print("Result for '/bin/cat':")
    # result = get_file_content("calculator", "/bin/cat")
    # print(result)
    #
    # Lorem.txt
    # print("Result from 'get_file_content()' for 'lorem.txt':")
    # working_directory = "calculator"
    # file_path = "lorem.txt"
    # result = get_file_content(working_directory, file_path)
    #
    # # result = get_file_content("calculator", "lorem.txt")
    # is_truncated = result.endswith(
    #     f'...File "{file_path}" truncated at {MAX_CHARS} characters]'
    # )
    # print(f"'lorem.txt' is truncated: {is_truncated}")
    # print(result)

    # --- Tests for 'get_file_info' ---
    # print("--- Test 1 ---")
    # test_1_result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(test_1_result)
    #
    # print("--- Test 2 ---")
    # test_2_result = get_files_info("calculator", "pkg")
    # print('Result for "pkg" directory:')
    # print(test_2_result)
    #
    # print("--- Test 3 ---")
    # test_3_result = get_files_info("calculator", "/bin")
    # print('Result for "/bin" directory:')
    # print(test_3_result)
    #
    # print("--- Test 4 ---")
    # test_4_result = get_files_info("calculator", "../")
    # print('Result for "../" directory:')
    # print(test_4_result)


if __name__ == "__main__":
    tests()
