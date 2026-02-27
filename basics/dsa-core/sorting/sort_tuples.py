"""
Sort a List of Tuples by Primary and Secondary Keys

Given a list of tuples where each tuple contains two integers,
sort the list based on:

- Primary key → second element of the tuple (ascending order)
- Secondary key → first element of the tuple (ascending order)
  (Used only if second elements are equal)

Example:
Input: [(3,2), (1,2), (4,1), (2,1)]
Output: [(2,1), (4,1), (1,2), (3,2)]

Explanation:
First sort by second element:
(4,1), (2,1), (3,2), (1,2)

Among tuples with same second element:
Sort by first element.

Constraints:
- 1 <= len(list) <= 10^5
- Tuple elements are integers.
"""

def sort_keys(listoftuples):

    sec_sorted = sorted(listoftuples, key = lambda x: (x[1], x[0]))

    return sec_sorted

print(sort_keys([(3,2), (1,2), (4,1), (2,1)]))