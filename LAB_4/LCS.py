def lcs(X, Y, m, n):
    if m == len(X) or n == len(Y):
        return 0, ""
    elif X[m] == Y[n]:
        length, lcs_str = lcs(X, Y, m+1, n+1)
        return 1 + length, X[m] + lcs_str
    else:
        length1, lcs_str1 = lcs(X, Y, m, n+1)
        length2, lcs_str2 = lcs(X, Y, m+1, n)
        if length1 > length2:
            return length1, lcs_str1
        else:
            return length2, lcs_str2

# Example usage:
X = "president"
Y = "providence"
length, lcs_str = lcs(X, Y, 0, 0)
print("Length of LCS is", length)
print("LCS is", lcs_str)
