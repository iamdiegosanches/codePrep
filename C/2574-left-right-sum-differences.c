/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int modulus_subtraction(int a, int b) {
    int result = a - b;
    if (result < 0) {
        result = -result;
    }
    return result;
}

int* leftRigthDifference(int* nums, int numsSize, int* returnSize){
    int *leftSum = (int *)malloc(numsSize * sizeof(int));
    int *rightSum = (int *)malloc(numsSize * sizeof(int));
    int *arr = (int *)malloc(numsSize * sizeof(int));

    // Generate left sum
    int sum = 0;
    for (int j = 0; j < numsSize; j++) {
        leftSum[j] = sum;
        sum += nums[j];
    }

    // Generate right sum
    sum = 0;
    for (int j = numsSize-1; j >= 0; j--) {
        rightSum[j] = sum;
        sum += nums[j];
    }

    for (int j = 0; j < numsSize; j++) {
        arr[j] = modulus_subtraction(rightSum[j], leftSum[j]); 
    }

    *returnSize = numsSize;
    free(leftSum);
    free(rightSum);
    return arr;
}
