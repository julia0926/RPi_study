/*
    5초마다 duty를 하나씩 증가시켜 밝기를 증가 
*/

#include <stdio.h>
#include <wiringPi.h>

#define LED_PORT 1

int main(void){
    unsigned int value = 0;
    if(wiringPiSetup() == -1)
        return 1; //WiringPi 핀 번호 사용
    pinMode(LED_PORT,PWM_OUTPUT);
    for(;;){
        for(value=0;value<1024;value++){
            pwmWrite(LED_PORT,value);
            delay(5);
        }
        return 0;
    }
}