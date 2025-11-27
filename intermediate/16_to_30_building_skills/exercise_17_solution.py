# Exercise 17: Dictionary Merger - SOLUTION
# Difficulty: Beginner+
# Concepts: Dictionaries, Dictionary methods, Merging data

# SOLUTION
def merge_dicts_replace(dict1, dict2):
    """Merge two dictionaries, second dict values take precedence."""
    result = dict1.copy()  # Create a copy to avoid modifying original
    result.update(dict2)   # Update with second dictionary
    return result

def merge_dicts_add(dict1, dict2):
    """Merge two dictionaries, adding values for common keys."""
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            result[key] += value  # Add values for common keys
        else:
            result[key] = value   # Add new keys

    return result

# Test examples
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'c': 30, 'd': 4}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print()

merged_replace = merge_dicts_replace(dict1, dict2)
print("Merged (replace):", merged_replace)

merged_add = merge_dicts_add(dict1, dict2)
print("Merged (add):", merged_add)

"""
EXPLANATION:
1. merge_dicts_replace() uses .copy() to create a new dictionary
2. .update() modifies the dictionary by adding key-value pairs from dict2
3. If a key exists in both, the value from dict2 overwrites the original
4. merge_dicts_add() iterates through dict2 items
5. For each key, we check if it exists in result and add values accordingly
6. .items() returns (key, value) tuples for easy iteration

Key Concepts:
- .copy() creates a shallow copy of a dictionary
- .update() merges dictionaries in-place
- Checking 'if key in dict' is efficient in Python
- Dictionary comprehensions can also be used for merging
"""

# Alternative using dictionary unpacking (Python 3.5+)
print("\n--- ALTERNATIVE SOLUTION ---")

def merge_dicts_unpacking(dict1, dict2):
    """Merge using dictionary unpacking."""
    return {**dict1, **dict2}

merged_unpacking = merge_dicts_unpacking(dict1, dict2)
print("Merged using unpacking:", merged_unpacking)

# Extension solution: Merge multiple dictionaries
print("\n--- EXTENSION SOLUTION ---")

def merge_multiple_dicts(*dicts, mode='replace'):
    """
    Merge any number of dictionaries.

    Args:
        *dicts: Variable number of dictionaries to merge
        mode: 'replace' (default) or 'add'
    """
    if not dicts:
        return {}

    result = {}

    if mode == 'replace':
        for d in dicts:
            result.update(d)

    elif mode == 'add':
        for d in dicts:
            for key, value in d.items():
                if isinstance(value, (int, float)):
                    result[key] = result.get(key, 0) + value
                else:
                    result[key] = value

    return result

# Test with multiple dictionaries
dict3 = {'d': 40, 'e': 5}
dict4 = {'a': 100, 'f': 6}

print("\nMerging 4 dictionaries (replace mode):")
multi_merged_replace = merge_multiple_dicts(dict1, dict2, dict3, dict4, mode='replace')
print(multi_merged_replace)

print("\nMerging 4 dictionaries (add mode):")
multi_merged_add = merge_multiple_dicts(dict1, dict2, dict3, dict4, mode='add')
print(multi_merged_add)

# Handling mixed types
print("\n--- HANDLING MIXED TYPES ---")
dict_mixed1 = {'name': 'Alice', 'score': 85, 'tags': ['python', 'data']}
dict_mixed2 = {'score': 15, 'tags': ['ml'], 'city': 'NYC'}

def smart_merge(dict1, dict2):
    """Merge with type-aware handling."""
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            # Add numbers
            if isinstance(value, (int, float)) and isinstance(result[key], (int, float)):
                result[key] += value
            # Extend lists
            elif isinstance(value, list) and isinstance(result[key], list):
                result[key] = result[key] + value
            # Otherwise replace
            else:
                result[key] = value
        else:
            result[key] = value

    return result

smart_merged = smart_merge(dict_mixed1, dict_mixed2)
print("Smart merge result:", smart_merged)
