# RaspberryPi Study

## GPIO

- gpio -g : -g 옵션은 wiringPi 핀 번호가 아닌 GPIO_BCM 으로 해석
    - 디폴트 모드는 wiringPi 핀 번호 사용
- gpio readall : 모든 핀을 읽고, 테이블 형식으로 출력
- LED, 모터 : 출력 모드로 설정
- SW, 센서 : 입력모드로 설정


## 명령어 제어

- /sys/class/gpio 로 진입하여 명령어 제어
- 관련 디렉토리
    - export : 접근 허용
    - unexport: 접근 제거
- gpioN 내의 디렉토리 종류
    - active_low, device, direction, edge, power, subsystem, uevent, value
    - active_low 파일 : 0과 1이 반전되서 동작 (0이 켜짐, 1이 꺼짐)
    - edge : 값을 쓰면 인터럽트를 설정 (none, falling, rising, both)
- gpio export <pin> in/out : BCM-GPIO 핀 번호를 입력, 출력할 지 결정해서 export → 접근 허용한다.
- gpio pwm 18 765 : PWM 으로 선언하고, Duty 비율을 765로 출력하도록 (실제출력은 안됨)


## C언어로 제어

### wiringPi GPIO 설정 함수

- int wiringPiSetup(void) : wiringPi 핀 번호 사용
- int wiringPiSetupGpio(void) : BCM GPIO 핀 번호 사용
- int wiringPiSetupSys(void) : 직접 하드웨어에 접근X, /sys/class/gpio에 접근
- int wiringPiSetupPhys(void) : 물리 핀 번호 사용

### wiringPi GPIO 일반함수

- void pinMode(int pin, int mode);
    - INPUT, OUTPUT, PWM_OUTPUT 모드로 설정
- void digitalWrite(int pin, int value);
    - HIGH(1), LOW(0) 값을 주어진 핀에 씀
- void digitalWriteByte(int pin, int value);
    - 8비트 데이터를 출력, 하드웨어와 I2C 설정이 이루어져야 됨.
- void pwmWrite(int pin, int value);
    - 지정된 핀으로 PWM 파형 발생
    - 출력 지원 핀은 wiringPi 1,26,23,24번
    - Value = 0~1023
- void digitalRead(int value)
    - Write 한 값을 읽음. 0 또는 1 임
- void pullUpDnControl(int pin, int pud);
    - pud 값은 PUD_OFF, PUD_DOWN, PUD_UP
    - 풀업/다운 저항을 설정


## Python 제어

- 모듈 선언 : import RPi.GPIO as GPIO
- GPIO.setmode(pin) - 핀 번호 할당 방법
    - GPIO.BOARD : 물리 핀 번호 사용
    - GPIO.BCM : CPU 핀 번호 사용
- GPIO.setup(pin, in/out) - 사용할 GPIO 핀의 초기 값 설정
    - GPIO.IN : 입력
    - GPIO.OUT: 출력
    - GPIO.PUD_UP: 풀업 저항 지정
    - GPIO.PUD_DOWN: 풀다운 저항 지정
    - GPIO.HIGH : 출력시 초기상태 High로 지정
    - GPIO.LOW : 출력시 초기상태 Low로 지정
- GPIO.output(pin, state) : 지정된 핀에 state로 지정한 값 출력
    - 1 : High(3.3V)
    - 0 : Low(0V)
- GPIO.cleanup(pin) : pin에서 사용한 GPIO 해제. 프로그램 종료시 반드시 해야됨

---

### PWM (pulse width modulation)

- 아날로그 pulse(파장)를 디지털 신호의 네모 파장을 모듈화 해서 흉내낸다는 것
- 쉽게 말해 디지털 신호를 가지고 아날로그 신호를 흉내
- 아날로그는 신호가 곡선형태로 연결, but 디지털 신호는 0과 1로만 두 값만 가짐
- 디지털 → 아날로그 변환하는 방법
    - DAC (디지털 아날로그 컨버터)
    - PWM 사용해서 디지털 신호를 아날로그 처럼 보이게 하는 눈속임 !
