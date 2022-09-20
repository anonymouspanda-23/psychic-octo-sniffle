import q1b
import os

# Which function will be tested
FUNC = q1b.find_ascending_numbers

TEST_CASES = [
    ([], []),
    ([1], [1]),
    ([123, 312, 45612, 34567], [123, 34567]),
    ([1, 23, 654, 23345], [1, 23]),
    ([256, 2, 11, 35, 1358, 123456789], [256, 2, 35, 1358, 123456789])
]


def run_test(TEST_CASES, FUNC):
    results = []
    for case_number, input_answer in enumerate(TEST_CASES):
        print(f'Test #{case_number+1}:')
        print(f'Input: {input_answer[0]}')
        print(f'Expected output: {input_answer[1]}')
        print(f'Your function\'s output: {FUNC(input_answer[0])}')
        print(f'Passed?: {(passed := input_answer[1]==FUNC(input_answer[0]))}')
        print()
        results.append(passed)

    print('**** Final result: ')
    print('Your email ID: [', os.path.basename(
        os.path.dirname(os.path.realpath(__file__))), ']', sep='')
    print('(if your email id is wrong, please check your directory name)')
    print('Total cases passed: ', sum(results), f'(out of {len(TEST_CASES)})')


if __name__ == '__main__':
    run_test(TEST_CASES, FUNC)
