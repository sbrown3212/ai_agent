from functions.get_file_info import get_files_info


print("--- Test 1 ---")
test_1_result = get_files_info("calculator", ".")
print(test_1_result)

print("--- Test 2 ---")
test_2_result = get_files_info("calculator", "pkg")
print(test_2_result)

print("--- Test 3 ---")
test_3_result = get_files_info("calculator", "/bin")
print(test_3_result)

print("--- Test 4 ---")
test_4_result = get_files_info("calculator", "../")
print(test_4_result)
