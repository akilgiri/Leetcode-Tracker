// Last updated: 5/25/2025, 1:08:22 PM
class Solution {
public:
    int hammingWeight(int n) {
        int res = 0;
        for (int i=0; i<32; i++){
            // std::cout << (n<<i) << std::endl;
            // (n<<i);
            if ((n >> i) & 1){
                res+=1;
            }
        }
        std::cout << res << std::endl;
        return res;
    }
};