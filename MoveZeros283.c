#include <stdio.h>

// Flow: if the current number 0, move it to the end of the array. 
// Increment the movedZeros counter. 
// If after moved the current number is zero, decrement the counter. (e.g [0,0,1]) 
// During new iteration check whether the amount of movedZeros + i == numsSize
// that means we looped over all elements, break the loop.
// Downsides: nested loops. At the end of the array, would move zeros even if everything 
// to the right are zeros. 
// Time: O(n^2)
void moveZeroes(int* nums, int numsSize) {
	int movedZeros = 0;

	for (int i = 0; i < numsSize; i++) {
		if (i + movedZeros == numsSize) {
			break;
		}
		if (nums[i] == 0 && i != numsSize - 1)  {
			for (int j = i; j < numsSize - 1; j++) {
				int temp = nums[j];
				nums[j] = nums[j + 1];
				nums[j + 1] = temp;
			}
			movedZeros ++;
		}

		if (nums[i] == 0 && i != numsSize - 1) {
			i--;
		}
	}
}


// better version
// Flow: 
// For loop: checks if current element is NONZERO. If so moves it to the leftmost 
// position that is not zero. 
// Increment counter a, so the next non zero element gets saved to the right of previous 
// nonzero element.
// While loop: sets the rest of the elements at the end to zero.
// Time: O(n)
void moveZeroes1(int* nums, int numsSize) {
	int a = 0;

	for (int i = 0; i < numsSize; i++) {
		if (nums[i] != 0) {
			nums[a] = nums[i];
			a++;
		}
	}

	while (a < numsSize) {
		nums[a] = 0;
		a++;
	}
}