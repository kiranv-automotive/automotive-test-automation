import csv
from collections import defaultdict

def read_test_log(filename):
    results = []
    with open(filename, newline='',  encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            results.append(row)
    return results

def analyze_results(results):
    total = len(results)
    passed = [r for r in results if r['result'] == 'PASS']
    failed = [r for r in results if r['result'] == 'FAIL']
    pass_rate = (len(passed) / total) * 100

    print("=" * 45)
    print("  AUTOMOTIVE TEST LOG SUMMARY")
    print("=" * 45)
    print(f"  Total tests   : {total}")
    print(f"  Passed        : {len(passed)}")
    print(f"  Failed        : {len(failed)}")
    print(f"  Pass rate     : {pass_rate:.1f}%")
    print("=" * 45)

    if failed:
        print("\n  FAILED TEST CASES:")
        for r in failed:
            print(f"  [{r['test_id']}] {r['feature']}")
            print(f"        -> {r['comment']}")

    print("\n  PASSED TEST CASES:")
    for r in passed:
        print(f"  [{r['test_id']}] {r['feature']}")

def main():
    filename = 'test_log.csv'
    results = read_test_log(filename)
    analyze_results(results)

if __name__ == '__main__':
    main()