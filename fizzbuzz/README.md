# 🧮 FizzBuzz Infrastructure

**Mathematical FizzBuzz counter with O(1) time complexity.**

## 📁 Project Structure

```
fizzbuzz/
├── core.py      # Business logic (10 lines)
├── tests.py     # Test suite (20 lines)
└── README.md    # This documentation
```

## 🔧 How It Works

**Mathematical Foundation:**
- `floor(n/3)` = all multiples of 3 → "Fizz"
- `floor(n/5)` = all multiples of 5 → "Buzz"
- `floor(n/15)` = intersection (LCM of 3,5) → "FizzBuzz"

**Formula:**
```python
fizz_only    = floor(n/3) - floor(n/15)
buzz_only    = floor(n/5) - floor(n/15)
fizzbuzz     = floor(n/15)
neither      = n - (floor(n/3) + floor(n/5) - floor(n/15))
```

## 🚀 Usage

```python
from core import count_fizzbuzz

result = count_fizzbuzz(100)
print(result['fizz'])      # 27
print(result['buzz'])      # 14
print(result['fizzbuzz'])  # 6
print(result['neither'])   # 53
```

## 🧪 Running Tests

```bash
python tests.py
```

## 🎯 Performance

- **Time**: O(1) - constant time regardless of n
- **Space**: O(1) - fixed memory usage
- **Accuracy**: 100% mathematical precision

---

*3 files, ~50 lines total - maintainable, testable, scalable*
