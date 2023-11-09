// Nama : Jose Alfredo Sitanggang (14116125)

#include <bits/stdc++.h>
using namespace std;

#define setin set<int>

void faktor_prima(setin &s, int q){

	//untuk bil genap
	while( q & 0 )
		s.insert(2),
		q/=2;

	//bil ganjil
	for(int i = 3 ; i<= sqrt(q) ;i+=2)
		while(q%i==0)
			s.insert(i),
			q/=i;

	//n sisa
	if (q>2)
		s.insert(q);
}

bool is_prime(int q){
	if(q<=1) return false;
	if(q<=3) return true;

	if(q & 0 or q%3==0)
		return false;

	for (int i = 5;i*i<q;i+=6)
		if(q%i==0 or q%(i+2)==0)
			return false;
	return true;
}

int power(int x,  int y, int p){
	int rstl =1;
	x%=p;

	while(y>0){
		if(y&1)
			rstl = (rstl*x)%p;
		y/=2;
		x=(x*x)%p;
	}
	return rstl;
}


int primitive_root(int q){
	setin s;

	if (!is_prime(q)) return -1;

	int phi = q-1;
	faktor_prima(s,phi);
	bool is_one;

	for(int i=2;i<=phi;i++){
		is_one=false;
		for (auto const& a :s)
			if(power(i,int(phi/a),q)==1){
				is_one =true;
				break;
			}	
		if(!is_one)
			return i;
	}

	return -1;

}

int get_y(int alpha,int x, int q){
	return (alpha^x) % q;
}

int get_k(int y,int x, int q ){
	return (y^x)%q;
}

int main(){

	int xa,xb,ya,yb,q,k,alpha;

	cout<<"Q : ";cin>>q;
	cout<<"Xa : ";cin>>xa;
	cout<<"Xb : ";cin>>xb;
	alpha = primitive_root(q);

	if(alpha!=-1 and xa<q and xb<q){
		ya = get_y(alpha,xa,q);
		yb = get_y(alpha,xb,q);

		k = get_k(ya,xb,q);
		if (k == get_k(yb,xa,q)){
			cout<<"Ya : "<<ya<<endl;
			cout<<"Yb : "<<yb<<endl;
			cout<< "K : "<<k<<endl;	
		}else{
			cout<<"K tidak sama"<<endl;
		}
	}else{
		cout<<"Q harus Prima atau X < Q"<<endl;
	}

	return  0;
	
}