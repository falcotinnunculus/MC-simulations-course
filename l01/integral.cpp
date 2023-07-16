#include<iostream>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;

int main(){
    srand(time(0));
    
    for(int n=1;n<10;n++){
        int N=pow(10,n);
        double sum=0, sumsq=0, random ,a=0, b=M_PI;

        for(int i=0;i<N;i++){
            random=rand()/(1.0*RAND_MAX)*(b-a)+a;
            sum+=sin(random);
            sumsq+=sin(random)*sin(random);
        }

        double mean=1.0/N*sum;
        //cout<<mean<<endl;
        //cout<<sum<<endl<<sumsq<<endl;
        double stdv=sqrt((1.0/N*sumsq)-mean*mean)/sqrt(N);
        //cout<<stdv<<endl;

        cout<<N<<": "<<mean*(b-a)<<" \\pm "<<stdv*(b-a)<<endl;
    }
}