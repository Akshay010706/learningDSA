# 📚 Learning DSA - Data Structures & Algorithms Journey

<div align="center">

![DSA](https://img.shields.io/badge/Topic-DSA-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Language-Python-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Master Data Structures and Algorithms with hands-on coding examples and LeetCode problems**

[🎯 Quick Start](#quick-start) • [📖 Topics](#topics) • [💡 Resources](#resources) • [🤝 Contributing](#contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Folder Structure](#folder-structure)
- [Topics](#topics)
  - [Arrays](#arrays)
  - [Strings](#strings)
- [Learning Resources](#learning-resources)
- [LeetCode Problem Index](#leetcode-problem-index)
- [Contributing](#contributing)

---

## 🎯 Overview

This repository is a comprehensive collection of **Data Structures and Algorithms** implementations and solutions. It's designed for:

- 👨‍💻 **Beginners** learning fundamental algorithms
- 🎓 **Students** preparing for coding interviews
- 🚀 **Developers** improving problem-solving skills
- 📝 **Competitive Programmers** sharpening their algorithmic thinking

### Learning Philosophy
- **Theory + Practice**: Understand the concept, then code it
- **Multiple Approaches**: Learn different ways to solve problems
- **Progressive Difficulty**: Start with fundamentals, advance to complex problems
- **Real Interview Problems**: LeetCode problems from actual interviews

---

## 🚀 Quick Start

### Prerequisites
```bash
- Python 3.7+
- Basic understanding of programming concepts
```

### How to Use
```bash
# Clone the repository
git clone <this-repo>

# Navigate to a topic
cd Array/leetcodeimp/Easy

# Run any solution
python twosum.py
```

### Recommended Learning Path
1. **Start Here**: `Array/StartingAlgorithm/` - Master fundamental algorithms
2. **Learn Patterns**: `Array/leetcode8pattern/` - Understand common coding patterns
3. **Apply Knowledge**: `Array/leetcodeimp/` - Solve real LeetCode problems
4. **Practice Strings**: `Strings/` - Master string manipulation

---

## 📁 Folder Structure

```
learningDSA/
│
├── 📊 Array/                           # Array data structure problems
│   ├── StartingAlgorithm/              # Fundamental algorithms
│   │   ├── 1D_kadaneAlgo.py            # Maximum subarray sum (1D)
│   │   ├── 2D_Kadanesalgo.py           # Maximum subarray sum (2D)
│   │   ├── 2sumand3sum.py              # Two sum and three sum problems
│   │   ├── DNFalgo.py                  # Dutch National Flag algorithm
│   │   ├── jugglingalogrithm.py        # Array rotation technique
│   │   └── mooresvotingalgo.py         # Majority element algorithm
│   │
│   ├── leetcode8pattern/               # Common coding patterns
│   │   └── 1_twopointer.py             # Two-pointer technique
│   │
│   ├── leetcodeimp/                    # LeetCode problems by difficulty
│   │   ├── Easy/                       # Easy level problems
│   │   │   ├── twosum.py               # Two Sum
│   │   │   ├── Contains_Duplicate.py   # Contains Duplicate
│   │   │   ├── Maximum_Subarray.py     # Maximum Subarray
│   │   │   └── best_timetobuy_stock.py # Best Time to Buy and Sell Stock
│   │   ├── Medium/                     # Medium level problems
│   │   │   └── Product_of_Array_Except_Self.py
│   │   └── hard/                       # Hard level problems
│   │
│   └── Sorthingalgorithm/              # Sorting techniques (in progress)
│
├── 🔤 Strings/                         # String manipulation problems
│   ├── leetcodepattern/                # String patterns and techniques
│   │   ├── KMP_Alogo.py                # KMP pattern matching algorithm
│   │   ├── Valid_Anagram.py            # Anagram detection
│   │   └── KMP_Algo.jpeg               # KMP algorithm visualization
│   │
│   └── leetcodeimp/                    # LeetCode string problems (in progress)
│
└── README.md                           # This file!
```

---

## 📖 Topics

### 📊 Arrays

Arrays are fundamental data structures used in almost every coding problem. Master the following concepts:

#### 🎓 Starting Algorithms

| Algorithm | File | Complexity | Use Case |
|-----------|------|-----------|----------|
| **Kadane's Algorithm (1D)** | [1D_kadaneAlgo.py](Array/StartingAlgorithm/1D_kadaneAlgo.py) | O(n) | Maximum subarray sum |
| **Kadane's Algorithm (2D)** | [2D_Kadanesalgo.py](Array/StartingAlgorithm/2D_Kadanesalgo.py) | O(n²) | Max sum in 2D matrix |
| **Two Sum & Three Sum** | [2sumand3sum.py](Array/StartingAlgorithm/2sumand3sum.py) | O(n²) | Finding target sum pairs |
| **Dutch National Flag** | [DNFalgo.py](Array/StartingAlgorithm/DNFalgo.py) | O(n) | Partitioning (0s, 1s, 2s) |
| **Juggling Algorithm** | [jugglingalogrithm.py](Array/StartingAlgorithm/jugglingalogrithm.py) | O(n) | Array rotation |
| **Moore's Voting** | [mooresvotingalgo.py](Array/StartingAlgorithm/mooresvotingalgo.py) | O(n) | Finding majority element |

#### 🎯 Common Patterns

| Pattern | File | Description |
|---------|------|-------------|
| **Two Pointer** | [1_twopointer.py](Array/leetcode8pattern/1_twopointer.py) | Move two pointers from ends/start |

#### 💪 LeetCode Problems

**Easy Level** - Build your confidence!
- [❓ Two Sum](Array/leetcodeimp/Easy/twosum.py) - Find two numbers that add up to target
- [✓ Contains Duplicate](Array/leetcodeimp/Easy/Contains_Duplicate.py) - Check for duplicate elements
- [📈 Maximum Subarray](Array/leetcodeimp/Easy/Maximum_Subarray.py) - Find contiguous subarray with max sum
- [💰 Best Time to Buy and Sell Stock](Array/leetcodeimp/Easy/best_timetobuy_stock.py) - Maximize profit from one transaction

**Medium Level** - Level up your skills!
- [🎁 Product of Array Except Self](Array/leetcodeimp/Medium/Product_of_Array_Except_Self.py) - Calculate product without division

**Hard Level** - Ultimate challenge!
- (Coming Soon... 🚀)

---

### 🔤 Strings

Master string manipulation and pattern matching algorithms.

#### 🎓 String Patterns & Algorithms

| Algorithm | File | Complexity | Concept |
|-----------|------|-----------|---------|
| **KMP (Knuth-Morris-Pratt)** | [KMP_Alogo.py](Strings/leetcodepattern/KMP_Alogo.py) | O(n+m) | Efficient pattern matching |
| **Valid Anagram** | [Valid_Anagram.py](Strings/leetcodepattern/Valid_Anagram.py) | O(n) | Character frequency matching |

**Visual Guides:**
- 📊 [KMP Algorithm Visualization](Strings/leetcodepattern/KMP_Algo.jpeg) - Visual explanation of KMP

---

## 📚 Learning Resources

### How to Learn Effectively

```
1️⃣  READ the algorithm explanation
2️⃣  UNDERSTAND the logic and approach
3️⃣  CODE it yourself first (without copying)
4️⃣  TRACE through examples
5️⃣  COMPARE with multiple approaches
6️⃣  PRACTICE on LeetCode
7️⃣  OPTIMIZE for time & space complexity
```

### Algorithm Complexity Reference

| Complexity | Time | Space | Real World |
|-----------|------|-------|-----------|
| O(1) | Instant | Instant | Hash lookup |
| O(log n) | Binary Search | Efficient | Searching sorted data |
| O(n) | Linear | Proportional | Single loop |
| O(n log n) | Sorting | Efficient | Merge sort, Quick sort |
| O(n²) | Slow | Quadratic | Bubble sort, Nested loops |
| O(2ⁿ) | Very Slow | Exponential | Recursive algorithms |

### Key Concepts to Master

- ✅ **Time & Space Complexity** - Analyze algorithm efficiency
- ✅ **Two Pointer Technique** - Solve array problems optimally
- ✅ **Sliding Window** - Process contiguous subarrays
- ✅ **Prefix/Suffix** - Precompute values for optimization
- ✅ **Dynamic Programming** - Build solutions bottom-up
- ✅ **Pattern Matching** - String algorithms like KMP, Rabin-Karp

---

## 🔍 LeetCode Problem Index

### By Difficulty

<details>
<summary><b>Easy (4 problems)</b> - Start here! 🟢</summary>

1. Two Sum
2. Contains Duplicate
3. Maximum Subarray
4. Best Time to Buy and Sell Stock

</details>

<details>
<summary><b>Medium (1 problem)</b> - Level up! 🟡</summary>

1. Product of Array Except Self

</details>

<details>
<summary><b>Hard (TBD)</b> - Master challenge! 🔴</summary>

Coming soon...

</details>

### By Topic

| Topic | Easy | Medium | Hard |
|-------|------|--------|------|
| **Array - Two Sum Variants** | 1 | 1 | - |
| **Array - Subarrays** | 1 | - | - |
| **Array - Stock Trading** | 1 | - | - |
| **Array - Duplicates** | 1 | - | - |
| **Strings** | - | - | - |

---

## 💡 Tips for Interview Success

### Before You Code
- [ ] Ask clarifying questions
- [ ] Discuss edge cases
- [ ] Mention your approach & complexity
- [ ] Walk through an example

### While Coding
- [ ] Write clean, readable code
- [ ] Add comments for complex logic
- [ ] Test with edge cases
- [ ] Optimize if time permits

### Common Pitfalls to Avoid
- ❌ Not handling edge cases (empty array, single element, duplicates)
- ❌ Off-by-one errors in loops
- ❌ Forgetting about integer overflow
- ❌ Not considering optimal solution before coding
- ❌ Poor variable naming

---

## 🤝 Contributing

We'd love to see this repository grow! Here's how you can contribute:

### Adding New Solutions
1. Create a well-commented solution
2. Follow the existing naming convention
3. Include time and space complexity
4. Add test cases if applicable
5. Update this README

### Improvement Ideas
- [ ] Add more LeetCode problems
- [ ] Create visual explanations
- [ ] Add practice problems
- [ ] Explain advanced techniques
- [ ] Create difficulty progressions

---

## 📈 Progress Tracker

Track your learning journey:

```
[ ] Foundation Algorithms (StartingAlgorithm/)
  [x] Kadane's Algorithm
  [x] Two Sum & Three Sum
  [x] Dutch National Flag
  [x] Juggling Algorithm
  [x] Moore's Voting Algorithm
  
[ ] Array Patterns (leetcode8pattern/)
  [x] Two Pointer Technique
  
[ ] Easy LeetCode Problems (leetcodeimp/Easy/)
  [x] Two Sum
  [x] Contains Duplicate
  [x] Maximum Subarray
  [x] Best Time to Buy and Sell Stock
  
[ ] Medium LeetCode Problems (leetcodeimp/Medium/)
  [x] Product of Array Except Self
  
[ ] Hard LeetCode Problems (leetcodeimp/hard/)
  [ ] (Coming Soon)
  
[ ] String Algorithms (Strings/)
  [x] KMP Algorithm
  [x] Valid Anagram
```

---

## 🎓 Learning Milestones

- 🟢 **Beginner**: Complete all starting algorithms
- 🟡 **Intermediate**: Solve all easy LeetCode problems
- 🟠 **Advanced**: Master all medium problems
- 🔴 **Expert**: Conquer hard problems with optimal solutions

---

## 📞 Questions?

If you have questions about any algorithm or problem:

1. Check the code comments and examples
2. Review the complexity analysis
3. Try solving the problem yourself first
4. Look at alternative approaches

---

## 📄 License

This repository is open source under the MIT License - feel free to use it for learning!

---

## 🌟 Show Your Support

If this repository helped you learn DSA:
- ⭐ Give it a star
- 📢 Share with others
- 🔄 Contribute solutions
- 💬 Provide feedback

---

<div align="center">

**Happy Learning! Keep Coding! 🚀**

*Last Updated: 2024*

</div>