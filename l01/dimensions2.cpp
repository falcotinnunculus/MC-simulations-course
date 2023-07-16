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
    srand(time(0));
    
    for(int dim=1; dim<13; dim++){
        cout<<"dim "<<dim<<endl;
        for(int n=3;n<8;n++){
            int N=pow(10,n);
            double sum=0, sumsq=0, random ,a=0, b=M_PI, rands;
            int prevrand=3000;

            for(int i=0;i<N;i++){
                rands=1;
                for(int d=0;d<dim;d++){
                    prevrand=myrand(prevrand);
                    random=prevrand/(1.0*INT32_MAX)*(b-a)+a;
                    rands*=sin(random);
                }
                sum+=rands;
                sumsq+=rands*rands;
            }

            double mean=1.0/N*sum;
            //cout<<mean<<endl;
            //cout<<sum<<endl<<sumsq<<endl;
            double stdv=sqrt((1.0/N*sumsq)-mean*mean)/sqrt(N);
            //cout<<stdv<<endl;

            cout<<N<<": "<<mean*pow(b-a,dim)<<" \\pm "<<stdv*pow(b-a,dim)<<endl;
        }
    }
}