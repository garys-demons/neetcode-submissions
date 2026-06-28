class Solution {
   public:
    char reverse(char b) {
        if (b == ')') return '(';
        if (b == ']') return '[';
        if (b == '}') return '{';
        return '\0';
    }

    bool isValid(string s) {
        stack<char> b;

        for (char& c : s) {
            if (c == '(' || c == '[' || c == '{') {
                b.push(c);
            }
            else if (!b.empty() && b.top() == reverse(c)) {
                b.pop();
            } 
            else {
                return false;
            }
        }
        if(b.empty()) return true;
        return false;
    }
};