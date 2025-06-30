# python-opp-examples
OOP-style solutions to Python coding tasks 

## What's inside
- 'sequence_generetors.py': Classes ArithmeticProgression and GeometricProgression for generating members of arithmetic and geometric progression.
- 'domain_validator.py': The Domain class is used for working with domains. It has three ways to create an instance: directly through a class call or using the from_url() or from_email() methods.
- 'high_score_table.py': The table allows you to view current records and add new results.
- 'paginator.py': The Pagination class is used to handle paginated data. Pagination is used to divide a large amount of data into parts.
                  1. prev_page() — go back to the previous page,
                  2. next_page() — go to the next page,
                  3. first_page() — go back to the first page,
                  4. last_page() — go to the last page,
                  5. go_to_page() — go to the page with the specified number (1 — first page, 2 — second page, and so on).
  - 'exam_tests.py': The Testpaper class allows you to create exam tests. Each test is created based on a topic, a scheme of correct answers, and a minimum percentage of correct solutions. The created tests are passed by a student — an instance of the Student class. It has a take_test() method that takes a test and the student's answers to this test as arguments. The test results are available as a dictionary, the key of which is the test topic, and the value is the test result (passed or failed) and the percentage of correct solutions.
