//LED 켜고 끄는 것을 스위치로 제어

#include <stdio.h>
#include <wiringPi.h>
#define LED1 4
#define SW1 1

int main(void){
    unsigned int i = 0;
    if(wiringPiSetup() == -1) return 1;
    pinMode(LED1,OUTPUT);
    pinMode(SW1, INPUT);
    pinMode(SW1, PUD_DOWN); 
    //pull down 하면 스위치가 눌렷을 때 1, 안눌리면 0
    for(;;){
        if(digitalRead(SW1) == 1){
            if(i==0) i==1;
            else i==0;
        }
        digitalWrite(LED1, i);
    }
    return 0;
}