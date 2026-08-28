/*Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.*/

#include <stdio.h>
int mySqrt(int number);

int main(){
    int num,sqrt;
    printf("Enter the number ");
    scanf("%d",&num);
    sqrt = mySqrt(num);
    printf("Square root of %d is %d",num,sqrt);
}

int mySqrt(int number){
    if (number<2)
        return number;

    int low=0, high=number,ans;
    
    while (low<=high){
        int mid = low + (high-low)/2;
        if (mid == number/mid){
            ans = mid;
            break;
        }
        else if(mid < number/mid){
            ans = mid;
            low = mid+1;
        }
        else
            high = mid-1;
    }
    return ans;
}