#include <stdio.h>
#include <unistd.h>
#include <wiringPi.h>
#include <softTone.h>
#define SPEAKER 1
#define BASIC_TIME 150
void tone(int scale,int timing);
int main(){
char tone_scale[] = {'c','c','g','g','a','a','g','f','f','e','e','d','d','c','g','g','f','f','e','e','d','g','g','f','f','e','e','d','c','c','g','g','a','a','g','f','f','e','e','d','d','c'};
int time_scale[] = {2,2,2,2,2,2,4,2,2,2,2,2,2,4,2,2,2,2,2,2,4,2,2,2,2,2,2,4,2,2,2,2,2,2,4,2,2,2,2,2,2,4};
int counter = 0;
if(wiringPiSetup() == -1)
return 0;
softToneCreate(SPEAKER);

for(counter = 0; counter < 42; counter++){
tone(tone_scale[counter], time_scale[counter]);
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