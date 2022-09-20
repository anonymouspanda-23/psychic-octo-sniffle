import q2
import os

# Which function will be tested
FUNC = q2.change_case_n_times

TEST_CASES = [
    (('', 3), ''),
    (('GHQW', 4), 'ghqw'),
    (('aDTHQ', 0), 'aDTHQ'),
    (('JTE7tw$%bBG', 2), 'jtE7tw$%bBG'),
    (('apple', 7), 'apple')
]


def run_test(TEST_CASES, FUNC):
    results = []
    for case_number, input_answer in enumerate(TEST_CASES):
        print(f'Test #{case_number+1}:')
        print(f'Input: {input_answer[0]}')
        print(f'Expected output: {input_answer[1]}')
        print(f'Your function\'s output: {FUNC(*input_answer[0])}')
        print(f'Passed?: {(passed := input_answer[1]==FUNC(*input_answer[0]))}')
        print()
        results.append(passed)

    print('**** Final result: ')
    print('Your email ID: [', os.path.basename(
        os.path.dirname(os.path.realpath(__file__))), ']', sep='')
    print('(if your email id is wrong, please check your directory name)')
    print('Total cases passed: ', sum(results), f'(out of {len(TEST_CASES)})')


if __name__ == '__main__':
    run_test(TEST_CASES, FUNC)
