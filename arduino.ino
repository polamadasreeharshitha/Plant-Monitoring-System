const int VAL_PROBE = A1;                 // Analog pin1 is connected to plant1 soilmoisture A0 pin
const int MOISTURE_LEVEL = 900;           // the value after the LED goes ON
const int sensorMin = A0;                 // Analog pin A0 is connected to raindrop A0
const int sensorMax = 1024;               // maximum value of soilmoisture sensor
const int VAL=A2;                         // Analog pin 2 is connected to plant1 soilmoisture A0 pin
int motorpin1=3;                          // motor 1 is connected to digital pin 3 
int motorpin2=4;                          // motor 2 is connected to digital pin 4 
int temp=0;
void setup() {
  Serial.begin(9600);                     // initialize serial communication @ 9600 baud:  
}

void LedState(int state) {
digitalWrite(13, state);
}


void loop() {
int moisture = analogRead(VAL_PROBE);      //reads the moisture level of plant1 and stored in moisture
int moisture2 = analogRead(VAL);           //reads the moisture level of plant2 and stored in moisture
int sensorReading = analogRead(A0);        //reads the output from raindrop sensor
int range = map(sensorReading, sensorMin, sensorMax, 0, 2);  //We assign a value 1 if it is raining else 0

if(moisture > MOISTURE_LEVEL) {
LedState(LOW);
} else {
LedState(HIGH);
}
 delay(460);
 switch (range) {
 case 0:    			            // Sensor getting wet
    temp=1;
    Serial.print("Raining");
    Serial.print(",");
    Serial.print(moisture);
    Serial.print(",");
    Serial.print(moisture2);
    Serial.print(",");
    //temp=1;
    break;
 case 1:    				     // Sensor not getting wet
    temp=0;
    Serial.print("Not Raining");
    Serial.print(",");
    Serial.print(moisture);
    Serial.print(",");
    Serial.print(moisture2);
    Serial.print(",");
    break;
  }
  if(temp==1){                               //If it is raining both motors stop running 
    digitalWrite(motorpin1,LOW);
    Serial.println("No");
    digitalWrite(motorpin2,LOW);
    Serial.println("No");
    
  }

/* Motor functioning is controlled based on obtained soil moisture values*/

  else{
    if(moisture>=600 & moisture2>=600){      
      Serial.println("Yes");
      Serial.print(",");
      Serial.println("Yes");
      digitalWrite(motorpin1,HIGH);
      digitalWrite(motorpin2,HIGH);
      delay(1000);
      digitalWrite(motorpin1,LOW);
      digitalWrite(motorpin2,LOW);
    }
   else if(moisture>=600 & moisture2<600){
      Serial.println("Yes");
      Serial.print(",");
      Serial.println("No");
      digitalWrite(motorpin1,HIGH);
      digitalWrite(motorpin2,LOW);
      delay(1000);
      digitalWrite(motorpin1,LOW);
    }
    else if(moisture<600 & moisture2>=600){
      digitalWrite(motorpin1,LOW);
      digitalWrite(motorpin2,HIGH);
      Serial.println("No");
      Serial.print(",");
      Serial.println("Yes");
      delay(1000);
      digitalWrite(motorpin2,LOW);
      
    }
     else if(moisture<600 & moisture2<600){
      digitalWrite(motorpin1,LOW);
      digitalWrite(motorpin2,LOW);
      Serial.println("No");
      Serial.print(",");
      Serial.println("No");
      
    }
  }  
  delay(100);  				          // delay between reads
  
}

