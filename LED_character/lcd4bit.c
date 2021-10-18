#include <wiringPi.h>
#include <lcd.h> //lcd 함수를 사용하기 위함
#include <stdio.h>

#define LCD_RS 11 //high일 때 register 지정, 아니면 지정 X
#define LCD_E 12 //LCD 제어하는 신호 역할
#define LCD_D4 23
#define LCD_D5 22
#define LCD_D6 21
#define LCD_D7 14 //4~7번 모두 WiringPi 핀 번호

int main(){
    int lcd;
    wiringPiSetup(); //wiringPi 핀 번호 사용
    // 2*16 display 사용하고, 4비트 연결모드라서 4~7까지의 값만 들어가고 나머지는 0
    lcd = lcdInit(2, 16, 4, LCD_RS, LCD_E, LCD_D4, LCD_D5, LCD_D6, LCD_D7, 0, 0, 0, 0);
    lcdPosition(lcd, 0, 0); //LCD 커서를 지정된 위치로 이동
    lcdPuts(lcd, "Hello, World!"); //파일 디스크립터로 지정된 LCD에 문자열을 출력
}

/*
실행
gcc -o lcd4bit lcd4bit.c -lwiringPi -lwiringPiDev
sudo ./lcd4bit
*/
