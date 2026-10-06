struct stack{
    int top;
    char a[10000];
}st;


void push(int value){
    st.top++;
    st.a[st.top] = value;


}
char pop(){  
    if(st.top == -1)
        return 0;  
   
    char x;
    x = st.a[st.top];
    st.top--;
    return x;


}
bool isValid(char* s) {
    st.top = -1;
    char bracket;
    for(int i=0; i<strlen(s); i++){
        if(s[i] == '[' || s[i] == '{' || s[i] == '(')
            push(s[i]);


        if(s[i] == ']' || s[i] == '}' || s[i] == ')'){
            bracket = pop();
       
            if((bracket == '[' && s[i] == ']') || (bracket == '(' && s[i] == ')')||( bracket == '{' && s[i] == '}' )){
                continue;
            }
            else{
                return false;
            }
        }
    }
    if(st.top == -1)
        return (true);
    else
        return false;




}
