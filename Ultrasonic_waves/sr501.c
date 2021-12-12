#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define GPIOIN 17
#define GPIOOUT 27

void read(){
    uint8_t State;
    pinMode(GPIOIN, INPUT);
    pinMode(GPIOOUT, OUTPUT);
    printf("Sensor start!!");

    while(1){
        delay(1000);
        State = digitalRead(GPIOIN);
        printf("state = %d", State)
        digitalWrite(GPIOOUT, State) //LED 켜거나 끔
    }
    
}

int main(void){
    if(wiringPiSetupGPIO() == -1) {
        exit(1);
    }
    read()
    return(0);
}