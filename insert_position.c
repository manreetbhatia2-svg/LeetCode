/*Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.*/

#include<stdio.h>
int searchInsert(int* nums, int numsSize, int target);
int main(){
    int target, numsSize, output;
    int nums[] = {1,3,5,6};
    numsSize = sizeof(nums)/sizeof(nums[0]);
    printf("Enter target ");
    scanf("%d",&target);
    output = searchInsert(nums, numsSize, target);
    printf("%d",output);
}
int searchInsert(int* nums, int numsSize, int target) {
    int ans;
    for(int i=0; i<numsSize; i++){
        if(nums[0]>target)
            return 0;
        if (nums[i]==target){
            ans = i;
            break;
        }
        else if(nums[i]<target)
            ans = i+1;
    }
    return ans;
}