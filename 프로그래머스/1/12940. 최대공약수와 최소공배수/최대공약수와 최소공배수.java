class Solution {
    public int[] solution(int n, int m) {
        
        int gcd = getGCD(n,m);
        int lcm = getLCM(n,m,gcd);
        
        int[] answer = {gcd, lcm};
        return answer;
    }
    
    // 최대 공약수 구하는 함수
    public int getGCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return getGCD(num2,num1%num2);
    }
    
    // 최대 공배수 구하는 함수
    public int getLCM(int num1, int num2, int gcd) {
        return (num1*num2)/gcd;
    }
}