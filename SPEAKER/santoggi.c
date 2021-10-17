#include <stdio.h>
#include <wiringPi.h>
#include <softTone.h>
#include <unistd.h>
#define SPEAKER 1
#define BASIC_TIME 187 //BPM
/*
    c, d, e, f, g, a, b, C
    도, 레, 미, 파, 솔, 라, 시, 도
*/
void tone(int scale, int timing);
int main(){
    char tone_scale[] = {'g','e','e','g','e','c','d','e','d','c','e','g',
    'C','g','C','g','C','g','e','g','d','f','e','d','c'} //음계
    int time_scale[] = {4,2,2,2,2,4,4,2,2,2,2,4,3,1,2,2,2,2,4,4,2,2,2,2,4}; //길이
    int count = 0;
    if(wiringPiSetup() == -1) return 1; //wPi 핀번호 사용
    softToneCreate(SPEAKER) //스피커 소리를 출력할 핀번호 설정 

    for(count = 0; count < 25; count++ ){
        tone(tone_scale[count], tone_scale[count]); 
        //tone(박자, 음계) 전달
    }
}

void tone(int scale, int timing){
    int scale_sound;
    switch(scale){
        case 'c': scale_sound = 261; break;
        case 'd': scale_sound = 293; break;
        case 'e': scale_sound = 329; break;
        case 'f': scale_sound = 349; break;
        case 'g': scale_sound = 391; break;
        case 'a': scale_sound = 440; break;
        case 'b': scale_sound = 493; break;
        case 'C': scale_sound = 523; break;
        default: scale_sound = 0; break;
    }
    softToneWrite(SPEAKER, scale_sound);
    delay(BASIC_TIME * timing);
    softToneWrite(SPEAKER, 0);
}