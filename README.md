111111111111111111111111111111
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char str[50];
    int i, flag = 0;

    char *keywords[] = {
        "if", "else", "switch", "case",
        "for", "while", "do", "break",
        "continue", "goto", "return"
    };

    printf("Enter a word: ");
    scanf("%s", str);

    for(i = 0; i < 11; i++)
    {
        if(strcmp(str, keywords[i]) == 0)
        {
            flag = 1;
            break;
        }
    }

    if(flag)
        printf("It is a Flow Control Keyword\n");

    else if(isalpha(str[0]) || str[0] == '_')
    {
        for(i = 1; str[i] != '\0'; i++)
        {
            if(!isalnum(str[i]) && str[i] != '_')
            {
                flag = 2;
                break;
            }
        }

        if(flag == 2)
            printf("Invalid Identifier\n");
        else
            printf("It is an Identifier\n");
    }
    else
        printf("Invalid Identifier\n");

    return 0;
}

2222222222222222222222222222222222222

#include <stdio.h>
#include <string.h>
#include <ctype.h>

char lhs[20], rhs[20][20];
char first[26][20];
int n, count[26];

void add(int nt, char c)
{
    for(int i=0; i<count[nt]; i++)
        if(first[nt][i] == c)
            return;

    first[nt][count[nt]++] = c;
}

int main()
{
    printf("Enter number of productions: ");
    scanf("%d",&n);

    printf("Enter productions (E->E+T):\n");

    for(int i=0; i<n; i++)
    {
        char s[30];
        scanf("%s",s);

        lhs[i] = s[0];
        strcpy(rhs[i],s+3);
    }

    int change;

    do
    {
        change = 0;

        for(int i=0; i<n; i++)
        {
            int nt = lhs[i]-'A';
            char c = rhs[i][0];

            if(isupper(c))
            {
                int x = c-'A';

                for(int j=0; j<count[x]; j++)
                {
                    int old = count[nt];
                    add(nt,first[x][j]);

                    if(count[nt] != old)
                        change = 1;
                }
            }
            else
            {
                int old = count[nt];
                add(nt,c);

                if(count[nt] != old)
                    change = 1;
            }
        }

    }while(change);

    printf("\nFIRST Sets:\n");

    for(int i=0; i<26; i++)
    {
        if(count[i])
        {
            printf("FIRST(%c) = { ",i+'A');

            for(int j=0; j<count[i]; j++)
                printf("%c ",first[i][j]);

            printf("}\n");
        }
    }

    return 0;
}


3333333333333333333333333333333333333
#include <stdio.h>
#include <string.h>

char stack[100], input[100];
int top = -1, ip = 0;

char *table[5][6] = {
    {"TQ", "",   "",    "TQ",  "",  ""},
    {"",   "+TQ","",    "",    "#", "#"},
    {"FR", "",   "",    "FR",  "",  ""},
    {"",   "#",  "*FR", "",    "#", "#"},
    {"i",  "",   "",    "(E)", "",  ""}
};

char nt[] = {'E', 'Q', 'T', 'R', 'F'};

void push(char c)
{
    stack[++top] = c;
}

char pop()
{
    return stack[top--];
}

int row(char c)
{
    for(int i = 0; i < 5; i++)
        if(nt[i] == c)
            return i;

    return -1;
}

int col(char c)
{
    if(c == 'i') return 0;

    switch(c)
    {
        case '+': return 1;
        case '*': return 2;
        case '(': return 3;
        case ')': return 4;
        case '$': return 5;
    }

    return -1;
}

void display()
{
    printf("\nPredictive Parsing Table\n");
    printf("NT/T\tid\t+\t*\t(\t)\t$\n");

    for(int i = 0; i < 5; i++)
    {
        printf("%c\t", nt[i]);

        for(int j = 0; j < 6; j++)
            printf("%s\t", table[i][j][0] ? table[i][j] : "-");

        printf("\n");
    }
}

