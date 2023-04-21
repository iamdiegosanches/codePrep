/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int *arr = (int *)malloc(numsSize * sizeof(int));
    if (arr == NULL) {
      *returnSize = 0;
      return NULL;
    }
    int i, j, k;

    for (i = 0, j = n, k = 0; i < n; i++, j++, k+=2)
    {
        arr[k] = nums[i];
        arr[k+1] = nums[j];
    }
    *returnSize = numsSize;
    return arr;
}
