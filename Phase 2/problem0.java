int sumOfAllDigitsInRange(int l, int r)
{
    int sum = 0;
    for(int i = l; i < r+1; i++){
        int j = i;
        while(j > 0){
            sum += j%10;
            j /= 10;
        }
    }
    return sum;
}