int main()
{
    display();

    printf("\nEnter input ending with $: ");
    scanf("%99s", input);

    if(strlen(input) == 0 ||
       input[strlen(input) - 1] != '$')
    {
        printf("Invalid String\n");
        return 0;
    }

    push('$');
    push('E');

    while(top >= 0)
    {
        char x = stack[top];
        char a = input[ip];

        if(x == 'i' && a == 'i' && input[ip+1] == 'd')
        {
            pop();
            ip += 2;
        }
        else if(x == a)
        {
            pop();
            ip++;
        }
        else if(x >= 'A' && x <= 'Z')
        {
            int r = row(x);
            int c = col(a);

            if(r == -1 || c == -1 || table[r][c][0] == '\0')
            {
                printf("Invalid String\n");
                return 0;
            }

            char *p = table[r][c];
            pop();

            if(p[0] != '#')
            {
                for(int j = strlen(p)-1; j >= 0; j--)
                    push(p[j]);
            }
        }
        else
        {
            printf("Invalid String\n");
            return 0;
        }
    }

    if(input[ip] == '\0')
        printf("Valid String\n");
    else
        printf("Invalid String\n");

    return 0;
}

444444444444444444444444444444444
#include <stdio.h>
#include <string.h>

int a[12][6] = {
    {5,0,0,4,0,0},
    {0,6,0,0,0,999},
    {0,-2,7,0,-2,-2},
    {0,-4,-4,0,-4,-4},
    {5,0,0,4,0,0},
    {0,-6,-6,0,-6,-6},
    {5,0,0,4,0,0},
    {5,0,0,4,0,0},
    {0,6,0,0,11,0},
    {0,-1,7,0,-1,-1},
    {0,-3,-3,0,-3,-3},
    {0,-5,-5,0,-5,-5}
};

int g[12][3] = {
    {1,2,3}, {-1,-1,-1}, {-1,-1,-1}, {-1,-1,-1},
    {8,2,3}, {-1,-1,-1}, {-1,9,3}, {-1,-1,10},
    {-1,-1,-1}, {-1,-1,-1}, {-1,-1,-1}, {-1,-1,-1}
};

char *p[] = {"","E+T","T","T*F","F","(E)","id"};
char lhs[] = {' ','E','E','T','T','F','F'};
int len[] = {0,3,1,3,1,3,1};

int main()
{
    char s[100], stack[100];
    int st[100], top=0, i=0, c, x, r, k;

    printf("Enter string: ");
    scanf("%98s",s);
    strcat(s,"$");

    stack[0]='$';
    st[0]=0;

    while(1)
    {
        switch(s[i])
        {
            case 'i': c=0; i = i; break;
            case '+': c=1; break;
            case '*': c=2; break;
            case '(': c=3; break;
            case ')': c=4; break;
            case '$': c=5; break;
            default:
                printf("Invalid input\n");
                return 0;
        }

        if(s[i]=='i' && s[i+1]!='d')
        {
            printf("Invalid input\n");
            return 0;
        }

        x=a[st[top]][c];

        if(x==999)
        {
            printf("String Accepted\n");
            break;
        }
        else if(x>0)
        {
            printf("Shift %d\n",x);
            stack[++top]=s[i];
            st[top]=x;
            i += (s[i]=='i') ? 2 : 1;
        }
        else if(x<0)
        {
            r=-x;
            printf("Reduce %c -> %s\n",lhs[r],p[r]);

            top-=len[r];

            k = (lhs[r]=='E') ? 0 : (lhs[r]=='T') ? 1 : 2;

            x=g[st[top]][k];

            if(x==-1)
            {
                printf("Rejected\n");
                break;
            }

            stack[++top]=lhs[r];
            st[top]=x;
        }
        else
        {
            printf("String Rejected\n");
            break;
        }

        printf("Stack: ");
        for(int j=0;j<=top;j++)
            printf("%c%d ",stack[j],st[j]);

        printf("\n");
    }

    return 0;
}

