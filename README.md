# Learning DSA with a Custom Terminal-Based Testing Platform

**Author:** [Krishnarjun Mitra](https://github.com/Krishnarjunmitra)

[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
[![GitHub issues](https://img.shields.io/github/issues/Krishnarjunmitra/Learning-DSA)](https://github.com/Krishnarjunmitra/Learning-DSA/issues)
[![GitHub stars](https://img.shields.io/github/stars/Krishnarjunmitra/Learning-DSA)](https://github.com/Krishnarjunmitra/Learning-DSA/stargazers)

> A modern approach to learning Data Structures and Algorithms with an integrated testing platform

## 📚 Overview

Learning DSA is a comprehensive repository designed to make learning Data Structures and Algorithms accessible and effective. It combines theoretical knowledge with practical implementation through an integrated testing platform. This repository serves as both a learning resource and a development environment where you can practice DSA problems with a LeetCode-like testing experience.

## ✨ Features

- **Structured Learning**: Organized theoretical content with code implementations
- **Interactive Testing Platform**: Test your solutions with a custom-built runner
- **LeetCode-like Experience**: Familiar format for solving and testing problems
- **Colorful Terminal Output**: Clear, visual feedback on test results
- **Smart Test Display**: Focus on what matters - failures and important test cases
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🗂️ Repository Structure

```
LEARNING DSA/
├── Theories/                 # Theoretical concepts with implementations
│   ├── Data Structure/      # Core data structures (Array, Linked List, Stack, Queue, Tree, etc.)
│   ├── Sorting/             # Sorting algorithms (Bubble, Quick, Merge, Heap, etc.)
│   ├── Searching/           # Searching algorithms (Linear, Binary, Jump, etc.)
│   ├── DP/                  # Dynamic Programming and Divide & Conquer
│   ├── Greedy/              # Greedy algorithms
│   ├── Bitwise/             # Bit manipulation techniques
│   ├── Graphs/              # Graph algorithms (BFS, DFS, etc.)
│   ├── Trees/               # Tree algorithms (Traversals, Segment Trees, etc.)
│   ├── NumberTheory/        # Number theory algorithms (GCD, Sieve, etc.)
│   ├── Strings/             # String algorithms (KMP, Rabin-Karp, etc.)
│   ├── Geometry/            # Geometry algorithms (Convex Hull, etc.)
│   ├── Randomized/          # Randomized algorithms
│   ├── Compression/         # Data compression algorithms (Huffman, RLE)
│   ├── Caching/             # Caching and LRU cache
│   ├── Memory/              # Memory management (GC, reference counting)
│   ├── Analysis/            # Amortized and complexity analysis
│   ├── Hashing/             # Hashing techniques
│   ├── DisjointSet/         # Disjoint set/Union-Find
│   ├── Heaps/               # Advanced heaps (Fibonacci, Pairing)
│   ├── Persistence/         # Persistent data structures
│   ...                      # (Add more as you expand)
│
├── my-dsa-platform/          # Interactive testing platform
│   ├── data/                 # Your solution files
│   │   └── 1. Extract Digits.py  # Example solution file
│   │
│   ├── test_cases/           # Test cases corresponding to solutions
│   │   └── 1. Extract Digits test case.json  # Example test file
│   │
│   ├── package.json          # Project metadata and dependencies
│   └── test_runner.py        # Testing framework script
│
└── README.md                 # Repository documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Krishnarjunmitra/Learning-DSA.git
   cd Learning-DSA
   ```

2. Install dependencies:
   ```bash
   pip install colorama
   ```

### Using the DSA Platform

1. Navigate to the platform directory:
   ```bash
   cd my-dsa-platform
   ```

2. Run a test for an existing problem:
   ```bash
   python test_runner.py 1
   ```
   This will run tests for "1. Extract Digits.py" using the corresponding test case file.

3. Create your own solution file:
   - Add a new file in the `data` directory with a numerical prefix (e.g., `2. Reverse String.py`)
   - Implement your solution using the `Solution` class pattern:
     ```python
     class Solution:
         def your_function_name(self, param1, param2):
             # Your solution here
             return result
     ```

4. Create corresponding test case file:
   - Add a new JSON file in the `test_cases` directory with the same numerical prefix
   - Format it as follows:
     ```json
     {
       "function": "your_function_name",
       "inputs": [["input1_case1", "input2_case1"], ["input1_case2", "input2_case2"]],
       "expected": ["expected_output_case1", "expected_output_case2"]
     }
     ```

5. Run your new tests:
   ```bash
   python test_runner.py 2
   ```

## 💡 What Makes This Repository Unique

### Integrated Learning Environment

Unlike traditional DSA resources that separate theory from practice, this repository combines comprehensive theoretical content with an interactive testing platform. This integration allows for immediate application of concepts learned.

### Professional Testing Experience

The custom test runner provides a professional, LeetCode-like experience with:
- Colorful, clear output
- Smart display of test results (showing only important test cases)
- Detailed performance metrics
- Cross-platform compatibility

### Focus on Real Understanding

By implementing both the theoretical components and the testing platform from scratch, users gain a deeper understanding of DSA concepts and software development principles simultaneously.

### Expandable Framework

The structure allows for continuous addition of new problems and concepts, making it a living repository that grows with your learning journey.

## 🔧 Customizing Test Display

You can customize how test results are displayed by modifying the `DisplayConfig` class in `test_runner.py`:

```python
class DisplayConfig:
    # Maximum number of passing tests to show
    MAX_PASS_DISPLAY = 3
    # Maximum number of failing tests to show
    MAX_FAIL_DISPLAY = 3
    # Whether to show detailed inputs/outputs for passing tests
    SHOW_PASS_DETAILS = True
    # Whether to always show the first test case regardless of pass/fail
    ALWAYS_SHOW_FIRST_TEST = True
```

## 🤝 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Add your contributions:
   - New DSA theory with implementations in the `Theories` directory
   - New problems with test cases in the platform directories
   - Improvements to the test runner
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Making It Open Source

The repository is already published under the ISC license, which is an open-source license. To make it more accessible to the community:

1. Ensure documentation is thorough and welcoming to newcomers
2. Add contributing guidelines in a CONTRIBUTING.md file
3. Add a CODE_OF_CONDUCT.md file
4. Consider setting up GitHub Actions for automated testing
5. Add issue templates to standardize bug reports and feature requests

## 📝 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

- **Krishnarjun Mitra** - [GitHub Profile](https://github.com/Krishnarjunmitra)

## 🙏 Acknowledgements

- LeetCode for inspiration on the problem-solving format
- All contributors who help improve this repository
- The open-source community for providing valuable resources

---

*Happy Learning and Coding!* 🚀