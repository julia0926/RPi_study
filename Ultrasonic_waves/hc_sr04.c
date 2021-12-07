#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#define GPIO_TRIGGER = 17
#define GPIO_ECHO = 27

int wait_state(int state) {
    //에코 입력 핀으로 부터 상태 값을 읽는다
    //센서의 출력 값이 라즈베리 파이의 입력 
    while (digitalRead(GPIO_ECHO) == state)
    return 0;
}

int main(void){
    long start,stop;
    float distance;

    if(wiringPiSetupGpio() == -1) exit(1);
    pinMode(GPIO_TRIGGER, OUTPUT);
    pinMode(GPIO_ECHO, INPUT);
    digitalWrite(GPIO_TRIGGER, LOW);
    delay(500);

    while(1){
        digitalWrite(GPIO_TRIGGER, HIGH);
        delayMicroseconds(10);
        digitalWrite(GPIO_TRIGGER, LOW);

        wait_state(LOW);
        start = micros();

        wait_state(HIGH);
        stop = micros();

        distance = (float) (stop-start) / 58.8235;
        printf("Distance: %9.1f cm \n", distance);
        delay(100);

    }
    return 0;
}