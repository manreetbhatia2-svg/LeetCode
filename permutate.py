def generate_permutation(nums):
    result = []
    digits = [str(i) for i in range(1,nums+1)]

    def backtrack(current_path,remaining_digits):
        if not remaining_digits:
            result.append(int("".join(current_path)))
            return
        
        for i in range(len(remaining_digits)):
            backtrack(current_path + [remaining_digits[i]], remaining_digits[:i] + remaining_digits[i+1:] )

    backtrack([],digits)
    return result 

nums = int(input("Enter number from 1 to 9: "))
print(generate_permutation(nums))