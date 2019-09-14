long oddNumbers(String s)
{
    long choices = 1;
    int possible = 9;
    ArrayList<Character> used = new ArrayList <Character>();
    for(int i =0; i < s.length(); i ++){
        char a = s.charAt(s.length()- i - 1);
        if(i == 0){
            choices *= 5;
            used.add(s.charAt(s.length()- i -1));
        }
        else if(used.contains(a)){

            choices *=1;
        }
        else{
            choices *= possible;
            possible -=1;
            used.add(a);
        }
    }
    return choices;
}
