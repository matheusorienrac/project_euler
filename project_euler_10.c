#include <time.h>

int v[1000000]; // vector that we will add all prime numbers found
int array_index = 0; // index that contains the latest prime added to v
int last_prime = 0; // index that contains the last prime in v that is imeddiately
//bigger than half of the next number to be checked as prime to reduce amount
//of testing in is_prime function

int main(){ 
     time_t start;
     time_t end;
     start = time(NULL);
     float sum = 2; // start from 2 so that we can skip even numbers without
     //adding another if statement in our for loop
     v[0] = 2;
     int i;
     for(i = 3; i<2000000 ;i = i + 2){ //skipping all even numbers, because
     //they are not prime
           if(is_prime(i)){
                           sum += i;
                           v[array_index] = i;
                           while(v[last_prime] < (i+2)/2){
                                   last_prime++;        
                           }
                           array_index++;
           }
     }

     end = time(NULL); 
     printf("Runtime %ld\n", end - start);
     printf("Sum: %f", sum);
     getchar();
     return(0);
       
}
          

int is_prime(int number){
        int i;
        if (number != 5 && number % 10 == 5){
                  return(0);          
        }
        for( i = 0; i <= last_prime; i++){
              if(number % v[i] == 0){
                        return(0); 
              }      
        }        
        return(1);
        
        
}