5555555555555555555555555555555555555555
#include <stdio.h>
#include <string.h>

int action[6][3] = {
    {3,-3,-3},
    {0,0,999},
    {0,5,-5},
    {0,-2,-2},
    {0,0,-1},
    {0,0,-4}
};

int go[6][3] = {
    {1,2,-1},
    {-1,-1,-1},
    {-1,-1,4},
    {-1,-1,-1},
    {-1,-1,-1},
    {-1,-1,-1}
};

char lhs[] = {' ','S','A','A','B','B'};
int len[] = {0,2,1,0,1,0};
char *p[] = {"","AB","a","e","b","e"};

int main()
{
    char s[100], stack[100];
    int st[100], top=0, i=0, c, x, r, k;

    printf("Enter input string (a, b): ");
    scanf("%99s",s);
    strcat(s,"$");

    stack[0]='$';
    st[0]=0;

    while(1)
    {
        switch(s[i])
        {
            case 'a': c=0; break;
            case 'b': c=1; break;
            case '$': c=2; break;
            default:
                printf("Invalid input\n");
                return 0;
        }

        x=action[st[top]][c];

        if(x==999)
        {
            printf("String Accepted\n");
            break;
        }
        else if(x>0)
        {
            printf("Shift %d\n",x);
            stack[++top]=s[i];
            st[top]=x;
            i++;
        }
        else if(x<0)
        {
            r=-x;
            printf("Reduce %c -> %s\n",lhs[r],p[r]);

            top-=len[r];

            k = (lhs[r]=='S') ? 0 : (lhs[r]=='A') ? 1 : 2;

            x=go[st[top]][k];

            if(x==-1)
            {
                printf("String Rejected\n");
                break;
            }

            stack[++top]=lhs[r];
            st[top]=x;
        }
        else
        {
            printf("String Rejected\n");
            break;
        }

        printf("Stack: ");
        for(int j=0;j<=top;j++)
            printf("%c%d ",stack[j],st[j]);

        printf("\n");
    }

    return 0;
}

666666666666666666666666666666666666666666
#include <stdio.h>
#include <string.h>

char ip[100];
int pos=0, error=0;

void E();
void Eprime();
void T();
void Tprime();
void F();

void E()
{
    T();
    Eprime();
}

void Eprime()
{
    if(ip[pos]=='+')
    {
        pos++;
        T();
        Eprime();
    }
}

void T()
{
    F();
    Tprime();
}

void Tprime()
{
    if(ip[pos]=='*')
    {
        pos++;
        F();
        Tprime();
    }
}

void F()
{
    if(ip[pos]=='(')
    {
        pos++;
        E();

        if(ip[pos]==')')
            pos++;
        else
            error=1;
    }
    else if(ip[pos]=='i' && ip[pos+1]=='d')
        pos+=2;
    else
        error=1;
}

int main()
{
    printf("Enter a string: ");
    scanf("%99s",ip);

    E();

    if(ip[pos]=='\0' && error==0)
        printf("String Accepted\n");
    else
        printf("String Not Accepted\n");

    return 0;
}

77777777777777777777777777
#include <stdio.h>

char ip[100];
int pos=0, error=0;

void S();
void L();
void Lprime();

void S()
{
    if(ip[pos]=='(')
    {
        pos++;
        L();

        if(ip[pos]==')')
            pos++;
        else
            error=1;
    }
    else if(ip[pos]=='a')
        pos++;
    else
        error=1;
}

void L()
{
    S();
    Lprime();
}

void Lprime()
{
    if(ip[pos]==',')
    {
        pos++;
        S();
        Lprime();
    }
}

int main()
{
    printf("Enter string: ");
    scanf("%99s",ip);

    S();

    if(ip[pos]!='\0')
        error=1;

    if(error==0)
        printf("String is Accepted\n");
    else
        printf("String is Not Accepted\n");

    return 0;
}


88888888888888888888888888
#include <stdio.h>

int a = 10;          // Static global allocation

