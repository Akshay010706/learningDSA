# 📚 Learning DSA (Data Structures & Algorithms)

> A comprehensive, actively-developing repository documenting my journey through **Data Structures and Algorithms** with implementations in **Python** (76.6%) and **C++** (23.4%).

<div align="center">

![Status](https://img.shields.io/badge/Status-Under%20Development-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-76.6%25-3776ab?style=flat-square&logo=python)
![C++](https://img.shields.io/badge/C%2B%2B-23.4%25-00599C?style=flat-square&logo=c%2B%2B)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Last Updated](https://img.shields.io/badge/Last%20Updated-June%202026-blue?style=flat-square)

**Master DSA with hands-on implementations, multiple languages, and real LeetCode problems**

[🎯 Quick Start](#-quick-start) • [📖 Structure](#-repository-structure) • [💻 Languages](#-language-implementations) • [🚀 Getting Started](#-getting-started)

</div>

---

## 📋 Table of Contents

- [About This Project](#-about-this-project)
- [Quick Start](#-quick-start)
- [Repository Structure](#-repository-structure)
- [Language Implementations](#-language-implementations)
- [Getting Started](#-getting-started)
- [Recommended Learning Path](#-recommended-learning-path)
- [Development Status](#-development-status)
- [Contributing](#-contributing)
- [Learning Resources](#-learning-resources)

---

## 🎯 About This Project

This repository is my **active learning journey** through Data Structures and Algorithms. It's designed as a:

✅ **Comprehensive Reference** - Well-organized implementations with explanations  
✅ **Dual-Language Practice** - Python for rapid development, C++ for performance  
✅ **Interview Preparation** - Real LeetCode and interview problems  
✅ **Learning Playground** - Experimenting with different approaches and optimizations  
⚠️ **Work in Progress** - Expect frequent updates, refactoring, and new content

### Perfect For:
- 👨‍💻 **Beginners** learning fundamental DSA concepts
- 🎓 **Students** preparing for coding interviews
- 🚀 **Developers** improving algorithmic thinking
- 📝 **Competitive Programmers** sharpening skills
- 🔄 **Anyone** wanting to learn in multiple languages

---

## 🚀 Quick Start

### Prerequisites

**For Python:**
```bash
Python 3.7 or higher
```

**For C++:**
```bash
GCC, Clang, or MSVC compiler
C++11 standard or higher
```

### Clone & Explore

```bash
# Clone the repository
git clone https://github.com/Akshay010706/learningDSA.git
cd learningDSA

# Run a Python example
cd Python/Array/StartingAlgorithm
python3 1D_kadaneAlgo.py

# Compile and run a C++ example
cd C++
g++ -std=c++11 -o solution solution.cpp
./solution
```

---

## 📁 Repository Structure

```
learningDSA/
│
├── 📂 Python/                              # Python implementations (76.6%)
│   │
│   ├── 📂 Array/                          # Array data structures & algorithms
│   │   │
│   │   ├── 📂 StartingAlgorithm/         # Fundamental algorithms
│   │   │   ├── 1D_kadaneAlgo.py          # Kadane's Algorithm (1D)
│   │   │   ├── 2D_Kadanesalgo.py         # Kadane's Algorithm (2D)
│   │   │   ├── 2sumand3sum.py            # Two Sum & Three Sum Problems
│   │   │   ├── DNFalgo.py                # Dutch National Flag Algorithm
│   │   │   ├── jugglingalogrithm.py      # Juggling Algorithm (Array Rotation)
│   │   │   └── mooresvotingalgo.py       # Moore's Voting Algorithm
│   │   │
│   │   ├── 📂 leetcode8pattern/          # Common coding patterns
│   │   │   └── 1_twopointer.py           # Two-pointer technique
│   │   │
│   │   ├── 📂 searchingalgorithm/        # Searching techniques
│   │   │   ├── binarysearch.py           # Binary Search
│   │   │   └── linearsearch.py           # Linear Search
│   │   │
│   │   └── 📂 leetcodeimp/               # LeetCode problems by difficulty
│   │       │
│   │       ├── 📂 Easy/                  # Easy level problems
│   │       │   ├── twosum.py             # Two Sum (LeetCode #1)
│   │       │   ├── Contains_Duplicate.py # Contains Duplicate (LeetCode #217)
│   │       │   ├── Maximum_Subarray.py   # Maximum Subarray (LeetCode #53)
│   │       │   └── best_timetobuy_stock.py # Best Time to Buy and Sell Stock
│   │       │
│   │       └── 📂 Medium/                # Medium level problems
│   │           └── Product_of_Array_Except_Self.py # Product of Array Except Self
│   │
│   └── 📂 Strings/                        # String manipulation (coming soon)
│
├── 📂 C++/                                 # C++ implementations (23.4%)
│       (Structure to be populated)
│
└── README.md                              # This file
```

---

## 💻 Language Implementations

### Python (76.6%) ✅ Active

**Current Implementation:**
- ✅ Array algorithms and patterns
- ✅ Searching algorithms (Linear & Binary Search)
- ✅ LeetCode problems (Easy & Medium)
- 📝 String implementations (Coming soon)

**Why Python for DSA?**
- ✨ Clean, readable syntax - focus on algorithms, not syntax
- 🚀 Rapid development and testing
- 📚 Excellent for prototyping and learning
- 🧪 Easy debugging and visualization

**Example (Kadane's Algorithm):**
```python
# Python/Array/StartingAlgorithm/1D_kadaneAlgo.py
def maxSubArraySum(arr):
    """Find maximum sum of contiguous subarray - O(n) solution"""
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far
```

### C++ (23.4%) 📋 Planned

**Why C++ for DSA?**
- ⚡ Performance-critical implementations
- 🎯 Competitive programming requirements
- 💾 Memory management & optimization
- 🏆 Many interview companies use C++

**Status:** Folder structure created, implementations coming soon!

---

## 🎓 Getting Started

### Recommended Learning Path

**Phase 1: Foundation Algorithms** 
Start with `Python/Array/StartingAlgorithm/` to master the basics:
1. [1D Kadane's Algorithm](Python/Array/StartingAlgorithm/1D_kadaneAlgo.py) - Maximum subarray sum
2. [2D Kadane's Algorithm](Python/Array/StartingAlgorithm/2D_Kadanesalgo.py) - 2D matrix maximum
3. [2Sum & 3Sum](Python/Array/StartingAlgorithm/2sumand3sum.py) - Finding target pairs
4. [Dutch National Flag](Python/Array/StartingAlgorithm/DNFalgo.py) - Partitioning arrays
5. [Juggling Algorithm](Python/Array/StartingAlgorithm/jugglingalogrithm.py) - Array rotation
6. [Moore's Voting](Python/Array/StartingAlgorithm/mooresvotingalgo.py) - Finding majority element

**Phase 2: Search Techniques**
Master searching in `Python/Array/searchingalgorithm/`:
1. [Linear Search](Python/Array/searchingalgorithm/linearsearch.py)
2. [Binary Search](Python/Array/searchingalgorithm/binarysearch.py)

**Phase 3: Common Patterns**
Learn coding patterns in `Python/Array/leetcode8pattern/`:
1. [Two Pointer Technique](Python/Array/leetcode8pattern/1_twopointer.py)

**Phase 4: LeetCode Practice**
Solve real interview problems in `Python/Array/leetcodeimp/`:

**Easy Level:**
- [Two Sum](Python/Array/leetcodeimp/Easy/twosum.py)
- [Contains Duplicate](Python/Array/leetcodeimp/Easy/Contains_Duplicate.py)
- [Maximum Subarray](Python/Array/leetcodeimp/Easy/Maximum_Subarray.py)
- [Best Time to Buy and Sell Stock](Python/Array/leetcodeimp/Easy/best_timetobuy_stock.py)

**Medium Level:**
- [Product of Array Except Self](Python/Array/leetcodeimp/Medium/Product_of_Array_Except_Self.py)

### Running Examples

**Python:**
```bash
# Navigate to the specific folder
cd Python/Array/StartingAlgorithm

# Run any Python file
python3 1D_kadaneAlgo.py
```

**C++:**
```bash
# Navigate to C++ folder
cd C++

# Compile and run (once implemented)
g++ -std=c++11 -o solution solution.cpp
./solution
```

---

## 📊 Current Progress

### Python Array Section
| Topic | Files | Status |
|-------|-------|--------|
| **Starting Algorithms** | 6 files | ✅ Complete |
| **Searching Algorithms** | 2 files | ✅ Complete |
| **Coding Patterns** | 1 file | 🔄 In Progress |
| **LeetCode Easy** | 4 files | ✅ Complete |
| **LeetCode Medium** | 1 file | ✅ Complete |
| **Strings** | 0 files | 📋 Planned |

### C++ Section
| Topic | Status |
|-------|--------|
| **All Implementations** | 📋 Planned |

---

## 💡 Quick Reference

### Big O Complexity Cheat Sheet

```
O(1)       - Constant time      (hash map lookup)
O(log n)   - Logarithmic        (binary search)
O(n)       - Linear             (simple loop)
O(n²)      - Quadratic          (nested loops)
O(n log n) - Linearithmic       (efficient sorting)
O(2ⁿ)      - Exponential        (recursion without memoization)
O(n!)      - Factorial          (permutations)
```

### Common Array Patterns

| Pattern | Example Problem | Use Case |
|---------|-----------------|----------|
| **Two Pointer** | Two Sum, 3Sum | Finding pairs/triplets |
| **Sliding Window** | Max length substring | Contiguous subarrays |
| **Prefix Sum** | Product of Array Except Self | Efficient calculations |
| **Kadane's Algorithm** | Maximum Subarray | Max/min subarray sum |
| **Binary Search** | Search in sorted array | Fast searching |

---

## 📈 Development Status

### Current Phase: 🔄 **Active Development**

This repository is **actively being built** and regularly updated. You may encounter:

✨ **What to Expect:**
- ✅ Well-documented Python implementations
- ✅ Comments explaining algorithm logic
- ✅ Time & Space complexity analysis
- ✅ Real LeetCode interview problems
- ✅ Working code examples

⚠️ **What's Still Changing:**
- 🔨 C++ implementations (planned)
- 📝 Reorganizing content for clarity
- ➕ Adding more LeetCode problems
- 🐛 Fixing any identified issues
- 📖 Expanding explanations

**Note:** This is intentional! Part of learning is revisiting and improving solutions. Feel free to watch, star, and check back often! 🌟

---

## 🎯 Interview Preparation

This repository covers essential patterns for coding interviews:

| Pattern | Topics Covered | Difficulty |
|---------|---|-----------|
| **Arrays** | Two Sum, Subarray, Stock Trading | Easy-Medium |
| **Searching** | Linear & Binary Search | Easy |
| **Two Pointers** | Partitioning, Sum problems | Medium |
| **Algorithms** | Sorting, Searching, Rotating | Easy-Medium |

---

## 🤝 Contributing

This is a personal learning project, but contributions and suggestions are welcome!

### How to Contribute

1. **Report Issues** - Found a bug or unclear explanation? [Open an issue](https://github.com/Akshay010706/learningDSA/issues)
2. **Suggest Improvements** - Have better solutions? Create a discussion
3. **Add Solutions** - Contribute new problems or C++ implementations

### Contribution Guidelines

When adding new solutions:
- ✅ Include clear, well-commented code
- ✅ Specify Time and Space complexity
- ✅ Provide example test cases
- ✅ Update this README
- ✅ Follow existing code style

---

## 📚 Learning Resources

### Free Online Platforms
- **LeetCode** - https://leetcode.com (Interview-style problems)
- **HackerRank** - https://www.hackerrank.com (Algorithm practice)
- **GeeksforGeeks** - https://www.geeksforgeeks.org (Theory + implementations)
- **InterviewBit** - https://www.interviewbit.com (Structured learning paths)
- **CodeSignal** - https://codesignal.com (Gamified challenges)

### Recommended Books
- **Introduction to Algorithms** (CLRS) - The classic reference
- **Cracking the Coding Interview** - Interview-focused
- **Algorithm Design Manual** - Problem-solving strategies
- **Data Structures and Algorithms Made Easy** - Simplified explanations

### YouTube Channels
- **Abdul Bari** - Excellent DSA explanations
- **William Fiset** - Graph algorithms & visualizations
- **Kunal Kushwaha** - Complete DSA course
- **CodeHelp** - Hindi & English tutorials

---

## 📞 Support & Questions

### Having Trouble?

1. **Check existing solutions** - Browse the relevant folder
2. **Read the comments** - Code is well-documented
3. **Trace through examples** - Step through the algorithm
4. **Try implementing first** - Don't just copy-paste
5. **Open an issue** - If still stuck

### Learning Tips

💡 **For Best Results:**
- 👨‍💻 Code along - don't just read
- 🧪 Modify and experiment with solutions
- 📝 Write your own comments
- 🔄 Revisit problems after a few days
- 🏆 Track your progress!

---

## 📄 License

This repository is open source under the **MIT License** - feel free to use it for learning and personal projects.

---

## 🌟 Show Your Support

If this repository helped you with your DSA journey:

- ⭐ **Star the repository** - helps others discover it
- 📢 **Share with friends** - spread the knowledge
- 🔄 **Contribute solutions** - help the community
- 💬 **Provide feedback** - help improve the project

---

<div align="center">

## 🚀 Ready to Master DSA?

**Pick a topic from the repository structure and start learning!**

### Remember:
```
"The only way to learn a new programming language is by writing programs in it."
                                                          — Dennis Ritchie

Consistency beats intensity. Code a little every day! 💪
```

**Happy Learning! Keep Coding! 📚💻**

*Last Updated: June 2026 | Actively Maintained | Open to Contributions*

[![Python](https://img.shields.io/badge/Made%20with-Python%20%26%20C%2B%2B-blue?style=flat-square)](https://github.com/Akshay010706/learningDSA)
[![GitHub](https://img.shields.io/badge/GitHub-Akshay010706-success?style=flat-square&logo=github)](https://github.com/Akshay010706)

</div>
