import q1a
import os

# Which function will be tested
FUNC = q1a.check_ascending_number

TEST_CASES = [
    (123, True),
    (3, True),
    (82, False),
    (0, True),
    (123456789, True)
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