void display()
{
    static int count = 0;  // Static local allocation
    count++;
    printf("Count = %d\n", count);
}

int main()
{
    int b = 20;      // Stack allocation

    printf("Global variable = %d\n", a);
    printf("Local variable = %d\n", b);

    display();
    display();
    display();

    return 0;
}

99999999999999999999999999
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *stack = NULL;
    int size, top = -1;
    int choice, value;

    printf("Enter the stack size: ");
    scanf("%d", &size);

    if (size <= 0)
    {
        printf("Invalid stack size!\n");
        return 1;
    }

    while (1)
    {
        printf("\n1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 1:
            printf("Enter the element: ");
            scanf("%d", &value);

            if (top == size - 1)
            {
                printf("Stack is full!\n");
                break;
            }

            int *temp = realloc(stack, (top + 2) * sizeof(int));

            if (temp == NULL)
            {
                printf("Memory allocation failed!\n");
                break;
            }

            stack = temp;
            stack[++top] = value;

            printf("%d pushed into the stack.\n", value);
            break;

        case 2:
            if (top == -1)
            {
                printf("Stack is empty!\n");
            }
            else
            {
                printf("Popped element: %d\n", stack[top]);
                top--;

                if (top == -1)
                {
                    free(stack);
                    stack = NULL;
                }
                else
                {
                    int *temp = realloc(stack, (top + 1) * sizeof(int));
                    if (temp != NULL)
                        stack = temp;
                }
            }
            break;

        case 3:
            if (top == -1)
            {
                printf("Stack is empty!\n");
            }
            else
            {
                printf("Stack elements are:\n");

                for (int i = top; i >= 0; i--)
                    printf("%d\n", stack[i]);
            }
            break;

        case 4:
            free(stack);
            printf("Memory released. Exiting...\n");
            return 0;

        default:
            printf("Invalid choice!\n");
        }
    }

    return 0;
}

10101010101010101010101101

#include <stdio.h>
#include <stdlib.h>

struct Block
{
    int size, free;
    struct Block *next;
};

int main()
{
    int n, i, choice, p, found;
    struct Block *head = NULL, *temp, *prev, *best;

    printf("Enter total number of memory blocks: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        temp = (struct Block *)malloc(sizeof(struct Block));

        printf("Enter block size: ");
        scanf("%d", &temp->size);

        temp->free = 1;
        temp->next = NULL;

        if (head == NULL)
            head = temp;
        else
            prev->next = temp;

        prev = temp;
    }

    printf("\n1.First Fit\n2.Best Fit\n3.Worst Fit");
    printf("\nEnter choice: ");
    scanf("%d", &choice);

    printf("Enter number of processes: ");
    scanf("%d", &p);

    for (i = 0; i < p; i++)
    {
        int size;

        printf("\nEnter process size: ");
        scanf("%d", &size);

        temp = head;
        best = NULL;
        found = 0;

        while (temp != NULL)
        {
            if (temp->free && temp->size >= size)
            {
                if (choice == 1)
                {
                    best = temp;
                    break;
                }

                if (choice == 2 &&
                   (best == NULL || temp->size < best->size))
                    best = temp;

                if (choice == 3 &&
                   (best == NULL || temp->size > best->size))
                    best = temp;
            }

            temp = temp->next;
        }

        if (best != NULL)
        {
            best->free = 0;
            found = 1;

            printf("Process %d allocated to block of size %d\n",
                   i + 1, best->size);
        }

        if (!found)
            printf("Process %d cannot be allocated\n", i + 1);
    }

    printf("\nFinal Heap Memory Status:\n");

    temp = head;
    i = 1;

    while (temp != NULL)
    {
        printf("Block %d: Size = %d, Status = %s\n",
               i++, temp->size,
               temp->free ? "Free" : "Allocated");

        temp = temp->next;
    }

    while (head != NULL)
    {
        temp = head;
        head = head->next;
        free(temp);
    }

    return 0;
}

