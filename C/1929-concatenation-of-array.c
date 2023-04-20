/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize){
    int *arr = (int *)malloc(2 * numsSize * sizeof(int));
    if (arr == NULL) {
      *returnSize = 0;
      return NULL;
    }
    for (int i = 0; i < numsSize; i++) {
      *(arr + i) = *(nums + i);
      *(arr + i + numsSize) = *(nums + i);
    }
    *returnSize = 2 * numsSize;
    return arr;
}