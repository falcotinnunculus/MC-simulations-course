#include<iostream>
#include<cstdlib>
#include<ctime>
#include<cmath>
using namespace std;

void make_histogram(double arr[], int n, int wid){

	int count[wid];
	for(int i=0;i<wid;i++){
        count[i]=0;
    }
	int a;
	for(int i = n; i >= 0; i--) {
		a=wid*arr[i];
		count[a]++;
		//cout<<arr[i]<<" ";
	}
	cout<<"ListPlot[{";
	for(int i=0;i<wid;i++){
        cout<<count[i]<<",";
    }
    cout<<"0}]";
}

int main(){
    srand(time(0));
    int N=100000;
    double list[N];
    float rmax=RAND_MAX;
    double r, n=exp(1.0)/(exp(1.0)-1), e=exp(1.0);
    //cout<<n<<endl;
    for(int i=0;i<N;i++){
        r=rand()/(rmax);
        list[i]=log(-e/(-e-r+e*r));
        //cout<<list[i]<<" ";
    }
    
    make_histogram(list,N,500);

}