111111111111111111111111111111
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct node
{
    char op, name[20], temp[20];
    struct node *l, *r;
};

char s[100];
int p=0, count=0;

struct node* create(char op, char *name, struct node *l, struct node *r)
{
    struct node *n = calloc(1, sizeof(struct node));

    n->op = op;
    if(name) strcpy(n->name, name);

    n->l = l;
    n->r = r;

    return n;
}

struct node* expr();

struct node* factor()
{
    while(s[p]==' ') p++;

    if(s[p]=='-')
    {
        p++;
        return create('~',NULL,factor(),NULL);
    }

    if(s[p]=='(')
    {
        p++;
        struct node *n=expr();
        p++;
        return n;
    }

    char a[20];
    int i=0;

    while(isalnum(s[p]) || s[p]=='_')
        a[i++]=s[p++];

    a[i]='\0';

    return create(0,a,NULL,NULL);
}

struct node* term()
{
    struct node *n=factor();

    while(s[p]=='*' || s[p]=='/')
    {
        char op=s[p++];
        n=create(op,NULL,n,factor());
    }

    return n;
}

struct node* expr()
{
    struct node *n=term();

    while(s[p]=='+' || s[p]=='-')
    {
        char op=s[p++];
        n=create(op,NULL,n,term());
    }

    return n;
}

char* generate(struct node *n)
{
    if(!n->op)
        return n->name;

    char a[20],b[20],t[20];

    strcpy(a,generate(n->l));

    sprintf(t,"t%d",++count);

    if(n->op=='~')
        printf("%s = -%s\n",t,a);
    else
    {
        strcpy(b,generate(n->r));
        printf("%s = %s %c %s\n",t,a,n->op,b);
    }

    strcpy(n->temp,t);
    return n->temp;
}

int main()
{
    char lhs[20];

    printf("Enter expression: ");
    fgets(s,sizeof(s),stdin);

    char *eq=strchr(s,'=');

    if(!eq)
    {
        printf("Invalid expression\n");
        return 0;
    }

    strncpy(lhs,s,eq-s);
    lhs[eq-s]='\0';

    p=eq-s+1;

    struct node *root=expr();

    printf("\nThree Address Code:\n");
    printf("%s = %s\n",lhs,generate(root));

    return 0;
}

131313131313131313131313131313131
%{
#include <stdio.h>
%}

%%
[+]?[0-9]+          { printf("Positive Integer\n"); }
[+]?[0-9]+"."[0-9]+ { printf("Positive Real\n"); }
-[0-9]+             { printf("Negative Integer\n"); }
-[0-9]+"."[0-9]+    { printf("Negative Real\n"); }
[ \t\n]+            ;
.                   { printf("Invalid Input\n"); }
%%

int yywrap() { return 1; }

int main()
{
    printf("Enter numbers:\n");
    yylex();
    return 0;
}
141414141414141414141414141414141
%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
-?[0-9]+"."[0-9]+ {
    printf("Integer = %d\n", atoi(yytext));
}
[ \t\n]+ ;
. { printf("Invalid Input\n"); }
%%

int yywrap() { return 1; }

int main()
{
    printf("Enter real numbers:\n");
    yylex();
    return 0;
}

1515151515151515151515151515151515
%{
#include <stdio.h>
#include <string.h>

void days(char *m)
{
    if (!strcmp(m,"January") || !strcmp(m,"March") ||
        !strcmp(m,"May") || !strcmp(m,"July") ||
        !strcmp(m,"August") || !strcmp(m,"October") ||
        !strcmp(m,"December"))
        printf("31 days\n");

    else if (!strcmp(m,"April") || !strcmp(m,"June") ||
             !strcmp(m,"September") || !strcmp(m,"November"))
        printf("30 days\n");

    else if (!strcmp(m,"February"))
        printf("28 or 29 days\n");

    else
        printf("Invalid month\n");
}
%}

%%
[A-Za-z]+ { days(yytext); }
[ \t\n]+  ;
.         { printf("Invalid input\n"); }
%%

