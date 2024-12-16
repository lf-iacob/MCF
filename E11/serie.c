#include <stdio.h>
#include <math.h>

double fibonacci(int n){
  double x=0;
  double y=0;
  double somma=1;
  for (int i=0; i<n; i++){
    if(i==n-1){
      y=somma;
    }
    somma=somma+x;
    x=somma-x;
  }
  return somma/y;
}
