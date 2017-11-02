#204


# Time:  O(n)
# Space: O(n)


# Count the number of prime numbers less than a non-negative number, n
#
# Hint: The number n could be in the order of 100,000 to 5,000,000.

class Sol():
    def countPrimes(self,n):
        is_primes=[True]*n
        is_primes[0]=is_primes[1]=False
        for num in range(2,int(n**0.5)+1):
            if is_primes[num]:
                is_primes[num*num:n:num]=[False]*len(is_primes[num*num:n:num])
        return sum(is_primes)
