class Solution {
    public boolean isPalindrome(String s) {
       int n=s.length();
       int i=0,j=n-1;
       while(i<=j)
       {
         while(j>i && !alphaNum(s.charAt(j)))
            j--;
         while(i<j && !alphaNum(s.charAt(i)))
            i++;
         if(Character.toLowerCase(s.charAt(i))!=Character.toLowerCase(s.charAt(j)))
            return false;
         i++;
         j--;
       }
       
       return true;
    }
    public boolean alphaNum(char c)
    {
        return (c>='A'&& c<='Z' || c<='z' && c>='a' || c<='9' && c>='0');
    }
}
