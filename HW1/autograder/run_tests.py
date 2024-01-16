"""
===================
EXAMPLE RESULT.JSON 
===================

{ "score": 44.0, // optional, but required if not on each test case below. Overrides total of tests if specified.
  "execution_time": 136, // optional, seconds
  "output": "Text relevant to the entire submission", // optional
  "output_format": "simple_format", // Optional output format settings, see "Output String Formatting" below
  "test_output_format": "text", // Optional default output format for test case outputs, see "Output String Formatting" below
  "test_name_format": "text", // Optional default output format for test case names, see "Output String Formatting" below
  "visibility": "after_due_date", // Optional visibility setting
  "stdout_visibility": "visible", // Optional stdout visibility setting
  "extra_data": {}, // Optional extra data to be stored
  "tests": // Optional, but required if no top-level score
    [
        {
            "score": 2.0, // optional, but required if not on top level submission
            "max_score": 2.0, // optional
            "status": "passed", // optional, see "Test case status" below
            "name": "Your name here", // optional
            "name_format": "text", // optional formatting for the test case name, see "Output String Formatting" below
            "number": "1.1", // optional (will just be numbered in order of array if no number given)
            "output": "Giant multiline string that will be placed in a <pre> tag and collapsed by default", // optional
            "output_format": "text", // optional formatting for the test case output, see "Output String Formatting" below
            "tags": ["tag1", "tag2", "tag3"], // optional
            "visibility": "visible", // Optional visibility setting
            "extra_data": {} // Optional extra data to be stored
        },
        // and more test cases...
    ],
  "leaderboard": // Optional, will set up leaderboards for these values
    [
      {"name": "Accuracy", "value": .926},
      {"name": "Time", "value": 15.1, "order": "asc"},
      {"name": "Stars", "value": "*****"}
    ]
}
"""

import json

results = {
    "score": 42.21,
    "output": "Your submission has been graded",
    "tests": [
        {
            "name": "Test 1",
            "score": 8.51,
            "max_score": 9,
            "output": "Test Case Test 1 Passed"
        },
        {
            "name": "Test 2",
            "score": 16.51,
            "max_score": 17,
            "output": "Test Case Test 2 Passed"
        },
        {
            "name": "Test 3",
            "score": 17.19,
            "max_score": 19,
            "output": "Test Case Test 3 Passed"
        }
    ]
}


with open('/autograder/results/results.json', 'w') as file:
    json.dump(results, file)