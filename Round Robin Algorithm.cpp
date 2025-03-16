// Roubd Robin.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

struct cpu{
    int arrival;
    int burst;//burst changes during gantt chart funcn so need copy to calculate turnaround time;
    int burst_copy;
    string name;
    int finish;
    int turnaround;
    int waiting;
};
vector<cpu> ob;//global object to lessen arguments
int cpu_time = 0;

bool compareMyStructs(const cpu& a, const cpu& b) {
    if(a.arrival == b.arrival) return a.burst < b.burst;//if arrival is same then sort on basis of burst;
    return a.arrival < b.arrival; 
}

int check(){
    for(int i=0;i<ob.size();i++){
        if(ob[i].burst > 0) return 1;//some process remaining to execute
    }
    return 0;//all processes finished
}
void gantt(){
    int q;
    cout <<"enter time quantum :";
    cin >> q;
    
    for(int i=0;i<ob.size();i++){
        if(ob[i].burst > 0){
            if(ob[i].burst < q){cpu_time+=ob[i].burst;ob[i].burst = 0;}
            else {cpu_time += q;ob[i].burst -= q;}
            ob[i].finish = cpu_time;
            cout << ob[i].name << " " << ob[i].finish << "\n";
        }
        if(i == ob.size()-1){if(check()){i=-1;continue;}}
    }
}

void initialise(){
    for(int i=0;i<ob.size();i++){
        ob[i].turnaround = ob[i].finish - ob[i].arrival;
        ob[i].waiting = ob[i].turnaround - ob[i].burst_copy;
    }
}
void avg(){
    double tavg=0,wavg=0;
    int len = ob.size();
    for(int i=0;i<len;i++){
        tavg += ob[i].turnaround;
        wavg += ob[i].waiting;
    }
    
    tavg = tavg/len;
    wavg = wavg/len;
    
    cout << "average turnaround time :" << tavg << "\n";
    cout << "average waiting time :" << wavg;
}


int _tmain(int argc, _TCHAR* argv[])
{
	int count;
    cout << "enter number of processes :";
    cin >> count;
    
    for(int i=0;i<count;i++){//create a vector of all processes
        int b,a;//only burst,name,arrival are initialised
        string n;
        cout << "enter name :";
        cin >> n;
        cout << "enter burst time :";
        cin >> b;
        cout << "enter arrival time :";
        cin >> a;
        ob.push_back({a,b,b,n});
    }
    
    sort(ob.begin(), ob.end(), compareMyStructs);//sort on basis of arrival
    gantt();
    initialise();
    avg();

	return 0;
}

