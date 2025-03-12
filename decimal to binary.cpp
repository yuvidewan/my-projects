// decimal to binary.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>


long convert(int d);

int main()
{
     int d;
    printf("Enter decimal : ");
   std::cin >> d;
    printf("Binary is %ld", convert(d));

    return 0;
}
long convert(int d)
{
    long b=0;
    int i,j=1;

    while (d!=0)
    {
        i=d%2;
        d=d/2;
        b=b+i*j;
        j=j*10;
    }
    return b;
}

