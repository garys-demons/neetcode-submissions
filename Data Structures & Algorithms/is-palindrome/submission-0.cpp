class Solution {
   public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.length() - 1;

        for (auto& c : s) {
            c = tolower(c);
        }

        while (i < s.length() && j >= 0 && i < j) {
            if (iswalnum(s[i]) && iswalnum(s[j])) {
                if (s[i] != s[j]) {
                    return false;
                }
                i++;
                j--;
            } else if (!iswalnum(s[i])) {
                i++;
            } else if (!isalnum(s[j])) {
                j--;
            }
        }

        return true;
    }
};
