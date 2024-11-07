import random

class QuickSort:
    def __init__(self, array):
        self.array = array

    # Deterministic method to find pivot
    def partition(self, low, high):
        pivot = self.array[high]  # High element is default pivot
        i = low - 1  # Pointer for greater element

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1  # Increment the pointer
                self.array[i], self.array[j] = self.array[j], self.array[i]  # Swap
        # Swap the pivot element with the greater element specified by i
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    def partition_random(self, low, high):
        pivot_index = random.randint(low, high)  # Random pivot
        self.array[pivot_index], self.array[high] = self.array[high], self.array[pivot_index]
        return self.partition(low, high)

    # Deterministic variant of sort
    def sort_d(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.sort_d(low, pivot - 1)
            self.sort_d(pivot + 1, high)

    # Randomized variant of sort
    def sort_r(self, low, high):
        if low < high:
            pivot = self.partition_random(low, high)
            self.sort_r(low, pivot - 1)
            self.sort_r(pivot + 1, high)

def main():
    while True:
        try:
            print("Press Ctrl+C to exit...")
            array = list(map(int, input("Enter array (space-separated): ").split()))
            if len(array) == 0:
                print("Array cannot be empty. Please enter at least one number.")
                continue

            print("Deterministic variant of sort")
            sort1 = QuickSort(array.copy())  # Use a copy to preserve the original array
            sort1.sort_d(0, len(array) - 1)
            print("Sorted array (Deterministic):", sort1.array)

            print("Randomized variant of sort")
            sort2 = QuickSort(array.copy())  # Use a copy to preserve the original array
            sort2.sort_r(0, len(array) - 1)
            print("Sorted array (Randomized):", sort2.array)
        
        except ValueError:
            print("Invalid input. Please enter a list of integers separated by spaces.")

if __name__ == "__main__":
    main()