int yywrap() { return 1; }

int main()
{
    printf("Enter month name:\n");
    yylex();
    return 0;
}


1616161616161616161616161
%{
#include <stdio.h>
#include <stdlib.h>

char *ones[] = {
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine"
};

char *teens[] = {
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
    "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
};

char *tens[] = {
    "", "", "Twenty", "Thirty", "Forty",
    "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
};

void words(int n)
{
    if (n < 0 || n > 100) {
        printf("Out of range\n");
    }
    else if (n < 10) {
        printf("%s\n", ones[n]);
    }
    else if (n < 20) {
        printf("%s\n", teens[n-10]);
    }
    else if (n < 100) {
        printf("%s", tens[n/10]);
        if (n % 10 != 0)
            printf(" %s", ones[n%10]);
        printf("\n");
    }
    else {
        printf("One Hundred\n");
    }
}
%}

%%
[0-9]+ {
    words(atoi(yytext));
}
[ \t\n]+ ;
. { printf("Invalid input\n"); }
%%

int yywrap() { return 1; }

int main()
{
    printf("Enter a number (0-100):\n");
    yylex();
    return 0;
}


17171717171717171717171717171717
%{
#include <stdio.h>
#include <stdlib.h>

char *one[] = {"Zero","One","Two","Three","Four",
"Five","Six","Seven","Eight","Nine"};

char *teen[] = {"Ten","Eleven","Twelve","Thirteen","Fourteen",
"Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};

char *ten[] = {"","","Twenty","Thirty","Forty",
"Fifty","Sixty","Seventy","Eighty","Ninety"};

void words(int n)
{
    if(n < 0 || n > 1000) {
        printf("Number out of range\n");
        return;
    }

    if(n < 10)
        printf("%s", one[n]);

    else if(n < 20)
        printf("%s", teen[n-10]);

    else if(n < 100) {
        printf("%s", ten[n/10]);
        if(n%10)
            printf(" %s", one[n%10]);
    }

    else if(n < 1000) {
        printf("%s Hundred", one[n/100]);
        if(n%100) {
            printf(" ");
            words(n%100);
        }
    }

    else
        printf("One Thousand");
}
%}

%%
[0-9]+ {
    words(atoi(yytext));
    printf("\n");
}
[ \t\n]+ ;
. { printf("Invalid input\n"); }
%%

int yywrap()
{
    return 1;
}

int main()
{
    printf("Enter a number between 0 and 1000:\n");
    yylex();
    return 0;
}

1818181818181818181818181818
%{
#include <stdio.h>
%}

%x COMMENT

%%
"//"[^\n]* {
    printf("Single-line comment: %s\n", yytext);
}

"/*" {
    printf("Multi-line comment: ");
    BEGIN(COMMENT);
}

<COMMENT>"*/" {
    printf("\n");
    BEGIN(INITIAL);
}

<COMMENT>\n {
    printf("\n");
}

<COMMENT>. {
    ECHO;
}

<COMMENT><<EOF>> {
    printf("\nUnterminated comment\n");
    return 0;
}

.|\n ;
%%

int yywrap() { return 1; }

int main()
{
    printf("Enter source code (Ctrl+D to stop):\n");
    yylex();
    return 0;
}

19191919191919191919191
%{
#include <stdio.h>
%}

%x COMMENT

%%
"//"[^\n]* {
    printf("Single-line comment: %s\n", yytext);
}

"/*" {
    printf("Multi-line comment: ");
    BEGIN(COMMENT);
}

<COMMENT>"*/" {
    printf("\n");
    BEGIN(INITIAL);
}

<COMMENT>\n {
    printf("\n");
}

<COMMENT>. {
    ECHO;
}

<COMMENT><<EOF>> {
    printf("\nUnterminated comment\n");
    return 0;
}

.|\n ;
%%

int yywrap() { return 1; }

int main()
{
    printf("Enter source code (Ctrl+D to stop):\n");
    yylex();
    return 0;
}
