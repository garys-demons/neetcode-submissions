class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()) return false;
        unordered_map<int, int> sht;
        unordered_map<int, int> tht;

        for(int i = 0; i < s.length(); i++){
            if(sht.count(s[i])){
                sht[s[i]]++;
            } else{
                sht[s[i]] = 1;
            }

            if(tht.count(t[i])){
                tht[t[i]]++;
            } else{
                tht[t[i]] = 1;
            }
        }

        if(sht == tht){
            return true;
        }

        return false;
    }
};
