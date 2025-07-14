from functions.get_file_info import get_files_info


def tests():
    print("--- Test 1 ---")
    test_1_result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(test_1_result)

    print("--- Test 2 ---")
    test_2_result = get_files_info("calculator", "pkg")
    print('Result for "pkg" directory:')
    print(test_2_result)

    print("--- Test 3 ---")
    test_3_result = get_files_info("calculator", "/bin")
    print('Result for "/bin" directory:')
    print(test_3_result)

    print("--- Test 4 ---")
    test_4_result = get_files_info("calculator", "../")
    print('Result for "../" directory:')
    print(test_4_result)


if __name__ == "__main__":
    tests()
