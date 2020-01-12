#include <dht.h>
dht DHT;
#define DHT11_PIN 7

const int pingPin = 2; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor

char code = '0';
long startDistance;

char receivedChar;

bool newData = false;

int count = 0;
void setup(){
  Serial.begin(9600);
  pinMode(9,OUTPUT); //Buzzer Alarm
  pinMode(8,OUTPUT); //Buzzer Light
  pinMode(12,INPUT);

  //State = 0 normal State = 2 Reset State = 1 Emergency
 startDistance =  calculateRange();
    

}
// Main
void loop()
{
  count += 1;
    if(code == '0'){
      code = distanceSensor(); //User Must send code 2 to stop
    }
    
    if(code == '1'){
      soundTheAlarms();
      checkForReset(); //User must send code 2 to stop
      recivedCode();
    }
    
    if(code == '2'){
      checkForTurnOn(); //User must send code 1 to start
      recivedCode();
    }
    if(count > 2){
      Serial.print("C");
      Serial.print(code);
      getTemp();
      Serial.print("E");
      count = 0;
      }
}
//Main system 

void recivedCode(){
  if (Serial.available() > 1) {    
    receivedChar = Serial.read();
    newData = true;
  }
    if(newData == true){
      if(receivedChar == '0'){
        digitalWrite(8, HIGH);
        delay(5000);
        digitalWrite(8, LOW);
        code = '0';
      }else if(receivedChar == '1'){
        code = '1';
      }else {
        code = '2';
      }
     }
      newData = false;
   return;
}
void checkForReset(){
  int resetBtn = digitalRead(12);

  if (resetBtn == HIGH){
    // reset code 
   digitalWrite(8, HIGH);
   code = '2';
   delay(5000);
   digitalWrite(8, LOW);
  return;
  }
}

void checkForTurnOn(){
  int resetBtn = digitalRead(12);
  if (resetBtn == HIGH){
    // reset code 
   digitalWrite(8, HIGH);
   code = '0';
   delay(5000);
   digitalWrite(8, LOW);
  }
  return;
}

//Sonic Code
long calculateRange(){
  long x = calculateDistances();
  delay(1000);
  long range = x;
  
  //Serial.print("Range: ");
  //Serial.println(range);
  range = abs(range);
  return range;
}

char distanceSensor(){
  long x = calculateDistances();
  delay(1000);
  long range = x - startDistance;
  range = abs(range);
  if(range > 20){
    return '1';
  }
  return '0';
}

long calculateDistances(){
    long arr[5];
  for(int i = 0; i < 5; ++i){
    arr[i] = getDistance();
  }
  return distanceAvrage(arr);
}

long getDistance(){
    long duration, inches, cm;
   pinMode(pingPin, OUTPUT);
   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   pinMode(echoPin, INPUT);
   duration = pulseIn(echoPin, HIGH);
   inches = microsecondsToInches(duration);
   //Serial.print("Inches : ");
   //Serial.println(inches);
   return inches;
}

long distanceAvrage(long avg[]){
  long total = 0;
  for(int i = 0; i < 5 ; ++i ){
   total += avg[i];
  }
  return total / 5;
}


long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

//Buzzer 

void soundTheAlarms(){
  tone(9, 1000);
  digitalWrite(8, HIGH);
  delay(500);
  noTone(9);
  digitalWrite(8, LOW);
  delay(500);
}

//Temp & Humid

void getTemp(){
    int chk = DHT.read11(DHT11_PIN);
   Serial.print("T");
   Serial.print(DHT.temperature);
   Serial.print("H");
   Serial.print(DHT.humidity);
    return;
}
