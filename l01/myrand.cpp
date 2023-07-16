#include<iostream>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;

int myrand(int seed){
    long int a=1103515245, c=12345, m=pow(2,31);
    return (int)(abs(a*seed+c)%m);
}

int main(){
    int prevrand=3;
    for(int i=0;i<100;i++){
        prevrand=myrand(prevrand);
        cout<<(prevrand)%10;
    }
    cout<<endl<<RAND_MAX<<endl<<INT32_MAX;
}