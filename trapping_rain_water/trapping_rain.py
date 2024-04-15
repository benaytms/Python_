'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
'''

def trapping_water(a: list[int]) -> int:
    # reversing the array of heights so we can create a list of maximum heights coming from the end to
    # the beginning
    reversed_a: list[int] = a[::-1]

    # size of the array, final index and total water units respectively
    n: int = len(a)
    k: int = n - 1
    agua_total: int = 0

    # list of maximum heights from left to right and from right to left respectively
    L2Rmaxs: list[int] = []
    R2Lmaxs: list[int] = []

    # variable for the maximum height value for each iteration, starts as the first value for the list going left-right
    # and the other starts at the final value for the list going right-left
    Lmax: int = a[0]
    Rmax: int = a[k]

    # initialize the lists putting the first values
    L2Rmaxs.append(Lmax)
    R2Lmaxs.append(Rmax)

    for i in range(1, n):
        
        # if the current height value is greater than the previous, it turns the maximum height to this current value
        if (a[i] > L2Rmaxs[i-1] and i <= k):
            Lmax = a[i]
        # every iteration appends the maximum value so it doesn't have values missing in case the if-conditional is not accessed
        L2Rmaxs.append(Lmax)

        # its the same as the previous, except its using the reversed array
        if (reversed_a[i] > R2Lmaxs[i-1] and i <= k):
            Rmax = reversed_a[i]
        R2Lmaxs.append(Rmax)
    # now it re-reverse the list of maximum heights coming from right-left
    R2Lmaxs = R2Lmaxs[::-1]

    # now finally, one last iteration so it binds the water units with the 'agua_total' variable 
    for j in range(n):
        # this operation takes in account the smaller maximum height value (as explained at the end of this file) and subtracts
        # from the current wall height, so it doesn't consider that there's water in places where there's actually an elevation
        agua_total = agua_total + (min(R2Lmaxs[j], L2Rmaxs[j]) - a[j])

    # return with the total of water units
    return agua_total

def main() -> None:
    # array of random wall heights
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # printing water units
    print(trapping_water(array))

if __name__ == "__main__":
    # main function call
    main()


'''
Algorithm explanation:

for this problem, the first thing we need to understand is that: if there's 2 walls with given heights,
to know how much water it will be in between them, we need to consider the smaller height value between the 2 walls;

i.g if you have a wall with 3m and another of 2m, the water between them can't be more than 2m tall because it overflows.

This means that between 2 maximum heights, one considering values from the left and another values from the right,
we'll always consider the smaller value between them.

Another thing we must consider is the the elevation height between 2 walls; 
Let's say we have a wall of 2m on the left, an elevation of 1m and a wall of 3m on the right;
we'll first consider the 2m wall as maximum water reach and remove the 1m elevation. Then there'll be 1m of water.


So basically, we'll have 2 maximum heights in every point, one considering values coming from the left and other from the right.
Why's that? because we need to verify up to that point the maximum height the water can reach, and that can
be values from the left and values from the right.

Let's say we only check for a maximum height coming from the left, we find a height of 3m as the maximum height, 
and we presume the water can reach 3m, but then we find that there's no other wall of 3m in the array, this means
the water container is 3m from the left but from the right the maximum is just, let's say, 1m. The water should overflow and have
1m as height, not 3. Therefore that's the reason why we use 2 pointers of maximum heights.

'''
