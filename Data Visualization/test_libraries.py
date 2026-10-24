"""
Test script to verify numpy, pandas, matplotlib, and seaborn are working correctly.
"""

import sys

def test_numpy():
    """Test NumPy functionality"""
    print("Testing NumPy...")
    import numpy as np
    
    # Create array and perform operations
    arr = np.array([1, 2, 3, 4, 5])
    print(f"  NumPy version: {np.__version__}")
    print(f"  Array: {arr}")
    print(f"  Mean: {np.mean(arr)}")
    print(f"  Sum: {np.sum(arr)}")
    print("  ✓ NumPy is working correctly!\n")
    return True

def test_pandas():
    """Test Pandas functionality"""
    print("Testing Pandas...")
    import pandas as pd
    
    # Create DataFrame and perform operations
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']
    }
    df = pd.DataFrame(data)
    print(f"  Pandas version: {pd.__version__}")
    print(f"  DataFrame:\n{df.to_string(index=False)}")
    print(f"  Shape: {df.shape}")
    print("  ✓ Pandas is working correctly!\n")
    return True

def test_matplotlib():
    """Test Matplotlib functionality"""
    print("Testing Matplotlib...")
    import matplotlib
    matplotlib.use('Agg')  # Use non-interactive backend for testing
    import matplotlib.pyplot as plt
    
    # Create a simple plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    ax.set_title('Test Plot')
    
    print(f"  Matplotlib version: {matplotlib.__version__}")
    print("  Successfully created a test plot")
    plt.close(fig)
    print("  ✓ Matplotlib is working correctly!\n")
    return True

def test_seaborn():
    """Test Seaborn functionality"""
    print("Testing Seaborn...")
    import seaborn as sns
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    # Load a sample dataset
    tips = sns.load_dataset("tips")
    print(f"  Seaborn version: {sns.__version__}")
    print(f"  Loaded 'tips' dataset with {len(tips)} rows")
    
    # Create a simple seaborn plot
    fig, ax = plt.subplots()
    sns.histplot(data=tips, x="total_bill", ax=ax)
    plt.close(fig)
    print("  Successfully created a seaborn histogram")
    print("  ✓ Seaborn is working correctly!\n")
    return True

def main():
    print("=" * 50)
    print("Library Installation Test")
    print("=" * 50)
    print(f"Python version: {sys.version}\n")
    
    results = []
    
    try:
        results.append(("NumPy", test_numpy()))
    except Exception as e:
        print(f"  ✗ NumPy failed: {e}\n")
        results.append(("NumPy", False))
    
    try:
        results.append(("Pandas", test_pandas()))
    except Exception as e:
        print(f"  ✗ Pandas failed: {e}\n")
        results.append(("Pandas", False))
    
    try:
        results.append(("Matplotlib", test_matplotlib()))
    except Exception as e:
        print(f"  ✗ Matplotlib failed: {e}\n")
        results.append(("Matplotlib", False))
    
    try:
        results.append(("Seaborn", test_seaborn()))
    except Exception as e:
        print(f"  ✗ Seaborn failed: {e}\n")
        results.append(("Seaborn", False))
    
    # Summary
    print("=" * 50)
    print("Summary")
    print("=" * 50)
    
    all_passed = True
    for name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"  {name}: {status}")
        if not passed:
            all_passed = False
    
    print()
    if all_passed:
        print("All libraries are installed and working correctly! 🎉")
    else:
        print("Some libraries have issues. Please check the errors above.")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
