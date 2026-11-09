# Move Zeroes 
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
n = [0,1,0,3,12]
write_ptr = 0
    
for read_ptr in range(len(n)):
    # If we find a non-zero element, swap it to the front
    if n[read_ptr] != 0:
        n[write_ptr], n[read_ptr] = n[read_ptr], n[write_ptr]
        write_ptr += 1

print(n)





                                                                                                 


 